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

        self.introduce = False

        if not self.data['username']:
            self.data['username'] = self.get_username()
            self.introduce = True
            self.intro_idx = 0

            self.printer.info('重复按下 Enter ')

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
                input_action = input(f'{self.data["username"]}/{self.data["location"]}>')

                if self.introduce:
                    intro = read_file('resources\\text\\introduction.json')
                    if 'var' in intro[self.intro_idx].keys():
                        self.printer.print(
                            intro[self.intro_idx]['text'] % eval(intro[self.intro_idx]['var']),
                            intro[self.intro_idx]['level']
                        )
                    else:
                        self.printer.print(intro[self.intro_idx]['text'], intro[self.intro_idx]['level'])
                    self.intro_idx += 1
                    if self.intro_idx >= len(intro):
                        self.introduce = False
                else:
                    if len(input_action) > 1 and input_action[0] == '/':
                        if input_action [1:] in ['h', 'help']:
                            self.help()
                    else:
                        pass
            except Exception as e:
                self.printer.fatal(repr(e))


if __name__ == '__main__':
    main = WerewolfDiary()
