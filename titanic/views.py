from titanic.models import TitanicModel
from util.dataset import Dataset


class TitanicController(object):

    def __init__(self):
        pass

    def __str__(self):
        return f''

    dataset = Dataset()
    model = TitanicModel()

    def preprocess(self, train, test) -> object:
        model = self.model
        this = self.dataset
        this.train = model.new_model(train)
        this.test = model.new_model(test)
        this.id = this.test['PassengerId']
        this = model.sex_Nominal(this)
        this = model.age_Ordinal(this)
        this = model.fare_Ordinal(this)
        this = model.embarked_Nominal(this)
        this = model.title_nominal(this)
        this = model.drop_features(this, 'PassengerId', 'Name', 'Sex', 'Age', 'SibSp', 'Parch',
       'Ticket', 'Fare', 'Cabin')
        return this

    def modeling(self, train, test) -> object:
        model = self.model
        this = self.preprocess(train, test)
        this.label = model.creat_label(this)
        this.train = model.creat_train(this)
        return this

    def learning(self):
        pass

    def submit(self):
        pass


if __name__ == '__main__':
    t = TitanicController()
    this = Dataset()
    this = t.modeling('train.csv', 'test.csv')
    print(this.train.columns)
    print(this.train.head())
