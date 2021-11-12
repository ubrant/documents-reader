from _internal.settings    import  *
from _internal.recursion   import  *
from _internal.parser      import  *
from _internal.web         import  *

# Global Settings
settings = Settings()
settings.print(
    headingLine = "Settings:",
    indent = " > ",
    appendBlankLines = 1)

# Processing files
print("Processing Files")
print("----------------")

for file in getDesiredFiles(settings, ".ubd"):
    print(f"Parsing {file}")

