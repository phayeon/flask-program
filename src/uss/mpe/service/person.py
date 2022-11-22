class Person(object):
    def __init__(self, name, rrn, add):
        self.name = name
        self.rrn = rrn
        self.add = add

    @staticmethod
    def get_data():
        return Person(input("이름 : "), input("주민번호(앞 8자리):"), input("주소 : "))

    def get_seven(self):
        return int(self.rrn[7])

    def get_age(self):
        seven = self.get_seven()
        age = int(self.rrn[:2])
        if seven == 1 or seven == 2:
            result = 2022 - (1900 + age)
        else:
            result = 2022 - (2000 + age)
        return result

    def get_gender(self):
        if self.get_seven() % 2 == 1:
            gender = "남성"
        else:
            gender = "여성"
        return gender

    def get_info(self):
        return f'{self.name} {self.get_gender()} {self.get_age()} {self.add}'

    @staticmethod
    def print_info(ls):
        [print(i.get_info()) for i in ls]

    @staticmethod
    def del_person(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]
