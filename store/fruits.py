from util.common import Common
class Fruits(object):
    def __init__(self, fruits, price):
        self.fruits = fruits
        self.price = price
    @staticmethod
    def get_menu():
        print("1.상품 등록\n2.상품 확인\n3.상품 삭제\n4.작업 종료")
        return int(input("작업 선택 : "))
    @staticmethod
    def get_fruits():
        return Fruits(input("과일명 : "), int(input("가격 : ")))
    def __str__(self):
        return f'{self.fruits} : {self.price}'
    @staticmethod
    def print_fruits(ls):
        print("과일 : 가격")
        [print(i) for i in ls]
    @staticmethod
    def del_fruits(ls, fruits):
        del ls[[i for i, j in enumerate(ls) if j.fruits == fruits][0]]
    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.menu()
            if menu == 0:
                print("작업을 종료합니다.")
                break
            elif menu == 1:
                ls.append(Fruits.get_fruits())
            elif menu == 2:
                Fruits.print_fruits(ls)
            elif menu == 3:
                Fruits.del_fruits(ls, input("삭제 할 과일 : "))
            else:
                print("다시 입력해 주세요.")
Fruits.main()