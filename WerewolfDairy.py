from random import randint
from rich.console import Console

from textprinter import TextPrinter
from config import *
from functions import *


class WerewolfDiary:
    def __init__(self):
        self.console = Console()
        self.printer = TextPrinter(self.console)

        self.data = read_file('data\\data.json', default_data)
        self.backpack = read_file('data\\backpack.json', default_backpack)

        self.plot = False
        self.plot_file = ''

        self.input_sign = ''

        if not self.data['username']:
            self.data['username'] = self.get_username()
            self.plot = True
            self.plot_file = 'introduction.json'
            self.plot_idx = 0

            self.printer.info('重复按下 Enter 以阅读信息')

        self.main()

    def get_username(self) -> str:
        while not self.data['username']:
            username = self.console.input('你的昵称是?')
            if not username.strip():
                self.printer.warn(f'”{username}“不可用！')
            else:
                return username

    def goto(self, place_name: str):
        self.data['location'] = place_name

    def help(self):
        pass  # 根据location打印不同help内容

    def main(self):
        while True:
            try:
                if self.plot:
                    self.input_sign = '*'
                else:
                    self.input_sign = ''

                input_action = input(f'{self.data["username"]}/{self.data["location"]}{self.input_sign}>')

                if self.plot:
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
                        self.plot = False
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
