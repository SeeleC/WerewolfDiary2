from functions import get_item_from_id
from item import Item
from itemstack import ItemStack


class Backpack:
    def __init__(self, lst: list[str]):
        self.items = {}
        for i in lst:
            id, amount = i.split('*')
            self.items[id] = ItemStack(get_item_from_id(id), int(amount))

    def to_list(self, value_type: str = 'name'):
        return [f'{eval(f"i.item.{value_type}")}*{i.amount}' for i in self.items.values() if i.amount > 0]

    def get_items(self):
        return [i for i in self.items.values() if i.amount > 0]

    def add_item(self, item: Item, amount: int = 1):
        try:
            self.items[item.id].amount += amount
        except KeyError:
            self.items[item.id] = ItemStack(item, amount)

    def reduce_item(self, item: Item, amount: int):
        if self.items[item.id].amount < amount:
            raise ValueError(f'背包中的 {item.name} 数量少于 {amount} ！')
        else:
            self.items[item.id].amount -= amount

    def has(self, item: Item):
        if item in [i.item for i in self.items.values()]:
            return True
        else:
            return False
