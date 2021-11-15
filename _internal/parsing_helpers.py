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

def getSecondAndThirdRestOfString(string: str) -> Tuple[str, str]:
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

def getSecondRestOfString(string: str) -> Type[str]:
    string = trimLR(string)
    string = trimMultipleSpaces(string)
    parts = string.split()
    numParts = len(parts)

    if (numParts <= 1):
        return ""
    else:
        rest = ""
        for p in parts[1:]:
            rest += " " + p
        return trimLR(rest)

######################################################################
#                     Parsing Elements From Text                     #
######################################################################

######
# Parsing Major Elements
####
def processMajorIdElement(
                data: Data,
                foldername: str,
                filename: str,
                lineNumber: int, lineText: str) -> bool:
    
    if (lineText.lstrip().lower().startswith("@major")):
        idString, titleString = getSecondAndThirdRestOfString(lineText)
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
def processMinorIdElement(
                data: Data,
                foldername: str,
                filename: str,
                lineNumber: int, lineText: str) -> bool:
    
    if (lineText.lstrip().lower().startswith("@minor")):
        idString, titleString = getSecondAndThirdRestOfString(lineText)
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
def processSectionIdElement(
                data: Data,
                foldername: str,
                filename: str,
                lineNumber: int, lineText: str) -> bool:
    
    if (lineText.lstrip().lower().startswith("@section")):
        idString, titleString = getSecondAndThirdRestOfString(lineText)
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
def processPageIdElement(
                data: Data,
                foldername: str,
                filename: str,
                lineNumber: int, lineText: str) -> bool:
    
    if (lineText.lstrip().lower().startswith("@page")):
        idString, titleString = getSecondAndThirdRestOfString(lineText)
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

def processPageTextElements(
                data: Data,
                foldername: str,
                filename: str,
                lineNumber: int, lineText: str) -> bool:
    
    trimmedLowercaseLine = trimLR(lineText).lower()
    secondHalfLine = getSecondRestOfString(lineText)
    page = data.getActivePage()

    # Section Tags
    if (trimmedLowercaseLine.startswith("$h1:")):
        return True

    if (trimmedLowercaseLine.startswith("$h2:")):
        return True

    if (trimmedLowercaseLine.startswith("$dt:")):
        return True

    if (trimmedLowercaseLine.startswith("$qt:")):
        return True

    if (trimmedLowercaseLine.startswith("$qb:")):
        return True

    if (trimmedLowercaseLine.startswith("$bg:")):
        return True

    # Heading Tags
    if (trimmedLowercaseLine.startswith("#h1:")):
        return True

    if (trimmedLowercaseLine.startswith("#h2:")):
        return True

    if (trimmedLowercaseLine.startswith("#h3:")):
        return True

    if (trimmedLowercaseLine.startswith("#h4:")):
        return True

    if (trimmedLowercaseLine.startswith("#h5:")):
        return True

    if (trimmedLowercaseLine.startswith("#h6:")):
        return True

    # Paragraph Tag
    if (trimmedLowercaseLine.startswith("#para:")):
        return True

    # List Tag
    if (trimmedLowercaseLine.startswith("#list:")):
        return True

    # Image Tag
    if (trimmedLowercaseLine.startswith("#image:")):
        return True
    
    return page.appendText(lineText)

######
# Parsing Pipeline
####
processPipeline = [
    processMajorIdElement,
    processMinorIdElement,
    processSectionIdElement,
    processPageIdElement,
    processPageTextElements
]
def parseDataLine(
                data: Data,
                foldername: str,
                filename: str,
                lineNumber: int, lineText: str) -> None:
    
    if (filename != data.lastProcessedFilename):
        data.updateProcessingState(filename, None, None, None, None)
    
    success = False
    for p in processPipeline:
        success = p(data, foldername, filename, lineNumber, lineText)
        if success:
            break
    
    if (not success):
        print(f"Error: Cannot parse line#{lineNumber} in {filename}")
    
    return

