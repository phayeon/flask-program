class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2
    @staticmethod
    def print_menu():
        print("1.입력\n2.출력\n3.삭제\n4.종료")
        return int(input("메뉴 선택 : "))
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
    def print_result(self):
        return f'{self.num1} {self.op} {self.num2} = {self.get_result()}'
    @staticmethod
    def print_info(ls):
        for i in ls:
            print(i.print_result())
    @staticmethod
    def del_calculator(ls, num1):
        for i, j in enumerate(ls):
            if j.num1 == num1:
                del ls[i]
    @staticmethod
    def main():
        ls = []
        while True:
            menu = Calculator.print_menu()
            if menu == 1:
                print("입력")
                cal = Calculator.get_data()
                ls.append(cal)
            elif menu == 2:
                print("출력")
                Calculator.print_info(ls)
            elif menu == 3:
                print("삭제")
                Calculator.del_calculator(ls, int(input("첫번째 숫자 : ")))
            elif menu == 4:
                print("종료")
                break
Calculator.main()