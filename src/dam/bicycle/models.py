import pandas as pd

from src.cmm.service.dataset import Dataset


class BicycleModel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        a = self.new_model('train.csv')
        return f" Train Type : {type(a)}\n" \
               f" Train columns : {a.columns}\n" \
               f" Train head : {a.head()}\n" \
               f" Train null의 개수 : {a.isnull().sum()}"

    def process(self):
        pass

    def new_model(self, fname):
        this = self.dataset
        this.context = '../../../static/data/dam/bicycle/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    def creat_train(self):
        pass

    def creat_lable(self):
        pass
