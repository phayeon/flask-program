from dataclasses import dataclass
import urllib
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

"""
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
"""


@dataclass
class MusicRanking(object):

    html: str
    parser: str
    domain: str
    query_string: str
    headers: dict
    tag_name: str
    fname: str
    class_names: list
    artists: list
    titles: list
    dic: dict
    df: None

    @property
    def html(self) -> str: return self._html

    @html.setter
    def html(self, html): self._html = html

    @property
    def ranking(self) -> str: return self._ranking

    @ranking.setter
    def ranking(self, ranking): self._ranking = ranking

    @property
    def parser(self) -> str: return self._parser

    @parser.setter
    def parser(self, parser): self._parser = parser

# 강사님 깃허브 보기

    @property
    def domain(self) -> str: return self._domain

    @domain.setter
    def domain(self, domain): self._domain = domain

    @property
    def query_string(self) -> str: return self._query_string

    @query_string.setter
    def query_string(self, query_string): self._query_string = query_string

    @property
    def headers(self) -> str: return self._headers

    @headers.setter
    def headers(self, headers): self._headers = headers

    @property
    def tag_name(self) -> str: return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name): self._tag_name = tag_name

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def class_names(self) -> str: return self._class_names

    @class_names.setter
    def class_names(self, class_names): self._class_names = class_names

    @property
    def artists(self) -> str: return self._artists

    @artists.setter
    def artists(self, artists): self._artists = artists

    @property
    def titles(self) -> str: return self._titles

    @titles.setter
    def titles(self, titles): self._titles = titles

    @property
    def dic(self) -> str: return self._dic

    @dic.setter
    def dic(self, dic): self._dic = dic

    @property
    def df(self) -> str: return self._df

    @df.setter
    def df(self, df): self._df = df

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dic, orient='index')

    def dataframe_to_csv(self):
        path = CTX+self.fname+'.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')


'''
class BugsMusic:
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        # print(soup.prettify(encoding="UTF8")) → 느려짐
        _ = 0
        title = {"class": "title"}
        artist = {"class": "artist"}
        album = {"class": "album"}
        # class → Hash
        titles = soup.find_all(name="p", attrs=title)
        artists = soup.find_all(name="p", attrs=artist)

        [print(f'{i}위. {j.find("a").text} / {k.find("a").text}')
         for i, j, k in zip(range(1, len(titles)), titles, artists)]


class MelonMusic(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrap(self):
        urlheader = urllib.request.Request(self.url, headers={'User-Agent': "Mozilla/5.0"})
        htmlurl = urllib.request.urlopen(urlheader).read()
        soup = BeautifulSoup(htmlurl, "lxml")
        _ = 0
        title = {"class": "ellipsis rank01"}
        artist = {"class": "ellipsis rank02"}
        rank = {"class": "rank"}
        # class → Hash
        titles = soup.find_all(name="div", attrs=title)
        artists = soup.find_all(name="div", attrs=artist)
        ranks = soup.find_all(name="span", attrs=rank)

        [print(f'{i}위. {j.find("a").text} / {k.find("a").text}') for i, j, k in zip(range(1, len(titles)), titles, artists)]
'''
