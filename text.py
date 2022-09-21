from color import Color


class Text:
    def __init__(self, text: str, color: Color):
        self.text = text
        self.color = color

    def __str__(self):
        return f'\033[{self.color.state};{self.color.color}m{self.text}\033[0m'
