from json import dump, load
from os import path, mkdir, getcwd
from random import random, choice
from typing import Union

from config import debug_color, info_color, warn_color, fatal_color
from color import Color
from item import Item, Items
from recipe import Recipe


def act(text: str) -> list[str]:
    if text[0] == '/':
        command = text.split(' ')
        args = [i for i in command[1:]]

        if len(command) == 1:
            return [f'event.{command[0]}.list']
        else:
            return [f'event.{command[0]}.{command[1]}', args]
    else:
        raise SyntaxError()


def get_file(filename, default=None) -> Union[dict, list]:
    if not path.exists(path.join(getcwd(), filename)) and default is not None:
        verify_dir('data')
        data = default
        save(filename, data)
    else:
        with open(filename, 'r', encoding='utf-8') as f:
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


def verify_dir(name: str) -> None:
    if not path.exists(path.join(getcwd(), name)):
        mkdir(name)
