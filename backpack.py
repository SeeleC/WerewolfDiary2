from functions import get_item
from item import Item, Items


class Backpack:
    def __init__(self, lst: list[str]):
        self.items = {}
        for i in lst:
            id, amount = i.split('*')
            self.items[get_item(id)] = int(amount)

    def get_formatted_items(self):
        return [f'{i.id}*{j}' for i, j in self.items.items() if j > 0]

    def get_items(self):
        return {i: j for i, j in self.items.items() if j > 0}

    def add_item(self, item: Item, amount: int = 1):
        try:
            self.items[item] += amount
        except KeyError:
            self.items[item] = amount

    def reduce_item(self, item: Item, amount: int):
        if self.items[item] < amount:
            raise ValueError(f'背包中的 {item.name} 数量少于 {amount} ！')
        else:
            self.items[item] -= amount
