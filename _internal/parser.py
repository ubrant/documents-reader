from _internal.parsing_helpers import *

from re import sub

class ParsedData:
    def __init__(me):
        pass
    
    def sort(me):
        return me

class Parser:
    def __init__(self):
        self.data = ParsedData()

    def loadFile(self, filename: str):
        foldername = getFolderFromFileName(filename)
        for ln, l in readFileWithLineNumbers(filename):
            if l.lstrip().startswith("~") == False and l.lstrip().rstrip() != "":
                print(f"{ln}: {l}")
        
        return
    
    def getParsedData(self) -> type(ParsedData):
        return self.data.sort()