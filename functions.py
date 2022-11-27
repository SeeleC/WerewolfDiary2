from json import dump, load
from os import path, mkdir, getcwd
from random import random, choice
from typing import Union

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


def read_file(filename, default=None) -> Union[dict, list]:
    if not path.exists(path.join(getcwd(), filename)) and default is not None:
        verify_dir('data')
        data = default
        save(filename, data)
    else:
        with open(filename, 'r', encoding='utf-8') as f:
            data = load(f)
    return data


def get_recipe(id: str) -> Recipe:  # TODO recipe
    pass


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
