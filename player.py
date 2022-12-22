from backpack import Backpack
from functions import read_file
from location import Location
from wallet import Wallet


class Player:
    name = ''
    backpack = Backpack()
    health = 5
    wallet = Wallet()
    location = Location()
    tags = []

    def __init__(self, **kwargs):
        for i, j in kwargs.items():
            self.write_in_raw(i, j)

    def to_dict(self):
        return {
            'name': self.name,
            'backpack': self.backpack.to_dict(),
            'health': self.health,
            'wallet': self.wallet.value,
            'location': self.location.value,
            'tags': self.tags
        }

    def write_in_raw(self, key: str, raw_value):
        if key == 'name':
            self.name = raw_value
        elif key == 'backpack':
            self.backpack = Backpack(raw_value)
        elif key == 'health':
            self.health = raw_value
        elif key == 'wallet':
            self.wallet = Wallet(raw_value)
        elif key == 'location':
            self.location = Location(raw_value)
        elif key == 'tags':
            self.tags = raw_value
