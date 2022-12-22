from random import randint
from rich.console import Console

from location import Location
from player import Player
from textprinter import TextPrinter
from config import *
from functions import *


class WerewolfDiary:
    def __init__(self):
        self.console = Console()
        self.printer = TextPrinter(self.console)

        self.init_player()
        self.init_game()

        self.in_plot = False
        self.plot_file = ''
        self.plot_idx = 0

        self.input_sign = ''

        self.main()

    def goto(self, location: str):
        self.player.location = Location(location)

    def help(self):
        pass  # 根据location打印不同help内容

    def init_game(self):
        try:
            self.data = read_file('save/game_data.json')
        except FileNotFoundError:
            self.data = {
                'day': 0,
                'daytime': 0,
            }

    def init_player(self):
        try:
            self.player = Player(**read_file('save\\player.json'))
        except FileNotFoundError:
            while True:
                name = self.console.input('你的昵称是?')
                if not name.strip():
                    self.printer.warn(f'”{name}“不可用！')
                else:
                    break

            self.player = Player(name=name)
            verify_dir('save')
            save('save\\player.json', self.player.to_dict())

            self.in_plot = True
            self.plot_file = 'introduction.json'

            self.printer.plain(f'{self.player.name}，欢迎来到狼人日记！')
            self.printer.info('重复按下 Enter 以阅读信息')

    def main(self):
        while True:
            try:
                if self.in_plot:
                    self.input_sign = '*'
                else:
                    self.input_sign = ''

                print()
                input_action = input(f'{self.player.name}/{self.player.location}{self.input_sign}>')

                if self.in_plot:
                    plot_file = read_file(f'resources/plot/{self.plot_file}')
                    if 'var' in plot_file[self.plot_idx].keys():
                        self.printer.print(
                            plot_file[self.plot_idx]['text'] % eval(plot_file[self.plot_idx]['var']),
                            plot_file[self.plot_idx]['level']
                        )
                    else:
                        self.printer.print(plot_file[self.plot_idx]['text'], plot_file[self.plot_idx]['level'])
                    self.plot_idx += 1
                    if self.plot_idx >= len(plot_file):
                        self.in_plot = False
                else:
                    if len(input_action) > 1 and input_action[0] == '/':
                        if input_action[1:] in ['h', 'help']:
                            self.help()
                    else:
                        pass
            except Exception as e:
                self.printer.fatal(repr(e))


if __name__ == '__main__':
    main = WerewolfDiary()
