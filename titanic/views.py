from titanic.models import TitanicModel
from util.dataset import Dataset


class TitanicController(object):

    def __init__(self):
        pass

    def __str__(self):
        return f''

    dataset = Dataset()
    model = TitanicModel()

    def preprocess(self, train, test) -> object: # 전처리
        model = self.model
        this = self.dataset
        this.train = model.new.model(train)
        this.test = model.new_model(test)
        this.id = this.test['PassengerId']
        # columns 편집과정

        return this

    def modeling(self, train, test) -> object:   # 모델생성
        model = self.model
        this = self.preprocess(train, test)
        this.label = model.creat_label(this)
        this.train = model.creat_train(this)
        self.preprocess()

    def learning(self):             # 기계 학습
        pass

    def submit(self):               # 배포
        pass

