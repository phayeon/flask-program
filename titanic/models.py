import pandas as pd
from util.dataset import Dataset

'''
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
시각화를 통해 얻은 상관관계 변수(variable = featuer = column)는
기준점 Survived
Pclass
Sex
Age
Fare
Embarked 이다.
### null 값 ###
Age            177
Cabin          687
Embarked         2
'''


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

    '''
    def mining(self): # 작업 순서 개념만 확인
        pass
    '''

    def preprocess(self):
        pass

    '''
    def postprocess(self) # 작업 순서 개념만 확인
        pass
    '''

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
    def drop_features(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop(i, axis=1)
            this.test = this.test.drop(i, axis=1)
        return this

    '''
    @staticmethod
    def pclass_Ordinal(this) -> object: # 1등칸, 2등칸, 3등칸
        train = this.train
        print(train['PassengerId'])
        return this
        
        편집 불필요 → 삭제 / 데이터 자체가 이미 오디널.
    '''

    @staticmethod
    def sex_Nominal(this) -> object:  # female → 1, male → 0
        # gender_mapping = {'male': 0, 'female': 1}
        for i in [this.train, this.test]:
            i['Gender'] = i['Sex'].map({'male': 0, 'female': 1})  # Gender 칼럼에 생성 → 0, 1 로 대체
        return this

    @staticmethod
    def age_Ordinal(this) -> object:  # 연령대 10대, 20대 등
        return this

    @staticmethod
    def fare_Ordinal(this) -> object:  # 가격 싼표, 일반표, 비싼표
        for i in [this.train, this.test]:
            i['FareBand'] = pd.qcut(i['Fare'], 4, ["0", "1", "2", "3"])
        return this

    @staticmethod
    def embarked_Nominal(this) -> object:  # 승선 항구 S, C, Q
        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.train.fillna({'Embarked': 'S'})  # fillna → null 값을 임시 값을 S로 채운다.(수가 적을 때 사용 가능)
        for i in [this.train, this.test]:
            i['Embarked'] = i['Embarked'].map({"S": 1, "C": 2, "Q": 3})
        return this


if __name__ == '__main__':
    t = TitanicModel()
    this = Dataset()
    this.train = t.new_model('train.csv')
    this.test = t.new_model('test.csv')
    this = TitanicModel.embarked_Nominal(this)
    print(this.train.columns)
    print(this.train.head(3))   # 위부터 3줄
    print(this.train.tail(3))   # 아래부터 3줄
