import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup


def MelonMusic(*params):
    urlheader = urllib.request.Request(params[0].domain, headers={'User-Agent': "Mozilla/5.0"})
    htmlurl = urllib.request.urlopen(urlheader).read()
    soup = BeautifulSoup(htmlurl, "lxml")

    title = {"class": params[0].class_names[0]}
    artist = {"class": params[0].class_names[1]}
    titles = soup.find_all(name=params[0].tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=params[0].tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i}위 {j} : {k}")  # 디버깅
    for i, j, k in zip(range(1, len(titles)+1), titles, artists)]
    diction = {}  # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    params[0].diction = diction
    params[0].dict_to_dataframe()
    params[0].dataframe_to_csv()  # csv파일로 저장


def BugsMusic(*params):
    soup = BeautifulSoup(urlopen(params[0].domain + params[0].query_string), 'lxml')
    title = {"class": params[0].class_names[0]}
    artist = {"class": params[0].class_names[1]}
    titles = soup.find_all(name=params[0].tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=params[0].tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i}위 {j} : {k}")  # 디버깅
    for i, j, k in zip(range(1, len(titles)+1), titles, artists)]
    diction = {}  # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    params[0].diction = diction
    params[0].dict_to_dataframe()
    params[0].dataframe_to_csv()  # csv파일로 저장
