from os                 import listdir
from os.path            import isfile
from os.path            import isdir
from os.path            import join

from _internal.settings import Settings


def getDirectories(directory, recursion = False, depth = 0):
    try:
        for name in listdir(directory):
            full_name = join(directory, name)
            if(isdir(full_name)):
                yield full_name

                if(recursion and depth > 0):
                    yield from getDirectories(full_name, recursion, depth - 1)
    except:
        return

def getFiles(directory, extension = ""):
    try:
        for name in listdir(directory):
            full_name = join(directory, name)
            if(isfile(full_name)):
                if (extension == None or extension == ""):
                    yield full_name
                else:
                    if(full_name.lower().endswith(extension.lower())):
                        yield full_name
    except:
        return f"<cannot access - {directory}>"

def getDesiredFiles(settings: Settings, extension):
    for dir in getDirectories(
                        settings.scanDir,
                        settings.isRecursive,
                        settings.recursionDepth):
        for full_filename in getFiles(dir, extension):
            yield full_filename