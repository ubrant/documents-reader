from _internal.settings       import Settings
from _internal.data_elements  import *

from os                       import mkdir, execl, system
from os.path                  import isdir, exists, join

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

class WebContentGenerator:
    def __init__(self, settings: Settings, data: Data) -> None:
        self.settings: Settings = settings
        self.data: Data = data
        self.written: bool = False
        return

    def generateOutput(self) -> None:
        self.printHierarchy()
        self.written = False
        if ensureDir(self.settings.outputDir):
            return ""
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
        if (self.written):
            pass
        return