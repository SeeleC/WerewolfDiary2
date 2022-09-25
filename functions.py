from json import dump, load
from os import path, mkdir, getcwd
from random import random, choice

from config import default_data, debug_color, info_color, warn_color, fatal_color, default_backpack
from color import Color
from item import Item, Items
from recipe import Recipe


def get_backpack() -> list:
    verify_dir()

    if not path.exists(path.join(getcwd(), 'data\\backpack.json')):
        backpack = default_backpack
        save('data\\backpack.json', backpack)
    else:
        with open('data\\backpack.json', 'r', encoding='utf-8') as f:
            backpack = load(f)
    return backpack


def get_data() -> dict:
    verify_dir()

    if not path.exists(path.join(getcwd(), 'data\\data.json')):
        data = default_data
        save('data\\data.json', data)
    else:
        with open('data\\data.json', 'r', encoding='utf-8') as f:
            data = load(f)
    return data


def get_item_from_id(id: str) -> Item:
    items = vars(Items)
    for i, j in items.items():
        if i.lower() == id:
            return items[i]
    raise AttributeError(f'没有id为 {id} 的物品！')


def get_item_from_name(name: str) -> Item:
    items = vars(Items)
    for i in items.values():
        if isinstance(i, Item) and i.name == name:
            return i
    raise AttributeError(f'没有名称为 {name} 的物品！')


def get_recipe(id: str) -> Recipe:  # TODO recipe
    pass


def printc(text, color: Color = Color(Color.States.PLAIN)) -> None:
    print(color.dyeing_text(text))


def random_choice(lst: list, probability: float):
    number = random()
    if number <= probability:
        return choice(lst)
    else:
        return None


def save(filename: str, data) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        dump(data, f, indent=1)


def verify_dir() -> None:
    if not path.exists(path.join(getcwd(), 'data')):
        mkdir('data')


def debug(text: str) -> None:
    printc(text, debug_color)


def info(text: str) -> None:
    printc(text, info_color)


def warn(text: str) -> None:
    printc(text, warn_color)


def fatal(text: str) -> None:
    printc(text, fatal_color)
