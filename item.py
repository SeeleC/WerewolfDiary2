from color import Color
from itemtype import ItemType


class Item:
    def __init__(
            self,
            name: str,
            id: str,
            type: ItemType = ItemType.PLAIN,
            rarity: int = 0,
            attack_damage: int = 1,
    ):
        self.name = name
        self.id = id
        self.rarity = rarity
        self.type = type
        self.attack_damage = attack_damage

    def __str__(self):
        return self.get_color().dyeing_text(self.name)

    def get_color(self):
        if self.rarity == 0:  # 普通材料 初期装备
            return Color(state=Color.State.BOLD)
        elif self.rarity == 1:  # 高级材料 需要蓝图的低级装备
            return Color(state=Color.State.BOLD, color=Color.Color.GREEN)
        elif self.rarity == 2:  # 高级装备
            return Color(state=Color.State.BOLD, color=Color.Color.YELLOW)
        elif self.rarity == 3:  # 顶级装备
            return Color(state=Color.State.BOLD, color=Color.Color.RED)
        elif self.rarity == 10:  # 蓝图
            return Color(state=Color.State.BOLD, color=Color.Color.BLUE)


class Items:  # 货币的物品形式（非必要）
    BOW = Item('弓', 'bow', type=ItemType.T_BOW, attack_damage=16, rarity=2)
    BLUEPRINT_CHAINSAW = Item('蓝图：电锯', 'blueprint_chainsaw', type=ItemType.BLUEPRINT, rarity=10)
    BLUEPRINT_CRYSTAL_AXE = Item('蓝图：水晶斧', 'blueprint_crystal_axe', type=ItemType.BLUEPRINT, rarity=10)
    BLUEPRINT_GOLDEN_TOOLS = Item('蓝图：金制工具', 'blueprint_golden_tools', type=ItemType.BLUEPRINT, rarity=10)
    BLUEPRINT_HOLY_SWORD = Item('蓝图：圣剑', 'blueprint_holy_sword', type=ItemType.BLUEPRINT, rarity=10)
    BLUEPRINT_IRON_TOOLS = Item('蓝图：铁制工具', 'blueprint_iron_tools', type=ItemType.BLUEPRINT, rarity=10)
    BLUEPRINT_LUCKY_SHOVEL = Item('蓝图：气运之锹', 'blueprint_lucky_shovel', type=ItemType.BLUEPRINT, rarity=10)
    BLUEPRINT_SILVER_LIGHT = Item('蓝图：银光', 'blueprint_silver_light', type=ItemType.BLUEPRINT, rarity=10)
    CHAINSAW = Item('电锯', 'chainsaw', type=ItemType.T_AXE, attack_damage=20, rarity=2)
    CRYSTAL_AXE = Item('水晶斧', 'crystal_axe', rarity=3)
    DIAMOND = Item('钻石', 'diamond', rarity=1)
    ELVEN_BLOOD = Item('精灵之血', 'elven_blood', rarity=1)
    FUR = Item('毛皮', 'fur')
    GOLD = Item('金', 'gold')
    GOLDEN_SWORD = Item('金剑', 'golden_sword', type=ItemType.T_SWORD, attack_damage=17, rarity=2)
    HOLY_SWORD = Item('圣剑', 'holy_sword', type=ItemType.T_SWORD, attack_damage=35, rarity=3)
    ICE = Item('雪', 'ice')
    IRON = Item('铁', 'iron')
    IRON_AXE = Item('铁斧', 'iron_axe', type=ItemType.T_AXE, attack_damage=12, rarity=1)
    IRON_SHOVEL = Item('铁锹', 'iron_shovel', type=ItemType.T_SHOVEL, attack_damage=9, rarity=1)
    IRON_SWORD = Item('铁剑', 'iron_sword', type=ItemType.T_SWORD, attack_damage=15, rarity=1)
    LUCKY_SHOVEL = Item('气运之锹', 'lucky_shovel', type=ItemType.T_SHOVEL, attack_damage=2, rarity=3)
    MEAT = Item('肉', 'meat')
    MUSHROOM = Item('蘑菇', 'mushroom')
    PUMPKIN = Item('南瓜', 'pumpkin')
    SILVER_LIGHT = Item('银光', 'silver_light', type=ItemType.T_SPEAR, attack_damage=25, rarity=3)
    SOIL = Item('土壤', 'soil')
    SPEAR = Item('长矛', 'spear', type=ItemType.T_SPEAR, attack_damage=10, rarity=2)
    STONE = Item('石头', 'stone')
    STONE_AXE = Item('石斧', 'stone_axe', type=ItemType.T_AXE, attack_damage=8)
    STONE_SHOVEL = Item('石锹', 'stone_shovel', type=ItemType.T_SHOVEL, attack_damage=6)
    STONE_SWORD = Item('石剑', 'stone_sword', type=ItemType.T_SWORD, attack_damage=10)
    TEETH = Item('牙齿', 'teeth')
    WEREWOLF_BLOOD = Item('狼人之血', 'werewolf_blood', rarity=1)
    WOOD = Item('木头', 'wood')
    WOODEN_AXE = Item('木斧', 'wooden_axe', type=ItemType.T_AXE, attack_damage=4)
    WOODEN_SHOVEL = Item('木锹', 'wooden_shovel', type=ItemType.T_SHOVEL, attack_damage=3)
    WOODEN_SWORD = Item('木剑', 'wooden_sword', type=ItemType.T_SWORD, attack_damage=5)
