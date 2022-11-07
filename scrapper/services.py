from urllib.request import urlopen

from bs4 import BeautifulSoup

from scrapper import MusicRanking


def BugsMusic(arg):
    arg = MusicRanking()
    soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), 'lxml')
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    # 디버깅
    [print(f'{i}위. {j.find("a").text} / {k.find("a").text}')
     for i, j, k in zip(range(1, len(titles)), titles, artists)]
    # dict 로 변환
    for i in range(0, len(titles)):
        arg.dic[arg.titles[i]] = arg.artists[i]
    # title → key, artists → value △ 한 가수가 2곡 낸 경우 못 걸러냄
    # csv 파일로 저장
    arg.dict_to_dataframe()
    arg.dataframe_to_csv()
