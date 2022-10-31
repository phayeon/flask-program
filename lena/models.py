import cv2

from util.dataset import Dataset


class LennaModel(object):
    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        return

    def new_model(self, fname):
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return cv2.imread(this.context + this.fname, cv2.IMREAD_COLOR)


if __name__ == '__main__':
    pass