from _internal.args        import  *
from _internal.recursion   import  *
from _internal.parser      import  *
from _internal.web         import  *

# Getting the command-line arguments
arguments = Arguments()
arguments.print()

# Recursing directories
for dir in getDirectories(
                    arguments.directoryPath,
                    arguments.isRecursive,
                    arguments.recursionDepth):
    print(f"Scanning: {dir}")

    for file in getFiles(dir, ".ubd"):
        print(f"    {file}")

