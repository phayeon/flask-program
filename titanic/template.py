from titanic.models import TitanicModel
from util.dataset import Dataset
import matplotlib.pyplot as plt
import seaborn as sns
# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:\Windows\Fonts\malgunbd.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


class Plot(object):
    dataset = Dataset()
    model = TitanicModel()

    def __init__(self, fname):
        self.entry = self.model.new_model(fname)

    def __str__(self):
        pass


    def draw_survived(self):
        this = self.entry
        f, ax = plt.subplots(1, 2, figsize=(18, 8)) # 한 화면에 두개의 그래프를 그릴 때는 복수형 plots 를 사용한다.
        this['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0.사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 vs 1.생존자')
        sns.countplot(x='Survived', data=this, ax=ax[1])
        plt.show()

    def draw_pclass(self):
        this = self.entry
        this["Survived"] = this["Survived"].replace(0, "사망자").replace(1, "생존자")
        this["Pclass"] = this["Pclass"].replace(1, "1등석").replace(2, "2등석").replace(3, "3등석")
        sns.countplot(data=this, x=this["Pclass"], hue=this["Survived"])
        plt.show()

    def draw_sex(self):
        this = self.entry
        f, ax = plt.subplots(1, 2, figsize=(18, 8))  # 한 화면에 두개의 그래프를 그릴 때는 복수형 plots 를 사용한다.
        this['Survived'][this['Sex'] == 'male'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        this['Survived'][this['Sex'] == 'female'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
        ax[0].set_title('남성의 생존비율 [0.사망자 vs 1.생존자]')
        ax[1].set_title('여성의 생존비율 [0.사망자 vs 1.생존자]')
        plt.show()