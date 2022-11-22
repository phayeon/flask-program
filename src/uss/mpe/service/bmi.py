class Bmi(object):
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg

    @staticmethod
    def get_data():
        return Bmi(input("이름 : "), int(input("키(cm) : ")), int(input("체중(kg) : ")))

    def get_bmi(self):
        return self.kg / (self.cm / 100) ** 2

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

    def __str__(self):
        return f'{self.name} {self.cm} {self.kg} {self.get_biman()}'

    @staticmethod
    def print_info(ls):
        print("이름 키(cm) 몸무게(kg) 비만도")
        [print(i) for i in ls]

    @staticmethod
    def del_bmi(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]
