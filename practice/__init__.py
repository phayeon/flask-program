from practice.models import TitanicModel
from practice.views import TitanicController
from util.common import Common
if __name__ == '__main__':

    api = TitanicController()

    while True:
        menu = Common.menu(['종료', '시각화', '모델링', '머신러닝', '배포'])
        if menu == "0":
            print("프로그램을 종료합니다.")
            break
        elif menu == "1":
            print("### 시각화 ###")
            a = TitanicModel()
            print(a.new_model('train.csv'))
        elif menu == "2":
            print("### 모델링 ###")
        elif menu == "3":
            print("### 머신러닝 ###")
        elif menu == "4":
            print("### 배포 ###")
        else:
            print("다시 입력 해 주세요.")