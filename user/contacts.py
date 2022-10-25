class Contacts(object):
    def __init__(self, name, num, mail, add):
        self.name = name
        self.num = num
        self.mail = mail
        self.add = add

    @staticmethod
    def get_data():
        return Contacts(input("이름 : "), input("번호 : "), input("이메일 : "), input("주소 : "))

    def __str__(self):
        return f'{self.name} {self.num} {self.mail} {self.add}'

    @staticmethod
    def print_info(ls):
        [print(i) for i in ls]

    @staticmethod
    def del_contacts(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]
