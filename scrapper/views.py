from scrapper.services import BugsMusic, MelonMusic


class ScrapController(object):
    @staticmethod
    def Menu_0(*params):
        print(params[0])

    @staticmethod
    def Menu_1(*params):
        print(params[0])
        BugsMusic(params[1])

    @staticmethod
    def Menu_2(*params):
        print(params[0])
        MelonMusic(params[1])
