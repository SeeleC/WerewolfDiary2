from backpack import Backpack
from functions import read_file
from location import Location
from wallet import Wallet


class Player:
    name: str = ''
    backpack = Backpack()
    health: float = 5
    wallet = Wallet()
    location = Location('home')
    tags: list = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'name':
                self.name = value
            elif key == 'backpack':
                self.backpack = Backpack(value)
            elif key == 'health':
                self.health = value
            elif key == 'wallet':
                self.wallet = Wallet(value)
            elif key == 'location':
                self.location = Location(value)
            elif key == 'tags':
                self.tags = value

    def add_tag(self, tag: str):
        self.tags.append(tag)

    def move_to(self, destination: Location):
        self.location = destination

    def to_dict(self):
        return {
            'name': self.name,
            'backpack': self.backpack.to_dict(),
            'health': self.health,
            'wallet': self.wallet.value,
            'location': 'home',
            'tags': self.tags
        }
