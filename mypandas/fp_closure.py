from dataclasses import dataclass

menus = ['종료', 'global', 'nonlocal', 'closure', 'closure_lambda']


@dataclass
class OOP:
    x = 30

    def foo(self):
        x = self.x
        print("OOP 출력: " + str(x))


x = 110


def foo():
    global x
    x = x + 20
    print("FP 출력: " + str(x))


def A():
    x = 10
    y = 100

    def B():
        x = 20

        def C():
            global x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)

        C()

    B()


def calc():
    a = 3
    b = 5
    total = 0

    def mul_add(x):
        nonlocal total
        total = total + (a * x + b)
        print(total)

    def mul_add2(x):
        nonlocal total
        total = total + (a * x - b)
        return print(total)

    return {'mul_add': mul_add, 'mul_add2': mul_add2}


def clac_lambda():
    a = 3
    b = 5
    return lambda x: a * x + b


if __name__ == '__main__':
    while True:
        [print(f'{i}. {j}') for i, j in enumerate(menus)]
        menu = input('메뉴 : ')
        if menu == '0':
            break
        elif menu == '1':
            f = OOP()
            f.foo()
            foo()
            print("전역출력: " + str(x))
        elif menu == '2':
            A()
        elif menu == '3':
            c = calc()
            c['mul_add'](0), c['mul_add'](1),\
            c['mul_add2'](0), c['mul_add2'](1)
        elif menu == '4':
            c = clac_lambda()
            print(c(1), c(2), c(3), c(4), c(5))
