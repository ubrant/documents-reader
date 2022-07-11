from _internal.data_elements   import *

from os.path                   import isfile, join
from typing                    import Tuple, Type
from re                        import sub, search

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

def getImageCaptionAndFilename(string: str) -> Tuple[str, str]:
    #Format=>
    # Image: [caption ...](module-graph.png)
    s = search(".*\[(.*)\]\s*\((.*)\).*$", string)

    if s == None:
        return ("", "")

    caption = trimLR(trimMultipleSpaces(s.group(1)))
    imagename = trimLR(trimMultipleSpaces(s.group(2)))
    return (caption, imagename)

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
                lineNumber: int, uncommentedLineText: str, uncommentedLineTextTrimmed: str) -> bool:
    
    if uncommentedLineTextTrimmed == "": return False

    if (uncommentedLineText.lstrip().lower().startswith("@major")):
        idString, titleString = getSecondAndThirdRestOfString(uncommentedLineText)
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
                lineNumber: int, uncommentedLineText: str, uncommentedLineTextTrimmed: str) -> bool:
    
    if uncommentedLineTextTrimmed == "": return False
    
    if (uncommentedLineText.lstrip().lower().startswith("@minor")):
        idString, titleString = getSecondAndThirdRestOfString(uncommentedLineText)
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
                lineNumber: int, uncommentedLineText: str, uncommentedLineTextTrimmed: str) -> bool:
    
    if uncommentedLineTextTrimmed == "": return False
    
    if (uncommentedLineText.lstrip().lower().startswith("@section")):
        idString, titleString = getSecondAndThirdRestOfString(uncommentedLineText)
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
                lineNumber: int, uncommentedLineText: str, uncommentedLineTextTrimmed: str) -> bool:
    
    if uncommentedLineTextTrimmed == "": return False
    
    if (uncommentedLineText.lstrip().lower().startswith("@page")):
        idString, titleString = getSecondAndThirdRestOfString(uncommentedLineText)
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
                lineNumber: int, uncommentedLineText: str, uncommentedLineTextTrimmed: str) -> bool:
    
    page = data.getActivePage()
    trimmedLowercaseLine = uncommentedLineTextTrimmed.lower()
    
    errorMessage = ""

    isHandled = False

    if uncommentedLineTextTrimmed != "":
        secondHalfLine = getSecondRestOfString(uncommentedLineText)

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
            imageFilename = trimLR(secondHalfLine)
            if not isfile(imageFilename):
                tempFilename = join(foldername, imageFilename)
                if isfile(tempFilename):
                    errorMessage = page.addSectionBackground(tempFilename)
                else:
                    errorMessage = f"Cannot find image file {imageFilename}"
            else:
                errorMessage = page.addSectionBackground(imageFilename)
            
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

        # Code Tag
        if (isHandled == False and trimmedLowercaseLine.startswith("#code:")):
            errorMessage = page.addCode(secondHalfLine)
            isHandled = True

        # Console Tag
        if (isHandled == False and trimmedLowercaseLine.startswith("#console:")):
            errorMessage = page.addConsole(secondHalfLine)
            isHandled = True

        # Image Tag
        if (isHandled == False and trimmedLowercaseLine.startswith("#image:")):
            imageCaption, imageFilename = getImageCaptionAndFilename(uncommentedLineText)
            if (imageCaption == "" and imageFilename == ""):
                errorMessage = "Invalid Image Tag"
            else:
                if not isfile(imageFilename):
                    tempFilename = join(foldername, imageFilename)
                    if isfile(tempFilename):
                        errorMessage = page.addImage(imageCaption, tempFilename)
                    else:
                        errorMessage = f"Cannot find image file {imageFilename}"
                else:
                    errorMessage = page.addImage(imageCaption, imageFilename)
            isHandled = True
        
        # Question Tags
        if (isHandled == False and trimmedLowercaseLine.startswith("@question")):
            errorMessage = page.addQuestion()
            isHandled = True

        if (isHandled == False and trimmedLowercaseLine.startswith("#difficulty:")):
            difficulty = PageQuestion.DIFFICULTY_EASY
            ds = secondHalfLine.lower()
            
            if ds == "medium":
                difficulty = PageQuestion.DIFFICULTY_MEDIUM
            elif ds == "hard":
                difficulty = PageQuestion.DIFFICULTY_HARD
            
            errorMessage = page.addQuestionDifficulty(difficulty)
            isHandled = True

        if (isHandled == False and trimmedLowercaseLine.startswith("#text:")):
            errorMessage = page.addQuestionText(secondHalfLine)
            isHandled = True

        if (isHandled == False and trimmedLowercaseLine.startswith("#opta:")):
            errorMessage = page.addQuestionOptA(secondHalfLine)
            isHandled = True

        if (isHandled == False and trimmedLowercaseLine.startswith("#optb:")):
            errorMessage = page.addQuestionOptB(secondHalfLine)
            isHandled = True

        if (isHandled == False and trimmedLowercaseLine.startswith("#optc:")):
            errorMessage = page.addQuestionOptC(secondHalfLine)
            isHandled = True

        if (isHandled == False and trimmedLowercaseLine.startswith("#optd:")):
            errorMessage = page.addQuestionOptD(secondHalfLine)
            isHandled = True

        if (isHandled == False and trimmedLowercaseLine.startswith("#opte:")):
            errorMessage = page.addQuestionOptE(secondHalfLine)
            isHandled = True

        if (isHandled == False and trimmedLowercaseLine.startswith("#optf:")):
            errorMessage = page.addQuestionOptF(secondHalfLine)
            isHandled = True

        if (isHandled == False and trimmedLowercaseLine.startswith("#optg:")):
            errorMessage = page.addQuestionOptG(secondHalfLine)
            isHandled = True

        if (isHandled == False and trimmedLowercaseLine.startswith("#attempts:")):
            na = 0
            try:
                na = int(secondHalfLine)
                errorMessage = page.addQuestionAttempts(secondHalfLine)
            except:
                errorMessage = "Invalid number of attempts"
            isHandled = True

        if (isHandled == False and trimmedLowercaseLine.startswith("#answer:")):
            errorMessage = page.addQuestionAnswer(secondHalfLine)
            isHandled = True

        if (isHandled == False and trimmedLowercaseLine.startswith("#explanation:")):
            errorMessage = page.addQuestionExplanation(secondHalfLine)
            isHandled = True

    ## Have we handled it ...?
    internalErrorPattern = "    Error:{} in {} at line#{}"
    if (isHandled == True):
        if (errorMessage != None and errorMessage != ""):
            print(internalErrorPattern.format(errorMessage, filename, lineNumber))
        
        return True
    else:
        errorMessage = page.appendText(uncommentedLineTextTrimmed, uncommentedLineText)
        if (errorMessage != None and errorMessage != ""):
            print(internalErrorPattern.format(errorMessage, filename, lineNumber))
        else:
            return True
    
    return False

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

def parseUncommentedLine(
                data: Data,
                foldername: str,
                filename: str,
                lineNumber: int, uncommentedLineText: str) -> None:
    
    if (filename != data.lastProcessedFilename):
        data.updateProcessingState(filename, None, None, None, None)
    
    success = False
    for p in processPipeline:
        success = p(data, foldername, filename, lineNumber, uncommentedLineText, trimLR(uncommentedLineText))
        if success:
            break
    
    if (not success and trimLR(uncommentedLineText) != ""):
        print(f"Error: Cannot parse line#{lineNumber} in {filename}")
    
    return

