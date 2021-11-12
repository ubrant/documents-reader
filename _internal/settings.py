from sys        import argv
from os         import getcwd
from os.path    import join
from os.path    import sep

######
# Command-line arguments:
#          1 => scan-directory
#          2 => recursion-enabled  [True/False]
#          3 => recursion-depth    [1000000 => infinite]
#          4 => output-directory
####
class Settings:
    def __init__(self):
        workingDir = getcwd()
        libsDir = "external-libs"
        outputDir = "Generated-Site"

        self.scriptName = ""
        self.scriptDir = workingDir
        self.scanDir = workingDir
        self.isRecursive = True
        self.recursionDepth = 1000000

        self.libBootstrapFile = join(workingDir, libsDir, "bootstrap.min.css")

        self.outputDir = join(workingDir, outputDir)
        
        self.parseArguments()

    def parseArguments(self):
        # Script name
        if(argv):
            self.scriptName = argv.pop(0).replace(self.scriptDir, "").replace(sep, "")

        # Scan Directory path
        if(argv):
            try:
                self.scanDir = argv.pop(0)
            except: pass
        
        # Recursion enabled
        if(argv):
            value = argv.pop(0).lstrip().rstrip().lower()

            if(value == "false" or value.startswith("0")):
                self.isRecursive = False
            else:
                self.isRecursive = True

        # Recursion depth
        if(argv):
            try:
                self.recursionDepth = int(argv.pop(0))
            except: pass
        
        # Output path
        if(argv):
            self.outputDir = argv.pop(0)

        # Spoiling remaining elements
        while(argv):
            argv.pop()
        

    def print(self, headingLine, indent, appendBlankLines = 0):
        re = "Disabled"
        if(self.isRecursive):
            re = "Enabled"
        
        rd = self.recursionDepth
        if(rd == 1000000):
            rd = "Infinite"
        
        print(headingLine)
        print(f"{indent}Script Directory    -> {self.scriptDir}")
        print(f"{indent}Script Name         -> {self.scriptName}")
        print(f"{indent}Scan Directory      -> {self.scanDir}")
        print(f"{indent}Recursion           -> {re}")
        print(f"{indent}Recursion Depth     -> {rd}")
        print(f"{indent}Output Path         -> {self.outputDir}")
        print(f"{indent}Library (Bootstrap) -> {self.libBootstrapFile}")

        while (appendBlankLines > 0):
            print("")
            appendBlankLines = appendBlankLines - 1

        return
