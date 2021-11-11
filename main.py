from _internal.args        import  *
from _internal.recursion   import  *
from _internal.parser      import  *
from _internal.web         import  *

# Getting the command-line arguments
print("Parameters:")
arguments = Arguments()
arguments.print("    ")

# Processing desired files
print("")
print("Processing Files")
for file in getDesiredFiles(arguments, ".ubd"):
    print(f"    Processing: {file}")

