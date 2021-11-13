from _internal.settings       import Settings
from _internal.parser         import Parser


class WebContentGenerator:
    def __init__(self, settings: Settings, parser: Parser):
        parser.sortData()
        pass

    def generateOutput(self):
        pass

    def openOutput(self):
        pass