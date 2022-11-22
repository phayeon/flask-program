import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

MENUS = ["종료",
         "메타데이터 출력",
         "poptotal/popasian 변수를 total/asian로 이름변경",
         "전체 인구 대비 아시아 인구 백분율 변수 추가",
         "아시아 인구 백분율 전체 평균을 large/small 로 분류",
         "large/small 빈도표와 빈도막대그래프 작성"]


def menulist():
    [print(f'{i}. {j}') for i, j in enumerate(MENUS)]
    return input("메뉴 입력 : ")


def menuprint(num):
    [print(j) for i, j in enumerate(MENUS) if str(i) == num]


class MidController:
    def __init__(self):
        self.midwest = pd.read_csv('../../../../../static/data/dam/per/midwest.csv')

    def mid_view(self):
        return print(self.midwest.head())

    def mid_rename(self):
        self.midwest = self.midwest.rename(columns={'poptotal': 'total'})
        self.midwest = self.midwest.rename(columns={'popasian': 'asian'})

    def mid_percentage(self):
        self.midwest['asi_per'] = (self.midwest['asian'] / self.midwest['total']) * 100

    def mid_average(self):
        self.mid_percentage()
        self.midwest['asi_avg'] = np.where(self.midwest['asi_per'] >= self.midwest['asi_per'].mean(), 'large', 'small')
        return self.midwest['asi_avg'].value_counts()

    def mid_plt(self):
        self.mid_average().plot.bar(rot=0)
        plt.savefig('../../../../../static/save/dam/per/midwest_avr.png')
        plt.show()


if __name__ == '__main__':
    mid = MidController()
    while True:
        menu = menulist()
        menuprint(menu)
        if menu == '0':
            break
        elif menu == '1':
            mid.mid_view()
        elif menu == '2':
            mid.mid_rename()
            print(mid.midwest.columns)
        elif menu == '3':
            mid.mid_rename()
            mid.mid_percentage()
            mid.mid_view()
        elif menu == '4':
            mid.mid_rename()
            mid.mid_average()
            mid.mid_view()
        elif menu == '5':
            mid.mid_rename()
            mid.mid_plt()
        else:
            print("다시 입력 해 주세요.")
