import copy
from imblearn.under_sampling import RandomUnderSampler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder

STROKE_MENUS = ["종료",  # 0
                "데이터 구조 파악(Spec)",  # 1
                "변수 한글화(Rename)",  # 2
                "연속형(Interval) 변수 편집",  # 3 18세 이상만 사용함
                "범주형(Norminal) 변수 편집",  # 4
                "타깃(Target)",  # 5
                "파티션(Partition)",  # 6
                "학습",  # 7
                "예측"]  # 8

stroke_meta = {
    'id': '아이디', 'gender': '성별', 'age': '나이',
    'hypertension': '고혈압',
    'heart_disease': '심장병',
    'ever_married': '기혼 여부',
    'work_type': '직종',
    'Residence_type': '거주 형태',
    'avg_glucose_level': '평균 혈당',
    'bmi': '체질량 지수',
    'smoking_status': '흡연 여부',
    'stroke': '뇌졸중'
}
stroke_menu = {
    "1": lambda x: x.spec(),
    "2": lambda x: x.rename_meta(),
    "3": lambda x: x.interval_variables(),
    "4": lambda x: x.norminal_variables(),
    "5": lambda x: x.target(),
    "6": lambda x: x.partition()
}

'''
Data columns (total 12 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 5110 non-null   int64  
 1   gender             5110 non-null   object 
 2   age                5110 non-null   float64
 3   hypertension       5110 non-null   int64  
 4   heart_disease      5110 non-null   int64  
 5   ever_married       5110 non-null   object 
 6   work_type          5110 non-null   object 
 7   Residence_type     5110 non-null   object 
 8   avg_glucose_level  5110 non-null   float64
 9   bmi                4909 non-null   float64
 10  smoking_status     5110 non-null   object 
 11  stroke             5110 non-null   int64  
dtypes: float64(3), int64(4), object(5)
'''


class StrokeService:
    def __init__(self):
        self.stroke = pd.read_csv('../../../static/data/dam/stroke/healthcare-dataset-stroke-data.csv')
        self.my_stroke = self.stroke.rename(columns=stroke_meta)
        self.adult_stroke = copy.deepcopy(self.my_stroke)

    '''
   1.스펙 보기
   '''

    def spec(self):
        print(" --- 1.Shape ---")
        print(self.stroke.shape)
        print(" --- 2.Features ---")
        print(self.stroke.columns)
        print(" --- 3.Info ---")
        print(self.stroke.info())
        print(" --- 4.Case Top1 ---")
        print(self.stroke.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.stroke.tail(3))
        print(" --- 6.Describe ---")
        print(self.stroke.describe())
        print(" --- 7.Describe All ---")
        print(self.stroke.describe(include='all'))

    '''
   2.한글 메타 데이터
   '''

    def rename_meta(self):
        print(" --- 2.Features ---")
        print(self.my_stroke.columns)

    '''
    3.타깃 변수(= 종속 변수 dependent, Y값) 설정
    입력 변수(= 설명 변수, 확률 변수, X값)
    타깃 변수명: stroke (=뇌졸중)
    타깃 변수값: 과거에 한 번이라도 뇌졸중이 발병했으면 1, 아니면 0
    인터벌 = ['나이','평균 혈당','체질량 지수']
    '''

    def interval_variables(self):
        interval = ['나이', '평균 혈당', '체질량 지수']
        print(f'--- 구간 변수 타입 ---\n{self.my_stroke[interval].dtypes}')
        stroke1 = self.my_stroke[self.my_stroke['나이'] > 18]
        print(f'--- 결측 값을 가진 column ---\n{stroke1.isna().any()[lambda x: x]}')
        print(f"--- 체질량 결측값 비율 확인 ---\n{self.my_stroke['체질량 지수'].isnull().mean()}")
        print(f'고유 값 개수 : {len(pd.unique(self.my_stroke["아이디"]))}')
        pd.options.display.float_format = '{:.2f}'.format
        print(f'--- 구간 변수 기초 통계량 --- \n{self.my_stroke[interval].describe()}')
        criterion = self.my_stroke['나이'] > 18
        self.adult_stoke = self.my_stroke[criterion]
        print(f'--- 성인 객체 스펙 --- \n{self.adult_stoke.shape}')
        # 평균 혈당 232.64이하와 체질량 지수 60.3이하를 이상치로 규정 하고 제거함
        self.adult_stoke
        c1 = self.adult_stoke['평균 혈당'] <= 232.64
        c2 = self.adult_stoke['체질량 지수'] <= 60.3
        self.adult_stoke = self.adult_stoke[c1 & c2]
        print(f'--- 이상치 제거한 성인 객체 스펙 ---\n{self.adult_stoke.shape}')

    '''
    4.범주형 = ['성별', '심장병', '기혼 여부', '직종', '거주 형태', '흡연 여부', '뇌졸중']
    '''

    def ratio_variables(self):  # 해당 칼럼이 없음
        pass

    def norminal_variables(self):
        category = ['성별', '심장병', '기혼 여부', '직종', '거주 형태', '흡연 여부', '고혈압']
        print(f'--- 범주형 변수 데이터 타입 ---\n{self.adult_stroke[category].dtypes}')
        print(f'--- 범주형 변수 결측값 ---\n{self.adult_stroke[category].isnull().sum()}')
        print(f'--- 결측 값 있는 변수 ---\n{self.adult_stroke[category].isna().any()[lambda x: x]}')
        self.adult_stroke['성별'] = OrdinalEncoder().fit_transform(self.adult_stroke['성별'].values.reshape(-1, 1))
        self.adult_stroke['기혼 여부'] = OrdinalEncoder().fit_transform(self.adult_stroke['기혼 여부'].values.reshape(-1, 1))
        self.adult_stroke['직종'] = OrdinalEncoder().fit_transform(self.adult_stroke['직종'].values.reshape(-1, 1))
        self.adult_stroke['거주 형태'] = OrdinalEncoder().fit_transform(self.adult_stroke['거주 형태'].values.reshape(-1, 1))
        self.adult_stroke['흡연 여부'] = OrdinalEncoder().fit_transform(self.adult_stroke['흡연 여부'].values.reshape(-1, 1))

        self.stroke = self.adult_stroke
        self.spec()
        self.stroke.to_csv('../../../static/save/dam/stroke/stroke.csv')
        print(" ### 프리 프로세스 종료 ### ")

    def ordinal_variables(self):  # 해당 칼럼이 없음
        pass

    def target(self):
        df = pd.read_csv('../../../static/save/dam/stroke/stroke.csv')
        self.data = df.drop(['뇌졸중'], axis=1)
        self.target = df['뇌졸중']
        print(f'--- data shape --- \n {self.data}')
        print(f'--- target shape --- \n {self.target}')

    def partition(self):
        data = self.data
        target = self.target
        undersample = RandomUnderSampler(sampling_strategy=0.333, random_state=2)
        data_under, target_under = undersample.fit_resample(data, target)
        print(target_under.value_counts(dropna=True))
        X_train, X_test, y_train, y_test = train_test_split(data_under, target_under, test_size=0.5, random_state=42,
                                                            stratify=target_under)

        print("X_train shape : ", X_train.shape)
        print("X_test shape : ", X_test.shape)
        print("y_train shape : ", y_train.shape)
        print("y_test shape : ", y_test.shape)


if __name__ == '__main__':
    def my_menu(ls):
        for i, j in enumerate(ls):
            print(f"{i}. {j}")
        return input('메뉴선택: ')


    t = StrokeService()
    while True:
        menu = my_menu(STROKE_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            try:
                stroke_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")
