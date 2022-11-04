from mosaic.views import MenuController
from util.common import Common

'''

이미지 읽기의 flag는 3가지가 있습니다.

cv2.IMREAD_COLOR : 이미지 파일을 Color로 읽어들입니다. 투명한 부분은 무시되며, Default값입니다.
cv2.IMREAD_GRAYSCALE : 이미지를 Grayscale로 읽어 들입니다. 실제 이미지 처리시 중간단계로 많이 사용합니다.
cv2.IMREAD_UNCHANGED : 이미지파일을 alpha channel까지 포함하여 읽어 들입니다

3개의 flag대신에 1, 0, -1을 사용해도 됩니다.

Shape is (220, 220, 3)
Y축(앞) : 220
X축(뒤) : 220
3은 RGB 로 되어있다.

cv2.waitKey(0) : keyboard입력을 대기하는 함수로 0이면 key입력까지 무한대기이며, 특정 시간동안 대기하려면 milisecond값을 넣어주면 됩니다.
cv2.destroyAllWindows() : 화면에 나타난 윈도우를 종료합니다. 일반적으로 위 3개는 같이 사용됩니다.

'''

LENNA = "Lenna.png"
SOCCER = "https://docs.opencv.org/4.x/roi.jpg"
BUILDING = "https://www.charlezz.com/wordpress/wp-content/uploads/2021/06/www.charlezz.com-opencv-building.jpg"
GIRL = "girl.jpg"
GIRL_LICLINED = "girl_licliend.png"
GIRL_SIDE_FACE = "girl_side_face.jpg"
GIRL_WITH_MOM = "girl_with_mom.jpg"
FACE_TARGET = ""
FACE_OBJECT = ""
CAT = "cat.jpg"


if __name__ == '__main__':
    api = MenuController
    while True:
        menus = ["종료", "원본보기", "그레이스케일", "엣지검출", "직선검출", "모자이크", "소녀 모자이크", "모녀 모자이크"]
        menu = Common.menu(menus)
        if menu == "0":
            api.Menu_0(menus[0])
            break
        elif menu == "1":
            api.Menu_1(menus[1], LENNA)
        elif menu == "2":
            api.Menu_2(menus[2], SOCCER)
        elif menu == "3":
            api.Menu_3(menus[3], SOCCER)
        elif menu == "4":
            api.Menu_4(menus[4], BUILDING)
        elif menu == "5":
            api.Menu_5(menus[5], CAT)
        elif menu == "6":
            api.Menu_6(menus[6], GIRL)
        elif menu == "7":
            api.Menu_7(menus[7], GIRL_WITH_MOM)
        else:
            print("다시 입력 해 주세요.")
