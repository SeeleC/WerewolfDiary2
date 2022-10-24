from random import randint

from backpack import Backpack
from config import *
from entity import *
from functions import *
from item import *


class WerewolfDiary:
    def __init__(self):
        self.data = get_data()
        self.backpack = get_backpack()

        if not self.data['username']:
            self.data['username'] = self.get_username()

            # 初始介绍
            print(f'\n剧情：曙光破晓，怪物停止了杀戮，幸存者从新一天的阳光中醒来。你叫 {self.data["username"]} ，是东镇的一个合法居民。')
            print('你住在东镇东区外围，这里濒临城郊，晚上就是怪物的天堂。')
            print('你的剧情从8点开始，晚上10点结束，一天有6次活动时间。')
            print('肉和蘑菇都是你生存的必需品，肉能保证你不被饿死。')
            print('肉还能用来换取金币，蘑菇也是制汤或制药的好材料。你可以去森林搜索来获得它们。')
            print('这个小镇还有很多的特殊剧情，玩家要自行探索。')
            print('现在开始你的日记')

        self.start_game()

    def get_username(self) -> str:
        while not self.data['username']:
            username = input('你的昵称是: \033[1m')
            print('\033[0m', end='')
            if not username.strip():
                warn(f'”{username}“不是一个有效的昵称！')
            else:
                return username

    def start_game(self):
        while True:
            act = input('你要干什么？[输入 help 获取帮助]')

            pass


if __name__ == '__main__':
    main = WerewolfDiary()
