class Random(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def print_menu():
        print("1.입력\n2.출력\n3.삭제\n4.종료")
        return int(input("메뉴 선택 : "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Random.print_menu()
            if menu == 1:
                print("입력")
                data = Random.get_data()
                ls.append(data)
            elif menu == 2:
                print("출력")
                Random.print_info(ls)
            elif menu == 3:
                print("삭제")
                Random.del_bmi(ls, input("이름 : "))
            elif menu == 4:
                print("종료")
                break
Random.main()