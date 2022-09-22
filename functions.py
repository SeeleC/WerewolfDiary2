from color import Color
from json import dump, load
from os import path, mkdir, getcwd

from config import default_data, debug_color, info_color, warn_color, fatal_color


def get_data():
    if not path.exists(path.join(getcwd(), 'data')):
        mkdir('data')

    if not path.exists(path.join(getcwd(), 'data\\data.json')):
        data = default_data
        save('data\\data.json', data)
    else:
        with open('data\\data.json', 'r', encoding='utf-8') as f:
            data = load(f)
    return data


def printc(text, color: Color = Color(Color.State.PLAIN)):
    print(color.dyeing_text(text))


def save(filename: str, data) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        dump(data, f)


def debug(text: str):
    printc(text, debug_color)


def info(text: str):
    printc(text, info_color)


def warn(text: str):
    printc(text, warn_color)


def fatal(text: str):
    printc(text, fatal_color)
