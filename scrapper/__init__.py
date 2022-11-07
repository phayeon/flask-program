from scrapper.domains import MusicRanking
from util.common import Common
from scrapper.views import ScrapController

if __name__ == '__main__':
    api = ScrapController
    while True:
        menus = ["종료", "Bugs", "Melon", "삭제"]
        menu = Common.menu(menus)
        m = MusicRanking()
        if menu == "0":
            api.menu_0(menus[0])
            break
        elif menu == "1":
            m.domain = 'https://music.bugs.co.kr/chart/track/day/total?chartdate='
            m.query_string = '20221105'
            m.parser = 'lxml'
            m.class_names = ["title", "artist"]
            m.tag_name = 'p'
            api.menu_1(m)
        elif menu == "2":
            api.menu_2(menus[2], 'https://www.melon.com/chart/index.htm')
        elif menu == "3":
            api.menu_3(menus[3])
        else:
            print("다시 입력 해 주세요.")
