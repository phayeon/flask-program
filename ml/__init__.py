from ml.views import StrokeController
from util.common import Common

if __name__ == '__main__':

    api = StrokeController()

    STROKE_MENUS = ["종료",  # 0
                    "데이터 구하기",  # 1
                    "타깃 변수 설정",  # 2
                    "데이터 처리",  # 3
                    "시각화",  # 4
                    "모델링",  # 5
                    "학습",  # 6
                    "예측"]  # 7

    stroke_meta = {'id': '아이디', 'gender': '성별', 'age': '나이', 'hypertension': '고혈압', 'heart_disease': '심장병',
                   'ever_married': '기혼 여부', 'work_type': '직종', 'Residence_type': '거주 형태', 'avg_glucose_level': '평균 혈당',
                   'bmi': '비만도', 'smoking_status': '흡연 여부', 'stroke': '뇌졸중'}

    while True:
        menu = Common.menu(STROKE_MENUS)
        if menu == "0":
            break
        elif menu == "1":
            print(" ### 문제 제기 ###")
            api.menu_1()

        elif menu == "2":
            print(" ### 데이터 구하기 ###")
            api.menu_2()

        elif menu == "3":
            print(" ### 타깃 변수 설정 ###")
            api.menu_3()

        elif menu == "4":
            print(" ### 데이터 처리 ###")
            api.menu_4()

        elif menu == "5":
            print(" ### 시각화 ###")
            api.menu_5()

        else:
            print("다시 입력 해 주세요.")
