import pandas as pd

house_meta = {'SERIALNO': '일련번호','VALP': '주택가격'}
HOUSE_MENUS = ["종료",    # 0
                  "가구의 데이터 구조 파악", # 1
                  "개인의 데이터 구조 파악", # 2
                  "가구와 개인의 데이터 병합", # 3
                  "타깃 변수 설정"]
house_menu = {
    "1": lambda x: x.house_spec(),
    "2": lambda x: x.indiv_spec(),
    "3": lambda x: x.oklahoma_merge(),
    "4": lambda x: x.oklahoma_target()
}

class HouseService:
    def __init__(self):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        self.house = pd.read_csv('./data/oklahoma-house.csv')
        self.indiv = pd.read_csv('./data/oklahoma-indiv.csv')
        self.my_house = self.house.rename(columns=house_meta)
        self.my_indiv = self.indiv.rename(columns=house_meta)
        self.comb = None

    '''
    1. 가구의 데이터 구조 파악
    '''
    def house_spec(self):
        print('가구 데이터 개수 :', self.my_house.shape)
        print('가구 데이터 타입 :', self.my_house['일련번호'].dtypes)
        print('가구 결측 값 :', self.my_house['일련번호'].isnull().sum())
        print('일련번호 중복 값 확인 :', len(pd.unique(self.my_house['일련번호'])))
        mask = pd.to_numeric(self.my_house['일련번호'], errors='coerce').isna()
        print('일련번호 정수가 아닌 값 확인 :', mask.sum())

    '''
    2. 개인의 데이터 구조 파악
    '''
    def indiv_spec(self):
        print('개인 데이터 개수 :', self.my_indiv.shape)
        print('개인 데이터 타입 :', self.my_indiv['일련번호'].dtypes)
        print('개인 결측 값 :', self.my_indiv['일련번호'].isnull().sum())
        print('일련번호 중복 값 확인 :', len(pd.unique(self.my_indiv['일련번호'])))
        mask = pd.to_numeric(self.my_indiv['일련번호'], errors='coerce').isna()
        print('일련번호 정수가 아닌 값 확인 :', mask.sum())

    '''
    3. 가구와 개인의 데이터 병합
    '''
    def oklahoma_merge(self):
        self.comb = pd.merge(self.my_indiv, self.my_house, how='inner', on='일련번호')
        comb_left = pd.merge(self.my_indiv, self.my_house, how='left', on='일련번호')
        print('inner 병합 결과 :', self.comb.shape)
        print('left 병합 결과 :', comb_left.shape)
        self.comb.to_csv('./save/oklahoma.csv')

    '''
    4. 타깃 변수 설정
    '''
    def oklahoma_target(self):
        print(self.comb['주택가격'].dtype)