import cv2
from matplotlib import pyplot as plt

from lena.models import LennaModel, CannyModel


class LennaController(object):

    def __init__(self):
        pass

    def __str__(self):
        return

    def preprocess(self):
        pass

    @staticmethod
    def modeling(fname):
        a = LennaModel().new_model(fname)
        print(f'cv2 버전 {cv2.__version__}')
        print(f'Shape is {a.shape}')
        cv2.imshow('A', a)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def Canny_modeling(fname):
        img = CannyModel().get(fname)
        print(f'cv2 버전 {cv2.__version__}')
        print(f'Shape is {img.shape}')
        edges = cv2.Canny(img, 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([170]), plt.yticks([200])
        plt.show()

    def learning(self):
        pass

    def submit(self):
        pass


if __name__ == '__main__':
    print(LennaController().modeling('Lenna.png'))
