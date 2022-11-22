class Grade(object):
    def __init__(self, name, kor, eng):
        self.name = name
        self.kor = kor
        self.eng = eng

    @staticmethod
    def get_data():
        return Grade(input("이름 : "), int(input("국어 : ")), int(input("수학 : ")))

    def get_tot(self):
        return self.kor + self.eng

    def get_avg(self):
        return self.get_tot() / 2

    def get_gra(self):
        avg = self.get_avg()
        if avg >= 90:
            gra = "A"
        elif avg >= 80:
            gra = "B"
        else:
            gra = "F"
        return gra

    def __str__(self):
        return f'{self.name} {self.kor} {self.eng} {self.get_tot()} {self.get_avg()} {self.get_gra()}'

    @staticmethod
    def print_grade(ls):
        [print(i) for i in ls]

    @staticmethod
    def del_grade(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]
