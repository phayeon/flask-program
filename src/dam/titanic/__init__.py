from src.dam.titanic.models import TitanicModel
from src.dam.titanic.template import Plot
from src.dam.titanic.views import TitanicController
from src.cmm.service.common import Common

if __name__ == '__main__':

    api = TitanicController()

    while True:
        menu = Common.menu(["종료", "시각화", "모델링", "머신러닝", "배포"])
        if menu == "0":
            break
        elif menu == "1":
            print(" ### 시각화 ###")
            a = TitanicModel()
            print(a.new_model('train.csv'))
            plot = Plot('train.csv')
            plot.draw_survived()
            plot.draw_sex()
            plot.draw_pclass()
            plot.draw_embarked()

        elif menu == "2":
            print(" ### 모델링 ###")
            df = api.modeling('train.csv', 'test.csv')

        elif menu == "3":
            print(" ### 머신러닝 ###")
            df = api.learning('train.csv', 'test.csv')
            # 랜덤 포레스트 분류기 : 81.94 %
            # 결정 트리 분류기 : 81.82 %
            # 로지스틱 회귀 : ? %
            # 서포트 벡터 머신 : ? %

        elif menu == "4":
            print(" ### 배포 ###")
            df = api.submit()

        else:
            print("해당 메뉴 없음")

