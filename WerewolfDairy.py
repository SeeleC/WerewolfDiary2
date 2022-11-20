from random import randint
from rich.console import Console

from textprinter import TextPrinter
from config import *
from functions import *
from item import *


class WerewolfDiary:
    def __init__(self):
        self.console = Console()
        self.printer = TextPrinter(self.console)

        self.data = get_file('data\\data.json', default_data)
        self.backpack = get_file('data\\backpack.json', default_backpack)

        if not self.data['username']:
            self.data['username'] = self.get_username()

            print(f'\n剧情：曙光破晓，怪物停止了杀戮，幸存者从新一天的阳光中醒来。你叫 {self.data["username"]} ，是东镇的一个合法居民。')
            print('你住在东镇东区外围，这里濒临城郊，晚上就是怪物的天堂。')
            print('你每天有6次活动时间。')
            print('食物是你生存的必需品，它们能保证你不被饿死。')
            print('食物还能用来换取金币，蘑菇是制汤或制药的好材料。你可以去森林搜索来获得它们。')
            print('这个小镇还有很多的特殊剧情，玩家要自行探索。')
            print('现在开始你的日记')

        self.start_game()

    def get_username(self) -> str:
        while not self.data['username']:
            username = self.console.input('你的昵称是: ')
            if not username.strip():
                self.printer.warn(f'”{username}“不是一个有效的昵称！')
            else:
                return username

    def goto(self, place_name: str):
        self.data['location'] = place_name

    def help(self):
        pass  # 根据location打印不同help内容

    def start_game(self):
        while True:
            try:
                input_action = input('你要干什么？[输入 /help 获取帮助]: ')

                if len(input_action) > 0 and input_action[0] == '/':
                    pass
                else:
                    pass
            except Exception as e:
                self.printer.fatal(repr(e))


if __name__ == '__main__':
    main = WerewolfDiary()
