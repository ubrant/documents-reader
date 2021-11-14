from _internal.settings    import  Settings
from _internal.recursion   import  getDesiredFiles
from _internal.parser      import  Parser
from _internal.web         import  WebContentGenerator

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
