from _internal.settings       import Settings
from _internal.data_elements  import *

from os                       import mkdir, execl, system
from os.path                  import isdir, exists, join

######
# Helpers
####
def ensureDir(dirname: str) -> bool:
    if exists(dirname):
        if isdir(dirname):
            return True
        else:
            print(f"Error: {dirname} exists but it is not a directory")
    else:
        mkdir(dirname)
        if isdir(dirname):
            return True
    return False

def loadFileText(indent: str, filename: str):
    print(f"{indent}{filename}")
    f = open(filename)
    text = f.read()
    f.close()
    return text

######
# Web Content Generator
####
class WebContentGenerator:
    def __init__(self, settings: Settings, data: Data) -> None:
        self.settings: Settings = settings
        self.data: Data = data
        self.lastWrittenFilename: str = None

        self.templateContentHeading1: str = None
        self.templateContentHeading2: str = None
        self.templateContentHeading3: str = None
        self.templateContentHeading4: str = None
        self.templateContentHeading5: str = None
        self.templateContentHeading6: str = None
        self.templateContentImage: str = None
        self.templateContentLink: str = None
        self.templateContentListUnordered: str = None
        self.templateContentListUnorderedItem: str = None
        self.templateContentPara: str = None
        self.templateContentQuestion: str = None
        self.templateContentSection: str = None
        self.templateSideMajorItem: str = None
        self.templateSideMinorItem: str = None
        self.templateSideSectionItem: str = None
        self.templateSidePageItem: str = None
        self.templateSite: str = None

        self.loadTemplates()
        return

    def loadTemplates(self) -> None:
        print("Loading templates:")

        indent: str = " > "
        self.templateContentHeading1: str = loadFileText(indent, self.settings.templateContentHeading1File)
        self.templateContentHeading2: str = loadFileText(indent, self.settings.templateContentHeading2File)
        self.templateContentHeading3: str = loadFileText(indent, self.settings.templateContentHeading3File)
        self.templateContentHeading4: str = loadFileText(indent, self.settings.templateContentHeading4File)
        self.templateContentHeading5: str = loadFileText(indent, self.settings.templateContentHeading5File)
        self.templateContentHeading6: str = loadFileText(indent, self.settings.templateContentHeading6File)
        self.templateContentImage: str = loadFileText(indent, self.settings.templateContentImageFile)
        self.templateContentLink: str = loadFileText(indent, self.settings.templateContentLinkFile)
        self.templateContentListUnordered: str = loadFileText(indent, self.settings.templateContentListUnorderedFile)
        self.templateContentListUnorderedItem: str = loadFileText(indent, self.settings.templateContentListUnorderedItemFile)
        self.templateContentPara: str = loadFileText(indent, self.settings.templateContentParaFile)
        self.templateContentQuestion: str = loadFileText(indent, self.settings.templateContentQuestionFile)
        self.templateContentSection: str = loadFileText(indent, self.settings.templateContentSectionFile)
        self.templateSideMajorItem: str = loadFileText(indent, self.settings.templateSideMajorItemFile)
        self.templateSideMinorItem: str = loadFileText(indent, self.settings.templateSideMinorItemFile)
        self.templateSideSectionItem: str = loadFileText(indent, self.settings.templateSideSectionItemFile)
        self.templateSidePageItem: str = loadFileText(indent, self.settings.templateSidePageItemFile)
        self.templateSite: str = loadFileText(indent, self.settings.templateSiteFile)

        return

    def generateOutput(self) -> None:
        self.printHierarchy()
        self.lastWrittenFilename = ""

        if ensureDir(self.settings.outputDir):
            for major in self.data.majors:
                for minor in major.minors:
                    for section in minor.sections:
                        for page in section.pages:
                            self.writeHtmlPage(major, minor, section, page)
        return

    def writeHtmlPage(self, major: Major,
                            minor: Minor,
                            section: Section,
                            page: Page):
        
        self.lastWrittenFilename = join(
            self.settings.outputDir,
            f"P{major.id}.{minor.id}.{section.id}.{page.id}.html")

        #f = open(self.lastWrittenFilename, "w")
        return

    def printHierarchy(self) -> None:
        print("Hierarchy:")
        for major in self.data.majors:
            print(f" > Major({major.id}): {major.title}")
            for minor in major.minors:
                print(f"    > Minor({minor.id}): {minor.title}")
                for section in minor.sections:
                    print(f"       > Section({section.id}): {section.title}")
                    for page in section.pages:
                        print(f"          > Page({page.id}): {page.title}")

    def openOutput(self) -> None:
        if (self.lastWrittenFilename != None and self.lastWrittenFilename != ""):
            pass
        return