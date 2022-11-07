from scrapper.services import BugsMusic


class ScrapController(object):
    @staticmethod
    def menu_0(*params):
        print(params[0])

    @staticmethod
    def menu_1(*arg):
        print(arg[0])
        BugsMusic(arg[1])

    @staticmethod
    def menu_2(*arg):
        print(arg[0])

    @staticmethod
    def menu_3(*params):
        print(params[0])
