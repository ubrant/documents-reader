class ParsedData:
    def __init__(me):
        pass
    
    def sort(me):
        return me


class Parser:
    def __init__(self):
        self.parsedData = ParsedData()
        self.sortedData = None
        pass

    def parseFile(self, filename: str):
        self.sortedData = None
        pass
        
    def getSortedData(self) -> type(ParsedData):
        if (self.sortedData == None):
            self.sortedData = self.parsedData
            return self.sortedData.sort()

        return self.parsedData.sortedData()