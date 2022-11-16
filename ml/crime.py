'''
데이터를 활용해서 서울시내 경찰서 범죄발생과
검거율 현황지도(폴리움)를 작성하시오.

Taget   검거율 = 비율 column 추가
'''
import copy

import googlemaps
import pandas as pd

cctv_meta = {
    '기관명': '관서명'
}
CRIME_MENUS = ['종료',
               'Spce',
               'Merge',
               'pop_xls']
crime_menu = {
    "1": lambda x: x.crime_spec(),
    "2": lambda x: x.save_police_pos(),
    "3": lambda x: x.pop_xls()
}


class CrimeSevrvice:
    def __init__(self):
        self.crime = pd.read_csv('./data/crime_in_seoul.csv')
        self.cctv = pd.read_csv('./data/cctv_in_seoul.csv')
        self.my_crime = copy.deepcopy(self.crime)
        self.my_cctv = self.cctv.rename(columns=cctv_meta)
        self.ls = [self.crime, self.cctv]
        self.pop = pd.read_excel('./data/pop_in_seoul.xls', skiprows=[0, 2])

    '''
    1~2. Spec
    Id      관서명
    Index(['관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생', '강간 검거', '절도 발생',
        '절도 검거', '폭력 발생', '폭력 검거'], dtype='object')
    '''

    def crime_spec(self):
        [(lambda x: print(f"--- 1.Shape ---\n{x.shape}\n"
                               f"--- 2.Features ---\n{x.columns}\n"
                               f"--- 3.Info ---\n{x.info}\n"
                               f"--- 4.Case Top1 ---\n{x.head(1)}\n"
                               f"--- 5.Case Bottom1 ---\n{x.tail(3)}\n"
                               f"--- 6.Describe ---\n{x.describe()}\n"
                               f"--- 7.Describe All ---\n{x.describe(include='all')}"))(i) for i in self.ls]

    '''
    2. 범죄율 합산 및 비율 칼럼 생성
    일부 데이터 정수형 변경 필요
    '''

    def save_police_pos(self):
        crime = self.crime
        station_names = []
        for name in crime['관서명']:
            print(f"지역 이름 : {name[:-1]}")
            station_names.append(f'서울{str(name[:-1])}경찰서')
        print(f'--- 서울시 내 경찰서는 총 {len(station_names)}개 이다. ---')
        [print(f'경찰서 이름 : {str(i)}') for i in station_names]
        gmaps = (lambda x: googlemaps.Client(key=x))('')
        print(gmaps.geocode('서울중부경찰서', language="ko"))
        print('--- API에서 주소 추출 시작 ---')
        station_addrs = []
        station_lats = []
        station_lngs = []
        for i, name in enumerate(station_names):
            _ = gmaps.geocode(name, language="ko")
            print(f'name {i} = {_[0].get("formatted_address")}')
            station_addrs.append(_[0].get('formatted_address'))
            _loc = _[0].get('geometry')
            station_lats.append(_loc['location']['lat'])
            station_lngs.append(_loc['location']['lng'])
        gu_names = []
        for name in station_addrs:
            _ = name.split()
            gu_name = [gu for gu in _ if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        crime.to_csv('./save/crime_gu.csv', index=False)

    def crime_mean(self):
        category = ['살인 발생', '강도 발생', '강간 발생',
                    '절도 발생', '폭력 발생']
        self.my_crime[category] = pd.to_numeric(self.my_crime[category])
        self.my_crime['범죄 발생 수'] = self.my_crime[category].sum()
        print(self.my_crime.head(3))

    '''
    3. xls 데이터 처리
    '''
    def pop_xls(self):
        category = ['자치구', '합계', '한국인', '등록외국인', '65세이상고령자']
        # self.pop = self.pop[category]
        self.pop = self.pop.iloc[:,[1, 3, 6, 9, 13]]
        print(self.pop.head(3))

    def interval(self):
        pass

    def ratio(self):
        pass

    def ordinal(self):
        pass

    def nominal(self):
        pass
