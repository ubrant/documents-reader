# *****************************************************************************************
# * Purpose:
# *     Defining and loading settings for the whole application
# *
# *
# *****************************************************************************************
# * Author: Usama
# *
# *****************************************************************************************
# * Changes:
# *
# * Date         Changed by      Description
# * ----         ----------      -----------
# *
# *
# *
# *
# *****************************************************************************************

from sys        import argv
from os         import getcwd
from os.path    import join
from os.path    import sep

# ***********
# Command-line arguments:
#          1 => scan-directory
#          2 => recursion-enabled  [True/False]
#          3 => recursion-depth    [1000000 => infinite]
#          4 => output-directory
#          5 => base-url
# ********
class Settings:
    def __init__(self):
        workingDir = getcwd()
        libsDir = "libs-web"
        templatesDir = join(libsDir, "templates")
        outputDir = "Generated-Site"

        self.scriptName: str = ""
        self.scriptDir: str = workingDir
        self.scanDir: str = workingDir
        self.isRecursive: bool = True
        self.recursionDepth: int = 1000000
        self.baseUrl: str = "https://ubrant.com"

        self.libCssBootstrapFile: str  = join(workingDir, libsDir, "bootstrap.min.css")
        self.libCssSiteStylesFile: str = join(workingDir, libsDir, "site-styles.css")
        self.libJsJQueryFile: str      = join(workingDir, libsDir, "jquery.min.js")
        self.libJsBootstrapFile: str   = join(workingDir, libsDir, "bootstrap.min.js")
        self.libJsSiteScriptFile: str  = join(workingDir, libsDir, "site-script.js")

        self.outputDir: str = join(workingDir, outputDir)

        self.templateContentHeading1File: str              = join(workingDir, templatesDir, "content-heading1-template.html")
        self.templateContentHeading2File: str              = join(workingDir, templatesDir, "content-heading2-template.html")
        self.templateContentHeading3File: str              = join(workingDir, templatesDir, "content-heading3-template.html")
        self.templateContentHeading4File: str              = join(workingDir, templatesDir, "content-heading4-template.html")
        self.templateContentHeading5File: str              = join(workingDir, templatesDir, "content-heading5-template.html")
        self.templateContentHeading6File: str              = join(workingDir, templatesDir, "content-heading6-template.html")
        self.templateContentImageFile: str                 = join(workingDir, templatesDir, "content-image-template.html")
        self.templateContentCodeFile: str                  = join(workingDir, templatesDir, "content-code-template.html")
        self.templateContentConsoleFile: str               = join(workingDir, templatesDir, "content-console-template.html")
        self.templateContentListUnorderedFile: str         = join(workingDir, templatesDir, "content-list-unordered-template.html")
        self.templateContentListUnorderedItemFile: str     = join(workingDir, templatesDir, "content-list-unordered-item-template.html")
        self.templateContentParaFile: str                  = join(workingDir, templatesDir, "content-para-template.html")
        self.templateContentQuestionFile: str              = join(workingDir, templatesDir, "content-question-template.html")
        self.templateContentSectionFile: str               = join(workingDir, templatesDir, "content-section-template.html")
        self.templateSideMajorItemFile: str                = join(workingDir, templatesDir, "side-major-item-template.html")
        self.templateSideMinorItemFile: str                = join(workingDir, templatesDir, "side-minor-item-template.html")
        self.templateSideSectionItemFile: str              = join(workingDir, templatesDir, "side-section-item-template.html")
        self.templateSidePageItemFile: str                 = join(workingDir, templatesDir, "side-page-item-template.html")
        self.templateSiteFile: str                         = join(workingDir, templatesDir, "site-template.html")
        
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
        
        # Base URL
        if(argv):
            self.baseUrl = argv.pop(0)

        # Spoiling remaining elements
        while(argv):
            argv.pop()
        

    def print(self, headingLine, indent, appendBlankLines = 0):
        indent2 = indent
        for i in range (len(indent)):
            indent2 = " " + indent2
        
        recursion = "Disabled"
        if(self.isRecursive):
            recursion = "Enabled"
        
        recursionDepth = self.recursionDepth
        if(recursionDepth >= 1000000):
            recursionDepth = "Infinite"
        
        scriptDirInd = "<script-dir>"
        outputDir = self.outputDir.replace(self.scriptDir, scriptDirInd)
        
        libCssBootstrapFile = self.libCssBootstrapFile.replace(self.scriptDir, scriptDirInd)
        libCssSiteStylesFile = self.libCssSiteStylesFile.replace(self.scriptDir, scriptDirInd)
        libJsJQueryFile = self.libJsJQueryFile.replace(self.scriptDir, scriptDirInd)
        libJsBootstrapFile = self.libJsBootstrapFile.replace(self.scriptDir, scriptDirInd)
        libJsSiteScriptFile = self.libJsSiteScriptFile.replace(self.scriptDir, scriptDirInd)

        templateContentHeading1File              = self.templateContentHeading1File.replace(self.scriptDir, scriptDirInd)
        templateContentHeading2File              = self.templateContentHeading2File.replace(self.scriptDir, scriptDirInd)
        templateContentHeading3File              = self.templateContentHeading3File.replace(self.scriptDir, scriptDirInd)
        templateContentHeading4File              = self.templateContentHeading4File.replace(self.scriptDir, scriptDirInd)
        templateContentHeading5File              = self.templateContentHeading5File.replace(self.scriptDir, scriptDirInd)
        templateContentHeading6File              = self.templateContentHeading6File.replace(self.scriptDir, scriptDirInd)
        templateContentImageFile                 = self.templateContentImageFile.replace(self.scriptDir, scriptDirInd)
        templateContentCodeFile                  = self.templateContentCodeFile.replace(self.scriptDir, scriptDirInd)
        templateContentConsoleFile               = self.templateContentConsoleFile.replace(self.scriptDir, scriptDirInd)
        templateContentListUnorderedFile         = self.templateContentListUnorderedFile.replace(self.scriptDir, scriptDirInd)
        templateContentListUnorderedItemFile     = self.templateContentListUnorderedItemFile.replace(self.scriptDir, scriptDirInd)
        templateContentParaFile                  = self.templateContentParaFile.replace(self.scriptDir, scriptDirInd)
        templateContentQuestionFile              = self.templateContentQuestionFile.replace(self.scriptDir, scriptDirInd)
        templateContentSectionFile               = self.templateContentSectionFile.replace(self.scriptDir, scriptDirInd)
        templateSideMajorItemFile                = self.templateSideMajorItemFile.replace(self.scriptDir, scriptDirInd)
        templateSideMinorItemFile                = self.templateSideMinorItemFile.replace(self.scriptDir, scriptDirInd)
        templateSideSectionItemFile              = self.templateSideSectionItemFile.replace(self.scriptDir, scriptDirInd)
        templateSidePageItemFile                 = self.templateSidePageItemFile.replace(self.scriptDir, scriptDirInd)
        templateSiteFile                         = self.templateSiteFile.replace(self.scriptDir, scriptDirInd)
        
        print(headingLine)
        print(f"{indent}Script Directory       -> {self.scriptDir}")
        print(f"{indent}Script Name            -> {self.scriptName}")
        print(f"{indent}Scan Directory         *> {self.scanDir}")
        print(f"{indent}Recursion              *> {recursion}")
        print(f"{indent}Recursion Depth        *> {recursionDepth}")
        print(f"{indent}Output Path            *> {outputDir}")
        print(f"{indent}Base URL               *> {self.baseUrl}")
        
        print(f"{indent}Library:")
        print(f"{indent2}(Bootstrap)    -> {libCssBootstrapFile}")
        print(f"{indent2}(jQuery)       -> {libJsJQueryFile}")
        print(f"{indent2}(Bootstrap JS) -> {libJsBootstrapFile}")
        print(f"{indent2}(Site CSS)     -> {libCssSiteStylesFile}")
        print(f"{indent2}(Site JS)      -> {libJsSiteScriptFile}")

        print(f"{indent}Templates:")
        print(f"{indent2}(Content - Heading 1) -> {templateContentHeading1File}")
        print(f"{indent2}(Content - Heading 2) -> {templateContentHeading2File}")
        print(f"{indent2}(Content - Heading 3) -> {templateContentHeading3File}")
        print(f"{indent2}(Content - Heading 4) -> {templateContentHeading4File}")
        print(f"{indent2}(Content - Heading 5) -> {templateContentHeading5File}")
        print(f"{indent2}(Content - Heading 6) -> {templateContentHeading6File}")
        print(f"{indent2}(Content - Image)     -> {templateContentImageFile}")
        print(f"{indent2}(Content - Code)      -> {templateContentCodeFile}")
        print(f"{indent2}(Content - Console)   -> {templateContentConsoleFile}")
        print(f"{indent2}(Content - List - Unordered)      -> {templateContentListUnorderedFile}")
        print(f"{indent2}(Content - List - Unordered Item) -> {templateContentListUnorderedItemFile}")
        print(f"{indent2}(Content - Para)      -> {templateContentParaFile}")
        print(f"{indent2}(Content - Question)  -> {templateContentQuestionFile}")
        print(f"{indent2}(Content - Section)   -> {templateContentSectionFile}")
        print(f"{indent2}(Side - Major Item)   -> {templateSideMajorItemFile}")
        print(f"{indent2}(Side - Minor Item)   -> {templateSideMinorItemFile}")
        print(f"{indent2}(Side - Section Item) -> {templateSideSectionItemFile}")
        print(f"{indent2}(Side - Page Item)    -> {templateSidePageItemFile}")
        print(f"{indent2}(Site)                -> {templateSiteFile}")

        while (appendBlankLines > 0):
            print("")
            appendBlankLines = appendBlankLines - 1

        return
