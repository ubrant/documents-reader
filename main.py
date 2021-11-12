from _internal.args        import  *
from _internal.recursion   import  *
from _internal.parser      import  *
from _internal.web         import  *

# Getting the command-line arguments
arguments = Arguments()
arguments.print(
    headingLine = "Using parameters for processing:",
    indent = "  > ",
    appendBlankLines = 2)

# Processing desired files
print("Processing Files")
print("----------------")
for file in getDesiredFiles(arguments, ".ubd"):
    print(f"    Processing: {file}")

