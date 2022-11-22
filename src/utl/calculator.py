from src.cmm.service.common import Common


class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    @staticmethod
    def get_data():
        return Calculator(int(input("첫번째 숫자 : ")), input("연산자 : "), int(input("두번재 숫자 : ")))

    def get_result(self):
        op = self.op
        num1 = self.num1
        num2 = self.num2
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        else:
            result = "잘못된 연산자 입니다."
        return result

    def __str__(self):
        return f'{self.num1} {self.op} {self.num2} = {self.get_result()}'

    @staticmethod
    def print_info(ls):
        [print(i) for i in ls]

    @staticmethod
    def del_calculator(ls, num1):
        del ls[[i for i, j in enumerate(ls) if j.num1 == num1][0]]

    @staticmethod
    def main():
        ls = []
        while True:
            menus = ['종료', '입력', '출력', '삭제']
            menu = Common.menu(menus)
            if menu == '0':
                print("종료")
                break
            elif menu == '1':
                print("입력")
                ls.append(Calculator.get_data())
            elif menu == '2':
                print("출력")
                Calculator.print_info(ls)
            elif menu == '3':
                print("삭제")
                Calculator.del_calculator(ls, int(input("첫번째 숫자 : ")))


if __name__ == '__main__':
    Calculator.main()
