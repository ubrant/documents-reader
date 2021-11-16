from _internal.settings       import Settings
from _internal.data_elements  import *


class WebContentGenerator:
    def __init__(self, settings: Settings, data: Data) -> None:
        self.settings = settings
        self.data = data
        return

    def generateOutput(self) -> None:
        self.printHierarchy()
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
        return