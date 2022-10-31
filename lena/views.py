import cv2

from lena.models import LennaModel


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

    def learning(self):
        pass

    def submit(self):
        pass


if __name__ == '__main__':
    print(LennaController().modeling('Lenna.png'))
