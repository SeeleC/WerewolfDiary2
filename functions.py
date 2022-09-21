from color import Color
from json import dump, load
from os import path, mkdir, getcwd


def get_data():
    if not path.exists(path.join(getcwd(), 'data')):
        mkdir('data')

    with open('data\\data.json') as f:
        return load(f)


def printc(text, color: Color = Color(30, 0)):
    print(color.get_formatted_text(text))


def save(filename: str, data) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        dump(data, f)
