from _internal.args        import  *
from _internal.recursion   import  *
from _internal.parser      import  *
from _internal.web         import  *

# Getting the command-line arguments
arguments = Arguments()
arguments.print(
    headingLine = "Using parameters for processing:",
    indent = " > ",
    appendBlankLines = 1)

# Processing files
print("Processing Files")
print("----------------")

for file in getDesiredFiles(arguments, ".ubd"):
    print(f"Parsing {file}")

