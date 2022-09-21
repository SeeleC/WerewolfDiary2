class Color:
    def __init__(self, state: int, color: int = None):
        self.color = color
        self.state = state

    def get_formatted_text(self, text: str):
        if self.color is not None:
            return '\033[' + str(self.state) + ';' + str(self.color) + 'm' + text + '\033[0m'
        else:
            return '\033[' + str(self.state) + 'm' + text + '\033[0m'

    class Code:
        BLACK = 30
        BLUE = 34
        GREEN = 32
        CYAN = 36
        RED = 31
        PURPLE = 35
        BROWN = 33
        YELLOW = 33
        WHITE = 37

        PLAIN = 0
        BOLD = 1
        UNDERSCORE = 4
        EVASIVE = 5
        REVERSE = 7
        DISAPPEAR = 8
