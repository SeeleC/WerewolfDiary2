from item import Item


class ItemStack:
    def __init__(self, item: Item, amount: int = 0):
        self.item = item
        self.amount = amount
