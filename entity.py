class Entity:
    def __init__(self, name: str, id: str, health: float, attack: float = 0):
        self.name = name
        self.id = id
        self.health = health  # health point
        self.attack = attack  # attack strength

    def to_dict(self):
        return {'name': self.name, 'id': self.id, 'health': self.health, 'attack': self.attack}


class Entities:
    BLACK_SQUIRREL = Entity('黑松鼠', 'black_squirrel', 7, 2)
    IRON_GOLEM = Entity('铁傀儡', 'iron_golem', 40, 3)
    LEAF_ELF = Entity('叶精灵', 'leaf_elf', 35, 5)
    MIMIC = Entity('宝箱怪', 'mimic', 50, 3)
    SNOW_GOLEM = Entity('雪傀儡', 'snow_golem', 25, 0.5)
    SQUIRREL = Entity('松鼠', 'squirrel', 5, 1)
    TREE_SPIRIT = Entity('树精', 'tree_spirit', 15, 3)
    WEREWOLF = Entity('狼人', 'werewolf', 100, 5)
