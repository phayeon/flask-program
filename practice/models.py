import pandas as pd
import numpy as np

from util.dataset import Dataset


class TitanicModels(object):
    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        return self.new_model(self.dataset.fname())

    def process(self) -> object:
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
    def sex_Nominal(this) -> object:
        for i in [this.train, this.test]:
            i['Sex'] = i['Sex'].map({'male': 0, 'female': 1})
        return this

    @staticmethod
    def age_Ordinary(this) -> object:
        for i in [this.train, this.test]:
            i['Age'] = i['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 68, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5,
                       'Adult': 6, 'Senior': 7}
        for i in [this.train, this.test]:
            i['Age'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['Age'] = i['Age'].map(age_mapping)
        return this

    @staticmethod
    def fare_Ordinary(this) -> object:
        for i in [this.train, this.test]:
            i['Fare'] = pd.qcut(['Fare'], 4, ['0', '1', '2', '3'])
            return this

    @staticmethod
    def embarked_Nominal(this) -> object:
        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.train.fillna({'Embarked': 'S'})
        for i in [this.train, this.test]:
            i['Embarked'] = i['Embarked'].map({'S': 1, 'C':2, 'Q':3})
        return this
