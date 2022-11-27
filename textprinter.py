from time import sleep

from rich.console import Console


class TextPrinter:
    def __init__(self, console: Console):
        self.console = console

    def debug(self, text: str):
        self.console.print(text, style='bold green')

    def info(self, text: str):
        self.console.print(text, style='#add8e6')

    def plain(self, text: str):
        self.console.print(text)

    def title(self, text: str):
        self.console.print(text, style='bold')

    def warn(self, text: str):
        self.console.print(text, style='yellow')

    def error(self, text: str):
        self.console.print(text, style='orange')

    def fatal(self, text: str):
        self.console.print(text, style='bold red')

    def print(self, text: str, level: str, wait: float = 0):
        sleep(wait)
        if level.lower() == 'debug':
            self.debug(text)
        elif level.lower() == 'info':
            self.info(text)
        elif level.lower() == 'plain':
            self.plain(text)
        elif level.lower() == 'title':
            self.title(text)
        elif level.lower() == 'warn':
            self.warn(text)
        elif level.lower() == 'error':
            self.error(text)
        elif level.lower() == 'fatal':
            self.fatal(text)

