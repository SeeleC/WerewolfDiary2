class Color:
    def __init__(self, state: int, color: int = None):
        self.color = color
        self.state = state

    def dyeing_text(self, text: str, end: str = '\033[0m') -> str:
        if self.color is not None:
            return '\033[' + str(self.state) + ';' + str(self.color) + 'm' + text + end
        else:
            return '\033[' + str(self.state) + 'm' + text + end

    def set_state(self, state: int):
        self.state = state
        return self

    def set_color(self, color: int):
        self.color = color
        return self

    class States:
        PLAIN = 0
        BOLD = 1
        UNDERSCORE = 4
        EVASIVE = 5
        REVERSE = 7
        DISAPPEAR = 8

    class Colors:
        BLACK = 30
        BLUE = 34
        GREEN = 32
        CYAN = 36
        RED = 31
        PURPLE = 35
        BROWN = 33
        YELLOW = 33
        WHITE = 37
