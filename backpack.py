from item import Item


class Backpack:
    def __init__(self, lst: list[str]):
        self.items = {}
        for i in lst:
            name, amount = i.split('*')
            self.items[name] = int(amount)

    def get_formatted_items(self):
        return [f'{i}*{j}' for i, j in self.items if j > 0]

    def add_item(self, item: Item, amount: int):
        self.items[item.name] = amount

    def reduce_item(self, item: Item, amount: int):
        if self.items[item.name] < amount:
            raise ValueError(f'背包中的 {item.name} 数量少于 {amount} ！')
        else:
            self.items[item.name] -= amount
