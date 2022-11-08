from scrapper.domains import Scrap
from scrapper.views import ScrapController
from util.common import Common

if __name__ == "__main__":
    scrap = Scrap()
    api = ScrapController

    while True:
        menus = ['종료', 'Bugs', 'Melon']
        menu = Common.menu(menus)
        if menu == "0":
            api.Menu_0(menus[0])
            break
        elif menu == "1":
            scrap.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            scrap.query_string = "20221101"
            scrap.parser = "lxml"
            scrap.class_names = ["title", "artist"]
            scrap.tag_name = "p"
            api.Menu_1(menus[1], scrap)
        elif menu == "2":
            scrap.domain = "https://www.melon.com/chart/index.htm?dayTime="
            scrap.query_string = "2022110810"
            scrap.parser = "lxml"
            scrap.class_names = ["ellipsis rank01", "ellipsis rank02"]
            scrap.tag_name = "div"
            api.Menu_2(menus[2], scrap)
        else:
            print("다시 입력 해 주세요.")
