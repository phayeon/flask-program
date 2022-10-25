from util.common import Common


class RandomList(object):
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count

    @staticmethod
    def get_menu():
        print("1.랜덤 출력\n2.숫자 확인\n3.작업 종료")
        return int(input("작업 선택 : "))

    @staticmethod
    def get_num():
        return RandomList(int(input("시작 숫자 : ")), int(input("종료 숫자 : ")), int(input("뽑을 개수 : ")))

    def __str__(self):
        return f'시작 숫자 : {self.start}, 종료 숫자 : {self.end}, 랜덤 숫자 : '

    @staticmethod
    def print_num(ls):
        [print(i) for i in ls]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.get_menu()
            if menu == 1:
                print("출력 범위를 입력해 주세요.")
                ls.append(RandomList.get_num())
            elif menu == 2:
                print("이전 출력 리스트 입니다.")
                RandomList.print_num(ls)
            elif menu == 3:
                print("프로그램을 종료합니다.")
                break
            else:
                print("다시 입력 해 주세요.")


RandomList.main()
