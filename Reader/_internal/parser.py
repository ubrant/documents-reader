# *****************************************************************************************
# * Purpose:
# *     Entry-point for parsing pipeline
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

from _internal.parsing_pipeline import *
from _internal.data_elements    import *

from typing                     import Type
from re                         import sub

# ***********
# File Reading
# ********
def readFileWithLineNumbers(filename: str) -> Tuple[int, str]:
    f = open(filename, "rU", 8192, "utf-8-sig")
    ln = 0
    for line in f:
        ln += 1
        yield (ln, sub("\r", "", sub("\n", "", line)))

    f.close()
    return

# ***********
# Parsing Point
# ********
class Parser:
    def __init__(self) -> None:
        self.data = Data()

    def loadFile(self, filename: str):
        foldername = stripLastPartFromPath(filename)
        for ln, l in readFileWithLineNumbers(filename):
            if not l.lstrip().startswith("~"):
                parseUncommentedLine(self.data, foldername, filename, ln, l)
        
        return
    
    def getParsedAndFilteredData(self) -> Type[Data]:
        return self.data.filterAndSort()
