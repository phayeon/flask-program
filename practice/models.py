import pandas as pd
from util.dataset import Dataset


class TitanicModel(object):
    dateset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        a = self.new_model(self.dateset.fname())
        return f' Train Type : {type(a)}\n' \
               f' Train columns : {a.columns}\n' \
               f' Train head : {a.head()}\n' \
               f' Train null의 개수 : {a.isnull().sum()}\n'

    def preprocee(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dateset
        this.context = './data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    def creat_train(self):
        pass

    def creat_label(self):
        pass