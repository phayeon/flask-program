class Grade(object):
    def __init__(self, name, kor, eng):
        self.name = name
        self.kor = kor
        self.eng = eng

    @staticmethod
    def print_menu():
        print("1.입력\n2.출력\n3.삭제\n4.종료")
        return int(input("메뉴 선택 : "))

    @staticmethod
    def get_data():
        return Grade(input("이름 : "), int(input("국어 : ")), int(input("수학 : ")))
    def get_tot(self):
        return self.kor + self.eng
    def get_avg(self):
        return self.get_tot()/2
    def get_gra(self):
        avg = self.get_avg()
        if avg >= 90:
            gra = "A"
        elif avg >= 80:
            gra = "B"
        else:
            gra = "F"
        return gra
    def get_grade(self):
        print("이름 국어 영어 총점 평균 학점")
        return f'{self.name} {self.kor} {self.eng} {self.get_tot()} {self.get_avg()} {self.get_gra()}'
    @staticmethod
    def print_grade(ls):
        for i in ls:
            print(i.get_grade())
    @staticmethod
    def del_grade(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]
    @staticmethod
    def main():
        ls = []
        while True:
            menu = Grade.print_menu()
            if menu == 1:
                print("입력")
                data = Grade.get_data()
                ls.append(data)
            elif menu == 2:
                print("출력")
                Grade.print_grade(ls)
            elif menu == 3:
                print("삭제")
                Grade.del_grade(ls, input("이름 : "))
            elif menu == 4:
                print("종료")
                break


Grade.main()