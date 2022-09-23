class Recipe:
    def __init__(self, input_items: dict):
        """
        :param input_items: {item1: amount1, item2: amount2, ...}
        """
        self.input_items = input_items

    def verify(self, input_items: dict):
        try:
            for i in self.input_items.keys():
                if not input_items[i] == self.input_items[i]:
                    return False
        except KeyError:
            return False
        return True
