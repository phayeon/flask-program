from practice import TitanicModels
from util.dataset import Dataset

class TitanicController(object):

    dataset = Dataset()
    model = TitanicModels()

    def __init__(self):
        pass

    def __str__(self):
        pass

    def preprocess(self, train, test) -> object:
        this = self.dataset
        model = self.model
        this.train = model.new_model(train)
        this.test = model.new_model(test)
        this.id = this.test['PassengerId']
        this = model.sex_Nominal(this)
        this = model.age_Ordinary(this)
        this = model.fare_Ordinary(this)
        this = model.embarked_Nominal(this)
        return this

    def modeling(self, train, test) -> object:
        model = self.model
        this = self.preprocess(train, test)
        this.label = model.creat_label(this)
        this.train = model.creat_train(this)
        return this

    def learning(self) -> object:
        pass

    def submit(self) -> object:
        pass