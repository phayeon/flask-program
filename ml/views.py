import pandas as pd
from ml.stroke import StrokeService

df = StrokeService().stroke_read()

class StrokeController:

    @staticmethod
    def menu_1():
        print('뇌졸중은 어떻게 발병하는가.')

    @staticmethod
    def menu_2():
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(df.info())
        print(df.head(3))

    @staticmethod
    def menu_3():
        print(df["stroke"].head(3))

    @staticmethod
    def menu_4():
        print(f'고유 값 개수 : {len(pd.unique(df["id"]))}')
        print(f'데이터 타입 : {df["stroke"].dtype}')
        print(f'타깃 변수 분포 : {df["stroke"].isnull().sum()}')
        print(f'타깃 변수 분포 : {df["stroke"].value_counts(dropna=False, normalize=True)}')

    @staticmethod
    def menu_5():
        df1 = df[df['age'] > 18]
        print(df1.isna().any()[lambda x:x]) # 결측값을 갖고 있는 column 찾기
        print(df['bmi'].isnull().mean())
