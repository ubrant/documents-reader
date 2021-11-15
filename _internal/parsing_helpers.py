from _internal.data_elements   import *

from typing                    import Tuple, Type
from re                        import sub

######
# File Reading
####
def readFileWithLineNumbers(filename: str) -> Tuple[int, str]:
    f = open(filename, "rU", 4096, "utf-8-sig")
    ln = 0
    for line in f:
        ln += 1
        yield (ln, sub("\r", "", sub("\n", "", line)))

    f.close()
    return

######
# Common Extractors
####
def stripLastPartFromPath(filename: str) -> Type[str]:
    tmp = sub("/[^/]*$", "", filename)
    return sub("\\\\[^\\\\]*$", "", tmp)

######################################################################
#                     Parsing Elements From Text                     #
######################################################################
#
# Parsing Major Elements
####
def processMajorElement(
                data: Data,
                foldername: str,
                filename: str,
                lineNumber: int, lineText: str) -> bool:
    
    if (lineText.lstrip().lower().startswith("@major")):
        return True
    return False

######
# Parsing Minor Elements
####
def processMinorElement(
                data: Data,
                foldername: str,
                filename: str,
                lineNumber: int, lineText: str) -> bool:
    
    if (lineText.lstrip().lower().startswith("@minor")):
        return True
    return False

######
# Parsing Section Elements
####
def processSectionElement(
                data: Data,
                foldername: str,
                filename: str,
                lineNumber: int, lineText: str) -> bool:
    
    if (lineText.lstrip().lower().startswith("@section")):
        return True
    return False

######
# Parsing Page Elements
####
def processPageElement(
                data: Data,
                foldername: str,
                filename: str,
                lineNumber: int, lineText: str) -> bool:
    
    if (lineText.lstrip().lower().startswith("@page")):
        return True
    return False

######
# Parsing Pipeline
####
processPipeline = [
    processMajorElement,
    processMinorElement,
    processSectionElement,
    processPageElement
]
def parseDataLine(
                data: Data,
                foldername: str,
                filename: str,
                lineNumber: int, lineText: str) -> None:
    for p in processPipeline:
        success = p(data, foldername, filename, lineNumber, lineText)
        if success:
            break
    return

