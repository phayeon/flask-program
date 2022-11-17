'''
데이터를 활용해서 서울시내 경찰서 범죄발생과
검거율 현황지도(폴리움)를 작성하시오.
'''
import copy
import pickle

import googlemaps
import numpy as np
import pandas as pd

cctv_meta = {
    '기관명': '관서명'
}
CRIME_MENUS = ['종료',
               'Show Spce',
               'Save police_pos',
               'Save cctv_pop',
               'Save police_norm']

crime_menu = {
    "1": lambda x: x.crime_spec(),
    "2": lambda x: x.save_police_pos(),
    "3": lambda x: x.save_cctv_pop(),
    "4": lambda x: x.save_police_norm()
}


def save_police_norm():
    polic_pos = pd.read_pickle('./save/police-pos.pkl')
    police = pd.pivot_table(polic_pos, index='구별', aggfunc=np.sum)
    police['살인 검거율'] = police['살인 검거'].astype(int) / police['살인 발생'].astype(int) * 100
    police['강도 검거율'] = police['강도 검거'].astype(int) / police['강도 발생'].astype(int) * 100
    police['강간 검거율'] = police['강간 검거'].astype(int) / police['강간 발생'].astype(int) * 100
    police['절도 검거율'] = police['절도 검거'].astype(int) / police['절도 발생'].astype(int) * 100
    police['폭력 검거율'] = police['폭력 검거'].astype(int) / police['폭력 발생'].astype(int) * 100
    police.drop(columns={'살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'}, axis=1)
    print(police)


class CrimeSevrvice:
    def __init__(self):
        self.crime = pd.read_csv('./data/crime_in_seoul.csv')
        cols = ['절도 발생', '절도 검거', '폭력 발생', '폭력 검거']
        self.crime[cols] = self.crime[cols].replace(',', '', regex=True).astype(int)
        self.cctv = pd.read_csv('./data/cctv_in_seoul.csv')
        self.my_crime = copy.deepcopy(self.crime)
        self.my_cctv = self.cctv.rename(columns=cctv_meta)
        self.pop = pd.read_excel('./data/pop_in_seoul.xls', skiprows=[0, 2],
                                 usecols=['자치구', '합계', '한국인', '등록외국인', '65세이상고령자'])
        self.ls = [self.crime, self.cctv, self.pop]

    '''
    1~2. Spec
    Id      관서명
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

    def save_police_pos(self):  # nominal
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
        # 구와 경찰서 위치가 다른 경우 수작업
        crime.loc[crime['관서명'] == '혜화서', ['구별']] == '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] == '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] == '양천구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] == '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] == '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] == '강남구'
        crime.to_csv('./save/crime_gu.csv', index=False)
        crime.to_pickle('./save/police-pos.pkl')
        print('--- 저장 완료 ---')
        print('--- 데이터 로드 ---')
        print(pd.read_pickle('./save/police-pos.pkl'))

    def crime_mean(self):
        category = ['살인 발생', '강도 발생', '강간 발생',
                    '절도 발생', '폭력 발생']
        self.my_crime[category] = pd.to_numeric(self.my_crime[category])
        self.my_crime['범죄 발생 수'] = self.my_crime[category].sum()
        print(self.my_crime.head(3))

    '''
    3. =
    '''

    def save_cctv_pop(self):  # ratio
        self.cctv.rename(columns={self.cctv.columns[0]: '구별'}, inplace=True)
        self.pop.rename(columns={
            self.pop.columns[0]: '구별',
            self.pop.columns[1]: '인구수',
            self.pop.columns[2]: '한국인',
            self.pop.columns[3]: '외국인',
            self.pop.columns[4]: '고령자',
        }, inplace=True)
        self.pop.drop(index=26, inplace=True)
        self.pop['외국인 비율'] = self.pop['외국인'].astype(int) / self.pop['인구수'].astype(int) * 100
        self.pop['고령자 비율'] = self.pop['고령자'].astype(int) / self.pop['인구수'].astype(int) * 100
        self.cctv.drop(['2013년도 이전', '2014년', '2015년', '2016년'], axis=1, inplace=True)
        cctv_pop = pd.merge(self.cctv, self.pop, on='구별')
        cor1 = np.corrcoef(cctv_pop['고령자 비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인 비율'], cctv_pop['소계'])
        print(f'고령자 비율과 CCTV의 상관계수 {str(cor1)} \n'
              f'외국인 비율과 CCTV의 상관계수 {str(cor2)} ')
        """
         고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                     [-0.28078554  1.        ]] 
         외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                     [-0.13607433  1.        ]]
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                    [-0.28078554  1.        ]]
        외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                    [-0.13607433  1.        ]]                        
        """
        cctv_pop.to_pickle('./save/cctv_pop.pkl')
        print('--- 저장 완료 ---')
        print(pd.read_pickle('./save/cctv_pop.pkl'))

    def ordinal(self):
            pass

