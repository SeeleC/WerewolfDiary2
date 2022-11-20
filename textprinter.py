from rich.console import Console


class TextPrinter:
    def __init__(self, console: Console):
        self.console = console

    def debug(self, text: str):
        self.console.print(text, style='bold green')

    def info(self, text: str):
        self.console.print(text, style='lightblue')

    def plain(self, text: str):
        self.console.print(text)

    def warn(self, text: str):
        self.console.print(text, style='yellow')

    def error(self, text: str):
        self.console.print(text, style='orange')

    def fatal(self, text: str):
        self.console.print(text, style='bold red')
