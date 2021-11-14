from re import sub

class ParsedData:
    def __init__(me):
        pass
    
    def sort(me):
        return me


def getFolderFromFileName(filename: str) -> str:
    tmp = sub("/[^/]*$", "", filename)
    return sub("\\\\[^\\\\]*$", "", tmp)

def readFileWithLineNumbers(filename: str) -> (int, str):
    f = open(filename)
    ln = 0
    for line in f:
        ln += 1
        yield (ln, sub("\r", "", sub("\n", "", line)))

    f.close()

class Parser:
    def __init__(self):
        self.data = ParsedData()

    def loadFile(self, filename: str):
        foldername = getFolderFromFileName(filename)
        for ln, l in readFileWithLineNumbers(filename):
            print(f"{ln}: {l}")
        
        return
    
    def getParsedData(self) -> type(ParsedData):
        return self.data.sort()