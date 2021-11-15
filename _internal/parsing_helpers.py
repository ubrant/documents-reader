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

def trimLR(string: str) -> Type[str]:
    return string.lstrip().rstrip()

def trimMultipleSpaces(string: str) -> Type[str]:
    return sub("\s\s*", " ", string)

def getSecondAndRestOfString(string: str) -> Tuple[str, str]:
    string = trimLR(string)
    string = trimMultipleSpaces(string)
    parts = string.split()
    numParts = len(parts)

    if (numParts <= 1):
        return ("", "")
    if (numParts <= 2):
        return (trimLR(parts[1]), "")
    else:
        rest = ""
        for p in parts[2:]:
            rest += " " + p
        return (trimLR(parts[1]), trimLR(trimMultipleSpaces(rest)))

######################################################################
#                     Parsing Elements From Text                     #
######################################################################

######
# Parsing Major Elements
####
def processMajorElement(
                data: Data,
                foldername: str,
                filename: str,
                lineNumber: int, lineText: str) -> bool:
    
    if (lineText.lstrip().lower().startswith("@major")):
        idString, titleString = getSecondAndRestOfString(lineText)
        id = 0
        try:
            id = int(idString)
            me = data.getOrAddNewMajorElementById(id)
            me.setTitleIfEmpty(titleString)
            data.updateProcessingState(None, id, None, None, None)
        except:
            print(f"Error: Cannot parse Id at line#{lineNumber} in {filename}")
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
        idString, titleString = getSecondAndRestOfString(lineText)
        id = 0
        try:
            id = int(idString)
            major = data.getOrAddNewMajorElementById(data.currentMajorElementId)
            me = major.getOrAddNewMinorElementById(id)
            me.setTitleIfEmpty(titleString)
            data.updateProcessingState(None, None, id, None, None)
        except:
            print(f"Error: Cannot parse Id at line#{lineNumber} in {filename}")
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
        idString, titleString = getSecondAndRestOfString(lineText)
        id = 0
        try:
            id = int(idString)
            major = data.getOrAddNewMajorElementById(data.currentMajorElementId)
            minor = major.getOrAddNewMinorElementById(data.currentMinorElementId)
            se = minor.getOrAddNewSectionElementById(id)
            se.setTitleIfEmpty(titleString)
            data.updateProcessingState(None, None, None, id, None)
        except:
            print(f"Error: Cannot parse Id at line#{lineNumber} in {filename}")
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
        idString, titleString = getSecondAndRestOfString(lineText)
        id = 0
        try:
            id = int(idString)
            major = data.getOrAddNewMajorElementById(data.currentMajorElementId)
            minor = major.getOrAddNewMinorElementById(data.currentMinorElementId)
            sectn = minor.getOrAddNewSectionElementById(data.currentSectionElementId)
            pg = sectn.getOrAddNewPageElementById(id)
            pg.setTitleIfEmpty(titleString)
            data.updateProcessingState(None, None, None, None, id)
        except:
            print(f"Error: Cannot parse Id at line#{lineNumber} in {filename}")
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
    
    if (filename != data.lastProcessedFilename):
        data.updateProcessingState(filename, None, None, None, None)
    
    for p in processPipeline:
        success = p(data, foldername, filename, lineNumber, lineText)
        if success:
            break
    return

