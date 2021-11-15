from _internal.parsing_helpers import *
from _internal.data_elements   import *

from typing                    import Type
from re                        import sub

class Parser:
    def __init__(self) -> None:
        self.data = Data()

    def loadFile(self, filename: str):
        foldername = getFolderFromFileName(filename)
        for ln, l in readFileWithLineNumbers(filename):
            if l.lstrip().startswith("~") == False and l.lstrip().rstrip() != "":
                parseDataLine(self.data, foldername, filename, ln, l)
        
        return
    
    def getParsedData(self) -> Type[Data]:
        return self.data.sort()