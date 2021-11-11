from sys   import argv
from os    import getcwd

######
# Command-line arguments:
#          1 => directory-path
#          2 => recursive-behavior [True/False]
#          3 => recursion-depth    [0 for infinite]
####
class Arguments:
    def __init__(self):
        self.scriptName = ""
        self.directoryPath = getcwd()
        self.isRecursive = True
        self.recursionDepth = 0
        
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

            if(value == "false"):
                self.isRecursive = False
            else:
                self.isRecursive = True

        # Recursion depth
        if(argv):
            try:
                self.recursionDepth = int(argv.pop(0))
            except:
                self.recursionDepth = 0

        # Spoiling remaining elements
        while(argv):
            argv.pop()
        

    def print(self):
        rd = self.recursionDepth
        if(rd == 0):
            rd = "Infinite"
        
        print(f"Script Name:       {self.scriptName}")
        print(f"Directory Path:    {self.directoryPath}")
        print(f"Recursion Enabled: {self.isRecursive}")
        print(f"Recursion Depth:   {rd}")
        return
