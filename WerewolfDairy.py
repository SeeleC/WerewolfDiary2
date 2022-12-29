from random import randint
from argparse import ArgumentParser
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

        self.in_plot = False
        self.plot_file = ''
        self.plot_idx = 0

        self.input_sign = ''
        self.launch_signal = True

        self.data = {}

        self.init_player()
        self.init_game()

        self.main()

    def execute(self, argv):
        if argv[0] == 'goto':
            self.goto(argv[1])
        elif argv[0] == 'help':
            self.help()

    def goto(self, location: str):
        self.player.location = Location(location)

    def help(self):
        print('可用的命令：')
        print(''.join(['\t' + i + '\n' for i in self.player.location.get_help()])[:-1])
        print('通用参数：')

    def init_game(self):
        try:
            self.data = read_file('save\\data.json')
        except FileNotFoundError:
            self.data = {
                'day': 0,
                'daytime': 0,
                'previous_daytime': 0
            }
            save('save\\data.json', self.data)

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

            self.player = Player(name=name, location='home')
            verify_dir('save')
            save('save\\player.json', self.player.to_dict())

            self.in_plot = True
            self.plot_file = 'introduction.json'

            self.printer.plain(f'{self.player.name}，欢迎来到狼人日记！')
            self.printer.info('重复按下 Enter 以阅读信息')

    def main(self):
        while True:
            try:
                if self.data['daytime'] != self.data['previous_daytime'] or self.launch_signal:
                    print(f'当前时间：{time_tips[self.data["daytime"]]}')
                    self.launch_signal = False

                if self.in_plot:
                    self.input_sign = signs['in_plot']
                else:
                    self.input_sign = signs['general']

                action = input(f'{self.player.name}/{self.player.location.value}{self.input_sign}>')

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
                    if len(action) > 1 and action[0] == '/':
                        action_args = action[1:].split()
                        self.execute(action_args)
            except Exception as e:
                raise e
                # self.printer.fatal(repr(e)) TODO 需删除的debug字段


if __name__ == '__main__':
    main = WerewolfDiary()
