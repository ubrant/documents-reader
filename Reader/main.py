# *****************************************************************************************
# * Purpose:
# *     Entry-point for the application
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

from datetime              import  datetime, timedelta
from os.path               import  isfile

from _internal.settings    import  Settings
from _internal.recursion   import  getDesiredFiles
from _internal.parser      import  Parser
from _internal.web         import  WebContentGenerator


# ***********
# Loading Settings
# ********

# Time-stamp - Start
tsStart = datetime.now()

# Global Settings
print("Loading Settings")
print("----------------")

settings = Settings()
settings.print(
    headingLine = "Settings:",
    indent = " > ",
    appendBlankLines = 1)

# Checking availability of templates
def checkTemplateFileAvailability(filename: str) -> None:
    if not isfile(filename):
        print(f"Error: Template File Missing ({filename})")
        print("Cannot continue to process ...")
        exit(1)
    return

checkTemplateFileAvailability(settings.templateContentHeading1File)
checkTemplateFileAvailability(settings.templateContentHeading2File)
checkTemplateFileAvailability(settings.templateContentHeading3File)
checkTemplateFileAvailability(settings.templateContentHeading4File)
checkTemplateFileAvailability(settings.templateContentHeading5File)
checkTemplateFileAvailability(settings.templateContentHeading6File)
checkTemplateFileAvailability(settings.templateContentImageFile)
checkTemplateFileAvailability(settings.templateContentCodeFile)
checkTemplateFileAvailability(settings.templateContentConsoleFile)
checkTemplateFileAvailability(settings.templateContentListUnorderedFile)
checkTemplateFileAvailability(settings.templateContentListUnorderedItemFile)
checkTemplateFileAvailability(settings.templateContentParaFile)
checkTemplateFileAvailability(settings.templateContentQuestionFile)
checkTemplateFileAvailability(settings.templateContentSectionFile)
checkTemplateFileAvailability(settings.templateSideMajorItemFile)
checkTemplateFileAvailability(settings.templateSideMinorItemFile)
checkTemplateFileAvailability(settings.templateSideSectionItemFile)
checkTemplateFileAvailability(settings.templateSidePageItemFile)
checkTemplateFileAvailability(settings.templateSiteFile)

# ***********
# Loading Files
# ********

# Time-stamp - Start Processing Files
tsStartProcessingFiles = datetime.now()

# Processing Files
print("Processing Files")
print("----------------")

numFilesLoaded: int = 0
parser = Parser()
for file in getDesiredFiles(settings, ".ubd"):
    print(f"Reading {file}")
    parser.loadFile(file)
    numFilesLoaded += 1

print("")

if numFilesLoaded == 0:
    print("No ubd file found ...")
    exit(0)

# ***********
# Writing Files
# ********

# Time-stamp - Start Writing Web Content
tsStartWritingWebContent = datetime.now()

# Generating Web Content
print("Generating Web Content")
print("----------------------")

webGenerator = WebContentGenerator(settings, parser.getParsedAndFilteredData())
webGenerator.generateOutput()
webGenerator.openOutput()

print("")

# ***********
# End
# ********

# Time-stamp - End
tsEnd = datetime.now()

def printElapsedTime(indent: str, parameter: str, dt: timedelta, compact = False):
    messageFormat = "{}{} = {:8.3f} {}"
    if compact == True:
        messageFormat = "{}{} = {:.3f} {}"

    value = dt.total_seconds()
    unit = "sec"
    
    if (value < 1.0):
        value = value * 1000
        unit = "msec"
    
    print(messageFormat.format(indent, parameter, value, unit))

print("")
print("Completed")
print("---------")

print("Phase-wise elapsed time:")
printElapsedTime(" > ", "Loading Settings", tsStartProcessingFiles - tsStart)
printElapsedTime(" > ", "Loading Files   ", tsStartWritingWebContent - tsStartProcessingFiles)
printElapsedTime(" > ", "Writing Files   ", tsEnd - tsStartWritingWebContent)
print("")
printElapsedTime(" > ", "Total", tsEnd - tsStart, compact = True)

print("")
