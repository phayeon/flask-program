import pandas as pd

MENUS = ["종료",
         "mpg 앞부분 확인",
         "mpg 뒷부분 확인",
         "행,열 출력",
         "데이터 속성 확인",
         "요약 통계량 출력",
         "문자 변수 요약 통계량 함께 출력"]
mpg = pd.read_csv('./data/mpg.csv')


def menulist():
    [print(f'{i}. {j}') for i, j in enumerate(MENUS)]
    return input("메뉴 선택 : ")


def menuprint(num):
    [print(j) for i, j in enumerate(MENUS) if str(i) == num]


if __name__ == '__main__':
    while True:
        menu = menulist()
        menuprint(menu)
        if menu == '0':
            break
        elif menu == '1':
            print(mpg.head())
        elif menu == '2':
            print(mpg.tail())
        elif menu == '3':
            print(mpg.shape)
        elif menu == '4':
            mpg.info()
        elif menu == '5':
            print(mpg.describe())
        elif menu == '6':
            print(mpg.describe(include='all'))
        else:
            print("다시 입력 해 주세요.")
