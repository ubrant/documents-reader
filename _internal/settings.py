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
        libsDir = "libs-web"
        outputDir = "Generated-Site"

        self.scriptName: str = ""
        self.scriptDir: str = workingDir
        self.scanDir: str = workingDir
        self.isRecursive: bool = True
        self.recursionDepth: int = 1000000

        self.libCssBootstrapFile: str  = join(workingDir, libsDir, "bootstrap.min.css")
        self.libCssSiteStylesFile: str = join(workingDir, libsDir, "site-styles.css")
        self.libJsJQueryFile: str      = join(workingDir, libsDir, "jquery.min.js")
        self.libJsBootstrapFile: str   = join(workingDir, libsDir, "bootstrap.min.js")
        self.libJsSiteScriptFile: str  = join(workingDir, libsDir, "site-script.js")

        self.outputDir: str = join(workingDir, outputDir)
        
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
        
        outputDir = self.outputDir.replace(self.scriptDir, "<script-dir>")
        libCssBootstrapFile = self.libCssBootstrapFile.replace(self.scriptDir, "<script-dir>")
        libCssSiteStylesFile = self.libCssSiteStylesFile.replace(self.scriptDir, "<script-dir>")
        libJsJQueryFile = self.libJsJQueryFile.replace(self.scriptDir, "<script-dir>")
        libJsBootstrapFile = self.libJsBootstrapFile.replace(self.scriptDir, "<script-dir>")
        libJsSiteScriptFile = self.libJsSiteScriptFile.replace(self.scriptDir, "<script-dir>")

        print(headingLine)
        print(f"{indent}Script Directory       -> {self.scriptDir}")
        print(f"{indent}Script Name            -> {self.scriptName}")
        print(f"{indent}Scan Directory         *> {self.scanDir}")
        print(f"{indent}Recursion              *> {re}")
        print(f"{indent}Recursion Depth        *> {rd}")
        print(f"{indent}Output Path            *> {outputDir}")
        print(f"{indent}Library (Bootstrap)    -> {libCssBootstrapFile}")
        print(f"{indent}        (Site CSS)     -> {libCssSiteStylesFile}")
        print(f"{indent}        (jQuery)       -> {libJsJQueryFile}")
        print(f"{indent}        (Bootstrap JS) -> {libJsBootstrapFile}")
        print(f"{indent}        (Site JS)      -> {libJsSiteScriptFile}")

        while (appendBlankLines > 0):
            print("")
            appendBlankLines = appendBlankLines - 1

        return
