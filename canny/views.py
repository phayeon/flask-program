import numpy as np
from PIL import Image
import cv2 as cv
from matplotlib import pyplot as plt
import canny.services as model


class MenuController(object):

    @staticmethod
    def Menu_0(*params):
        print(params[0])

    @staticmethod
    def Menu_1(*params):
        print(params[0])
        img = model.ImageRead(params[1])
        print(f'cv2 버전 {cv.__version__}')
        print(f'Shape is {img.shape}')
        cv.imshow('Original', img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def Menu_2(*params):
        print(params[0])
        arr = model.ImageToNumberArray(params[1])
        # 람다식 내부에서 GRAYSCALE 변환 공식 사용함
        img = (lambda x: x[:, :, 0] * 0.114 + x[:, :, 1] * 0.587 + x[:, :, 2] * 0.229)(arr)
        plt.imshow((lambda x: Image.fromarray(x))(img))
        plt.show()

    def Menu_3(*params):
        print(params[0])
        ### 디스크에서 읽는 경우 ###
        # img = cv.imread('./data/roi.jpg', 0)
        # img = cv.imread(img, 0)
        ### 메모리에서 읽는 경우 ###
        img = model.ImageToNumberArray(params[1])
        print(f'img type : {type(img)}')
        # img = GaussianBlur(img, 1, 1) cv.Canny() 를 사용하지 않는 경우 필요
        # img = Canny(img, 50, 150) cv.Canny() 를 사용하지 않는 경우 필요
        edges = cv.Canny(img, 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([170]), plt.yticks([200])
        plt.show()

    def Menu_4(*params):
        print(params[0])
        img = model.ImageToNumberArray(params[1])
        edges = cv.Canny(img, 100, 200)
        lines = cv.HoughLinesP(edges, 0.8, np.pi / 150., 90, minLineLength=10, maxLineGap=100)
        dst = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)

        for i in lines:
            cv.line(dst, (int(i[0][0]), int(i[0][1])), (int(i[0][2]), int(i[0][3])), (0, 255, 0), 2)

        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()
