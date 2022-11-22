from dataclasses import dataclass
import pandas as pd


@dataclass
class Scrap:
    html = ''
    parser = ''
    domain = ''
    query_string = ''
    headers = {}
    tag_name = ''
    fname = ''
    class_names = []
    artists = []
    titles = []
    diction = {}
    df = None

    def dict_to_dataframe(self):
        print(len(self.diction))
        self.df = pd.DataFrame.from_dict(self.diction, orient='index')

    def dataframe_to_csv(self):
        path = '../../../../static/save/cop/scp/service/result.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)
