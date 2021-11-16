from _internal.data_elements   import *

from typing                    import Tuple, Type
from re                        import sub

######
# File Reading
####
def readFileWithLineNumbers(filename: str) -> Tuple[int, str]:
    f = open(filename, "rU", 8192, "utf-8-sig")
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

    internalErrorPattern = "    Error:{} in {} at line#{}"
    errorMessage = ""

    isHandled = False

    # Section Tags
    if (isHandled == False and trimmedLowercaseLine.startswith("$h1:")):
        errorMessage = page.addSectionH1(secondHalfLine)
        isHandled = True

    if (isHandled == False and trimmedLowercaseLine.startswith("$h2:")):
        errorMessage = page.addSectionH2(secondHalfLine)
        isHandled = True

    if (isHandled == False and trimmedLowercaseLine.startswith("$dt:")):
        errorMessage = page.addSectionDescription(secondHalfLine)
        isHandled = True

    if (isHandled == False and trimmedLowercaseLine.startswith("$qt:")):
        errorMessage = page.addSectionQuote(secondHalfLine)
        isHandled = True

    if (isHandled == False and trimmedLowercaseLine.startswith("$qb:")):
        errorMessage = page.addSectionQuoteBy(secondHalfLine)
        isHandled = True

    if (isHandled == False and trimmedLowercaseLine.startswith("$bg:")):
        errorMessage = page.addSectionBackground(secondHalfLine)
        isHandled = True

    # Heading Tags
    if (isHandled == False and trimmedLowercaseLine.startswith("#h1:")):
        errorMessage = page.addH1(secondHalfLine)
        isHandled = True

    if (isHandled == False and trimmedLowercaseLine.startswith("#h2:")):
        errorMessage = page.addH2(secondHalfLine)
        isHandled = True

    if (isHandled == False and trimmedLowercaseLine.startswith("#h3:")):
        errorMessage = page.addH3(secondHalfLine)
        isHandled = True

    if (isHandled == False and trimmedLowercaseLine.startswith("#h4:")):
        errorMessage = page.addH4(secondHalfLine)
        isHandled = True

    if (isHandled == False and trimmedLowercaseLine.startswith("#h5:")):
        errorMessage = page.addH5(secondHalfLine)
        isHandled = True

    if (isHandled == False and trimmedLowercaseLine.startswith("#h6:")):
        errorMessage = page.addH6(secondHalfLine)
        isHandled = True

    # Paragraph Tag
    if (isHandled == False and trimmedLowercaseLine.startswith("#para:")):
        errorMessage = page.addPara(secondHalfLine)
        isHandled = True

    # List Tag
    if (isHandled == False and trimmedLowercaseLine.startswith("#list:")):
        errorMessage = page.addUnorderedList(secondHalfLine)
        isHandled = True

    # Image Tag
    if (isHandled == False and trimmedLowercaseLine.startswith("#image:")):
        errorMessage = page.addUnorderedList(secondHalfLine)
        isHandled = True
    
    ## Have we handled it ...?
    if (isHandled == True):
        if (errorMessage != None and errorMessage != ""):
            print(internalErrorPattern.format(errorMessage, filename, lineNumber))
        
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

