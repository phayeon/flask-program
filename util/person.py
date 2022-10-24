class Person(object):
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg

    @staticmethod
    def print_menu():
        print("1.입력\n2.출력\n3.삭제\n4.종료")
        return int(input("메뉴 선택 : "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Person.print_menu()
            if menu == 1:
                print("입력")
                data = Person.get_data()
                ls.append(data)
            elif menu == 2:
                print("출력")
                Person.print_info(ls)
            elif menu == 3:
                print("삭제")
                Person.del_bmi(ls, input("이름 : "))
            elif menu == 4:
                print("종료")
                break
Person.main()