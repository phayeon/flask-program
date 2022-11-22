import numpy as np
import pandas as pd
from string import ascii_lowercase
from src.cmm.service.common import Common


class Fruits(object):
    def __init__(self, fruits, price):
        self.fruits = fruits
        self.price = price

    @staticmethod
    def get_fruits():
        return Fruits(input("과일명 : "), int(input("가격 : ")))

    def __str__(self):
        return f'{self.fruits} : {self.price}'

    @staticmethod
    def print_fruits(ls):
        ls0 = ['제품', '가격', '판매량']
        ls1 = ['사과', '딸기', '바나나']
        ls2 = [1000, 5000, 1000]
        ls3 = [30, 40, 50]
        ls = [ls1, ls2, ls3]
        dc = pd.DataFrame(
            {j: ls[i] for i, j in enumerate(ls0)})
        '''
        for i, j in enumerate(ls0):
            dc[j] = ls[i]
        print(pd.DataFrame.from_dict(dc))
        '''
        print(dc)
        print('가격 평균 : ' + str(int(dc['가격'].mean())))
        print('판매량 평균 : ' + str(int(dc['판매량'].mean())))

        '''print("과일 : 가격")
        [print(i) for i in ls]'''

    @staticmethod
    def del_fruits(ls, fruits):
        del ls[[i for i, j in enumerate(ls) if j.fruits == fruits][0]]

    @staticmethod
    def my_list(a, b):
        return list(range(a, b))

    @staticmethod
    def num2d():
        df = pd.DataFrame(np.array([(Fruits.my_list(1, 11)),
                                    Fruits.my_list(11, 21),
                                    Fruits.my_list(21, 31)]),
                          columns=[list(ascii_lowercase)[0:10]])
        print(df.head())

    @staticmethod
    def main():
        ls = []
        while True:
            manus = ['종료', '추가', '확인', '삭제', '숫자2D']
            menu = Common.menu(manus)
            if menu == '0':
                print("작업을 종료합니다.")
                break
            elif menu == '1':
                ls.append(Fruits.get_fruits())
            elif menu == '2':
                Fruits.print_fruits(ls)
            elif menu == '3':
                Fruits.del_fruits(ls, input("삭제 할 과일 : "))
            elif menu == '4':
                Fruits.num2d()
            else:
                print("다시 입력해 주세요.")


if __name__ == '__main__':
    Fruits.main()
