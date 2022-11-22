class Member(object):
    def __init__(self, id, pw, name):
        self.id = id
        self.pw = pw
        self.name = name

    @staticmethod
    def print_menu():
        print("1.입력\n2.출력\n3.삭제\n4.종료")
        return int(input("메뉴 선택 : "))

    @staticmethod
    def get_data():
        return Member(input("아이디 : "), input("비밀번호 : "), input("이름 : "))

    def get_member(self):
        return f'{self.id} {self.pw} {self.name}'

    @staticmethod
    def print_member(ls):
        print("아이디 비밀번호 이름")
        for i in ls:
            print(i.get_member())

    @staticmethod
    def del_member(ls, id):
        del ls[[i for i, j in enumerate(ls) if j.id == id][0]]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Member.print_menu()
            if menu == 1:
                print("가입")
                data = Member.get_data()
                ls.append(data)
            elif menu == 2:
                print("확인")
                Member.print_member(ls)
            elif menu == 3:
                print("탈퇴")
                Member.del_member(ls, input("아이디 : "))
            elif menu == 4:
                print("종료")
                break


Member.main()
