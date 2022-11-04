import copy

import cv2 as cv
from matplotlib import pyplot as plt
import mosaic.services as model
from util.dataset import Dataset as ds
import util.lamdas as lam


class MenuController(object):

    @staticmethod
    def Menu_0(*params):
        print(params[0])

    @staticmethod
    def Menu_1(*params):
        print(params[0])
        img = lam.Mosaic('IMG_READ_PLT', params[1])
        print(f'cv2 버전 {cv.__version__}')
        print(f'Shape is {img.shape}')
        plt.subplot(111), plt.imshow(img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_2(*params):
        print(params[0])
        arr = model.ImageToNumberArray(params[1])
        # 람다식 내부에서 GRAYSCALE 변환 공식 사용함
        img = lam.Mosaic('GRAY_SCALE', arr)
        plt.imshow(lam.Mosaic('FROM_ARRAY', img))
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
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge'), plt.xticks([170]), plt.yticks([200])
        plt.show()

    @staticmethod
    def Menu_4(*params):
        print(params[0])
        img = model.ImageToNumberArray(params[1])
        dst = model.Hough(cv.Canny(img, 190, 200))

        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Hough'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_5(*params):
        print(params[0])
        plt_cat = lam.Mosaic('IMG_READ_PLT', params[1])
        mos = model.OneMosaic(plt_cat, (150, 150, 450, 450), 10)

        plt.subplot(121), plt.imshow(plt_cat, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(mos, cmap='gray')
        plt.title('Mosaic'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_6(*params):
        print(params[0])
        img = lam.Mosaic('IMG_READ_PLT', params[1])
        original = copy.deepcopy(img)

        gray = lam.Mosaic('GRAY_SCALE', img)
        edges = cv.Canny(img, 50, 51)
        hough = model.Hough(edges)
        mos = model.IMGMosaic(img, 10)
        model.HaarLine(img)

        cv.imwrite(f'{ds().context}girl-mosaic.png', cv.cvtColor(mos, cv.COLOR_BGR2RGB))

        plt.subplot(231), plt.imshow(original, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(232), plt.imshow(gray, cmap='gray')
        plt.title('Gray'), plt.xticks([]), plt.yticks([])
        plt.subplot(233), plt.imshow(edges, cmap='gray')
        plt.title('Edge'), plt.xticks([]), plt.yticks([])
        plt.subplot(234), plt.imshow(hough, cmap='gray')
        plt.title('Hough'), plt.xticks([]), plt.yticks([])
        plt.subplot(235), plt.imshow(mos, cmap='gray')
        plt.title('Mosaic'), plt.xticks([]), plt.yticks([])
        plt.subplot(236), plt.imshow(img, cmap='gray')
        plt.title('Haar'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def Menu_7(*params):
        print(params[0])
        img = lam.Mosaic('IMG_READ_PLT', params[1])
        mos = model.IMGMosaic(img, 10)

        cv.imwrite(f'{ds().context}family-mosaic.png', cv.cvtColor(mos, cv.COLOR_BGR2RGB))

        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Haar'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(mos, cmap='gray')
        plt.title('Mosaic'), plt.xticks([]), plt.yticks([])
        plt.show()
