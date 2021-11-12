from sys   import argv
from os    import getcwd

######
# Command-line arguments:
#          1 => directory-path
#          2 => recursive-behavior [True/False]
#          3 => recursion-depth    [1000 => infinite]
####
class Settings:
    def __init__(self):
        self.scriptName = ""
        self.directoryPath = getcwd()
        self.isRecursive = True
        self.recursionDepth = 1000
        
        self.parseArguments()

    def parseArguments(self):
        # Script name
        if(argv):
            self.scriptName = argv.pop(0)

        # Directory path
        if(argv):
            try:
                self.directoryPath = argv.pop(0)
            except:
                self.directoryPath = getcwd()
        
        # Recursiveness enabled
        if(argv):
            value = argv.pop(0).lstrip().rstrip().lower()

            if(value == "false" or value == "0"):
                self.isRecursive = False
            else:
                self.isRecursive = True

        # Recursion depth
        if(argv):
            try:
                self.recursionDepth = int(argv.pop(0))
            except:
                self.recursionDepth = 1000

        # Spoiling remaining elements
        while(argv):
            argv.pop()
        

    def print(self, headingLine, indent, appendBlankLines = 0):
        rd = self.recursionDepth
        if(rd == 1000):
            rd = "Infinite"
        
        print(headingLine)
        print(f"{indent}Script Name       -> {self.scriptName}")
        print(f"{indent}Directory Path    -> {self.directoryPath}")
        print(f"{indent}Recursion Enabled -> {self.isRecursive}")
        print(f"{indent}Recursion Depth   -> {rd}")

        while (appendBlankLines > 0):
            print("")
            appendBlankLines = appendBlankLines - 1

        return
