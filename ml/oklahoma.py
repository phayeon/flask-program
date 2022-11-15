from imblearn.under_sampling import RandomUnderSampler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder

oklahoma_meta = {}
OKLAHOMA_MENUS = ["종료",  # 0
                  "차원 축소",  # 1
                  "interval",  # 2
                  "nominal", # 3
                  "ordinal", # 4
                  "target", # 5
                  "partition"] # 6
oklahoma_menu = {
    "1": lambda x: x.oklahoma_spec(),
    "2": lambda x: x.interval_variables(),
    "3": lambda x: x.nominal_variables(),
    "4": lambda x: x.ordinal_variables(),
    "5": lambda x: x.oklahoma_target(),
    "6": lambda x: x.partition()
}


class OklahomaService:
    def __init__(self):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        self.okl = pd.read_csv('./data/comb32.csv')
        self.my_okl = self.okl.rename(columns=oklahoma_meta)
        self.data = None
        self.target = None
        # print(self.my_okl.columns)

    '''
    1. Spec
    '''

    def oklahoma_spec(self):
        print(" --- 1.Shape ---")
        print(self.my_okl.shape)
        print(" --- 2.Features ---")
        print(self.my_okl.columns)
        print(" --- 3.Info ---")
        print(self.my_okl.info())
        print(" --- 4.Case Top1 ---")
        print(self.my_okl.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.my_okl.tail(3))
        print(" --- 6.Describe ---")
        print(self.my_okl.describe())
        print(" --- 7.Describe All ---")
        print(self.my_okl.describe(include='all'))

    '''
    2~4. 변수의 분류
    '''

    def interval_variables(self):
        pd.options.display.float_format = '{:.2f}'.format
        category = ['AGEP', 'BDSP', 'CONP', 'ELEP', 'GASP',
                    'HINCP', 'NRC', 'RMSP', 'VALP']
        print(self.my_okl[category].describe())
        print('--- 왜도 ---\n', self.my_okl[category].skew())
        print('--- 첨도 ---\n', self.my_okl[category].kurtosis())
        self.my_okl.drop('CONP', axis=1, inplace=True)

        c1 = self.my_okl['ELEP'] <= 500
        c2 = self.my_okl['GASP'] <= 311
        c3 = self.my_okl['HINCP'] <= 320000

        df1 = self.my_okl[c1 & c2 & c3]
        df1.to_csv('./save/comb31-IQR30.csv', index=False)
        print(f'--- 이상치 제거 후 스펙 ---\n', df1.shape)

    def nominal_variables(self):
        category = ['AGEP', 'BDSP', 'ELEP', 'GASP',
                    'HINCP', 'NRC', 'RMSP', 'VALP']
        df_interval = self.my_okl[category]
        df = self.my_okl.drop(category, axis=1)
        df_category = df
        comb = pd.concat([df_interval, df_category], axis=1)
        comb.sort_index(axis=1, inplace=True)
        comb.to_csv('./save/comb32.csv', index=False)
        print(comb.columns)

    def ordinal_variables(self):
        pass

    '''
    5. 타겟 설정
    '''

    def oklahoma_target(self):
        df = pd.read_csv('./save/comb31-IQR30.csv')
        self.data = df.drop(['VALP_B1'], axis=1)
        self.target = df['VALP_B1']
        print(f'--- data shape --- \n {self.data.shape}')
        print(f'--- target shape --- \n {self.target.shape}')

    '''
    6. 파티션
    '''

    def partition(self):
        data = self.data
        target = self.target
        undersample = RandomUnderSampler(sampling_strategy=1, random_state=2)
        data_under, target_under = undersample.fit_resample(data, target)
        print(target_under.value_counts(dropna=True))
        X_train, X_test, y_train, y_test = train_test_split(
            data_under, target_under, test_size=0.5,
            random_state=42, stratify=target_under)

        print("X_train shape : ", X_train.shape)
        print("X_test shape : ", X_test.shape)
        print("y_train shape : ", y_train.shape)
        print("y_test shape : ", y_test.shape)
