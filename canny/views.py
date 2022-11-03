import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import canny.services as model
from util.dataset import Dataset as ds


class MenuController(object):

    @staticmethod
    def Menu_0(*params):
        print(params[0])

    @staticmethod
    def Menu_1(*params):
        print(params[0])
        img = model.ExecuteLambda('IMG_READ_PLT', params[1])
        print(f'cv2 버전 {cv.__version__}')
        print(f'Shape is {img.shape}')
        plt.subplot(111), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_2(*params):
        print(params[0])
        arr = model.ImageToNumberArray(params[1])
        # 람다식 내부에서 GRAYSCALE 변환 공식 사용함
        img = model.ExecuteLambda('GRAY_SCALE', arr)
        plt.imshow(model.ExecuteLambda('FROM_ARRAY', img))
        plt.show()

    @staticmethod
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

    @staticmethod
    def Menu_4(*params):
        print(params[0])
        img = model.ImageToNumberArray(params[1])
        edges = cv.Canny(img, 190, 200)
        dst = model.Hough(edges)

        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_5(*params):
        print(params[0])
        haar = cv.CascadeClassifier(f'{ds().context}{params[1]}')
        girl = params[2]
        img = model.ExecuteLambda('IMG_READ_PLT', girl)
        gray = model.ExecuteLambda('GRAY_SCALE', img)
        edges = cv.Canny(img, 50, 51)
        hough = model.Hough(edges)
        model.HaarLine(haar, img)

        plt.subplot(151), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(152), plt.imshow(gray, cmap='gray')
        plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(153), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(154), plt.imshow(hough, cmap='gray')
        plt.title('Hough Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(155), plt.imshow(img, cmap='gray')
        plt.title('Haar Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_6(*params):
        pass



