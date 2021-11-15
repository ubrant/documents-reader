from datetime              import  datetime
from _internal.settings    import  Settings
from _internal.recursion   import  getDesiredFiles
from _internal.parser      import  Parser
from _internal.web         import  WebContentGenerator

# Time-stamp
startTime = datetime.now()

# Global Settings
settings = Settings()
settings.print(
    headingLine = "Settings:",
    indent = " > ",
    appendBlankLines = 1)

# Processing Files
print("Processing Files")
print("----------------")

parser = Parser()
for file in getDesiredFiles(settings, ".ubd"):
    print(f"Reading {file}")
    parser.loadFile(file)

# Generating Web Content
webGenerator = WebContentGenerator(settings, parser.getParsedData())
webGenerator.generateOutput()
webGenerator.openOutput()

# Time Elapsed
et = (datetime.now() - startTime).total_seconds()
print("...")
print(".....")
print(f"Completed")

if (et < 1.0):
    print(f"Total Run-time = {et*1000:0.2f}ms")
else:
    print(f"Total Run-time = {et:0.2f}sec")

print("")
