import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


my_meta = {
    "manufacturer": "회사",
    "model": "모델",
    "displ": "배기량",
    "year": "연식",
    "cyl": "실린더",
    "trans": "차축",
    "drv": "오토",
    "cty": "도시연비",
    "hwy": "도로연비",
    "fl": "연료",
    "class": "차종"}

MENUS = ["종료",
         "mpg 앞부분 확인",
         "mpg 뒷부분 확인",
         "행,열 출력",
         "데이터 속성 확인",
         "요약 통계량 출력",
         "문자 변수 요약 통계량 함께 출력",
         "manufacturer 을 company 로 바꾸기",
         "파생 변수 만들기",
         "빈도표 만들기",
         "빈도 막대 그래프 만들기",
         "displ(배기량)이 4이하와 5이상 자동차의 hwy(고속도로 연비) 비교",
         "아우디와 토요타 중 도시연비(cty) 평균이 높은 회사 검색",
         "쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균",
         # mpg 150페이지 문제
         # 메타데이터가 category, cty 데이터는 해당 raw 데이터인 객체생성
         # 후 다음 문제 풀이
         "suv / 컴팩 자동차 중 어떤 자동차의 도시연비 평균이 더 높은가?",
         # mpg 153페이지 문제
         "아우디차에서 고속도로 연비 1~5위 출력하시오",
         # mpg 158페이지 문제
         "평균연비가 가장 높은 자동차 1~3위 출력하시오"]



def menulist():
    [print(f'{i}. {j}') for i, j in enumerate(MENUS)]
    return input("메뉴 선택 : ")


def menuprint(num):
    [print(j) for i, j in enumerate(MENUS) if str(i) == num]


class MpgService:
    def __init__(self):
        self.mpg = pd.read_csv('./data/mpg.csv')

    def mpg_rename(self):
        return self.mpg.rename(columns=my_meta)

    def mpg_test(self):
        mpg = self.mpg
        mpg['total'] = (mpg['cty'] + mpg['hwy']) / 2
        mpg['test'] = np.where(mpg['total'] >= 20, 'pass', 'fail')

    def mpg_value(self):
        self.mpg_test()
        return self.mpg['test'].value_counts()

    def mpg_plt(self):
        self.mpg_value().plot.bar(rot=0)
        plt.savefig('./save/test.png')
        plt.show()

    def mpg_comparison(self):
        mpg = self.mpg
        hwy4 = mpg.query('displ <= 4')
        hwy5 = mpg.query('displ >= 5')
        print(f'4이상 : {hwy4["hwy"].mean()}')
        print(f'4이상 : {hwy5["hwy"].mean()}')

    def mpg_cty(self):
        mpg = self.mpg
        cty_a = mpg.query('manufacturer == "audi"')
        cty_t = mpg.query('manufacturer == "toyota"')
        if cty_a["cty"].mean() > cty_t["cty"].mean():
            print('아우디')
        else:
            print('토요타')

    def mpg_hwy_evg(self):
        mpg = self.mpg
        hwy_c = mpg.query('manufacturer == "chevrolet"')
        hwy_f = mpg.query('manufacturer == "ford"')
        hwy_h = mpg.query('manufacturer == "honda"')
        print((hwy_c["hwy"].mean() + hwy_f["hwy"].mean() + hwy_h["hwy"].mean()) / 3)

    def mpg_class_cty(self):
        mpg = self.mpg_rename()
        cty_s = mpg.query('차종 == "suv"')
        cty_c = mpg.query('차종 == "compact"')
        if cty_s["도시연비"].mean() > cty_c["도시연비"].mean():
            print('suv 가 연비 더 좋아~')
        else:
            print('compact 가 연비 더 좋아~')

    def mpg_audi_hwy(self):
        mpg = self.mpg
        hwy_a = mpg.query('manufacturer == "audi"')
        hwy_a = hwy_a.sort_values('hwy', ascending=False)
        print(hwy_a.head(5))

    def mpg_sort_hwy(self):
        mpg = self.mpg
        mpg['pyb'] = (mpg["cty"] + mpg['hwy']) / 2
        hwy_a = mpg.sort_values('pyb', ascending=False)
        print(hwy_a.head(3))


if __name__ == '__main__':
    con = MpgService()
    while True:
        menu = menulist()
        menuprint(menu)
        if menu == '0':
            break
        elif menu == '1':
            print(con.mpg.head())
        elif menu == '2':
            print(con.mpg.tail())
        elif menu == '3':
            print(con.mpg.shape)
        elif menu == '4':
            con.mpg.info()
        elif menu == '5':
            print(con.mpg.describe())
        elif menu == '6':
            print(con.mpg.describe(include='all'))
        elif menu == '7':
            mpg = con.mpg_rename()
            print(mpg.head())
        elif menu == '8':
            con.mpg_test()
            print(con.mpg.head())
        elif menu == '9':
            print(con.mpg_value())
        elif menu == '10':
            con.mpg_plt()
        elif menu == '11':
            con.mpg_comparison()
        elif menu == '12':
            con.mpg_cty()
        elif menu == '13':
            con.mpg_hwy_evg()
        elif menu == '14':
            con.mpg_class_cty()
        elif menu == '15':
            con.mpg_audi_hwy()
        elif menu == '16':
            con.mpg_sort_hwy()
        else:
            print("다시 입력 해 주세요.")
