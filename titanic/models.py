import pandas as pd
from util.dataset import Dataset


# ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
# Age            177
# Cabin          687
# Embarked         2

class TitanicModel(object):
    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        a = self.new_model(self.dataset.fname())
        '''
        b = 'train.csv'
        a = self.new_model(b)
        '''
        return f' Train Type : {type(a)}\n' \
               f' Train columns : {a.columns}\n' \
               f' Train head : {a.head()}\n' \
               f' Train null의 개수 : {a.isnull().sum()}\n'

    def preprocess(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def creat_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def creat_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_features(this, *feature):
        for i in feature:
            this.train = this.train.drop(i, axis=1)
            this.test = this.test.drop(i, axis=1)
        return this