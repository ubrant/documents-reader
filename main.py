from datetime              import  datetime, timedelta

from _internal.settings    import  Settings
from _internal.recursion   import  getDesiredFiles
from _internal.parser      import  Parser
from _internal.web         import  WebContentGenerator


######
# Loading Settings
####

# Time-stamp - Start
tsStart = datetime.now()

# Global Settings
settings = Settings()
settings.print(
    headingLine = "Settings:",
    indent = " > ",
    appendBlankLines = 1)


######
# Loading Files
####

# Time-stamp - Start Processing Files
tsStartProcessingFiles = datetime.now()

# Processing Files
print("Processing Files")
print("----------------")

parser = Parser()
for file in getDesiredFiles(settings, ".ubd"):
    print(f"Reading {file}")
    parser.loadFile(file)


######
# Writing Files
####

# Time-stamp - Start Writing Web Content
tsStartWritingWebContent = datetime.now()

# Generating Web Content
webGenerator = WebContentGenerator(settings, parser.getParsedData())
webGenerator.generateOutput()
webGenerator.openOutput()


######
# End
####

# Time-stamp - End
tsEnd = datetime.now()

def printElapsedTime(indent: str, parameter: str, dt: timedelta):
    messageFormat = "{}{} = {:7.3f} {}"

    value = dt.total_seconds()
    unit = "sec"
    
    if (value < 1.0):
        value = value * 1000
        unit = "msec"
    
    print(messageFormat.format(indent, parameter, value, unit))

print("")
print(".")
print("...")
print("Completed")

print("")
print("Times taken:")
printElapsedTime("  > ", "Loading Settings", tsStartProcessingFiles - tsStart)
printElapsedTime("  > ", "Loading Files   ", tsStartWritingWebContent - tsStartProcessingFiles)
printElapsedTime("  > ", "Writing Files   ", tsEnd - tsStartWritingWebContent)
print("")
printElapsedTime("  > ", "Total", tsEnd - tsStart)

print("")
