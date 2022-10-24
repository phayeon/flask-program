class Bmi(object):
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg

    @staticmethod
    def print_menu():
        print("1.입력\n2.출력\n3.삭제\n4.종료")
        return int(input("메뉴 선택 : "))

    @staticmethod
    def get_data():
        return Bmi(input("이름 : "), int(input("키(cm) : ")), int(input("체중(kg) : ")))
    def get_bmi(self):
        m = self.cm/100
        return self.kg / m ** 2
    def get_biman(self):
        cal = self.get_bmi()
        if cal >= 35:
            biman = "고도 비만"
        elif cal >= 30:
            biman = "중(重)도 비만 (2단계 비만)"
        elif cal >= 25:
            biman = "경도 비만 (1단계 비만)"
        elif cal >= 23:
            biman = "과체중"
        elif cal >= 18.5:
            biman = "정상"
        else:
            biman = "저체중"
        return biman
    def print_data(self):
        return f'{self.name} {self.cm} {self.kg} {self.get_biman()}'
    @staticmethod
    def print_info(ls):
        print("이름 키(cm) 몸무게(kg) 비만도")
        for i in ls:
            print(i.print_data())
    @staticmethod
    def del_bmi(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]
    @staticmethod
    def main():
        ls = []
        while True:
            menu = Bmi.print_menu()
            if menu == 1:
                print("입력")
                data = Bmi.get_data()
                ls.append(data)
            elif menu == 2:
                print("출력")
                Bmi.print_info(ls)
            elif menu == 3:
                print("삭제")
                Bmi.del_bmi(ls, input("이름 : "))
            elif menu == 4:
                print("종료")
                break
Bmi.main()