class Contacts(object):
    def __init__(self, name, num, mail, add):
        self.name = name
        self.num = num
        self.mail = mail
        self.add = add
    @staticmethod
    def print_menu():
        print("1.입력\n2.출력\n3.삭제\n4.종료")
        return int(input("메뉴 선택 : "))
    @staticmethod
    def get_data():
        return Contacts(input("이름 : "), input("번호 : "), input("이메일 : "), input("주소 : "))
    def get_info(self):
        print("이름 전화번호 이메일 주소")
        return f'{self.name} {self.num} {self.mail} {self.add}'
    @staticmethod
    def print_info(ls):
        for i in ls:
            print(i.get_info())
    @staticmethod
    def del_contacts(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]
    @staticmethod
    def main():
        ls = []
        while True:
            menu = Contacts.print_menu()
            if menu == 1:
                print("입력")
                con = Contacts.get_data()
                ls.append(con)
            elif menu == 2:
                print("출력")
                Contacts.print_info(ls)
            elif menu == 3:
                print("삭제")
                Contacts.del_contacts(ls, input("이름 : "))
            elif menu == 4:
                print("종료")
                break
Contacts.main()