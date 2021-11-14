from re import sub

def getFolderFromFileName(filename: str) -> str:
    tmp = sub("/[^/]*$", "", filename)
    return sub("\\\\[^\\\\]*$", "", tmp)

def readFileWithLineNumbers(filename: str) -> (int, str):
    f = open(filename)
    ln = 0
    for line in f:
        ln += 1
        yield (ln, sub("\r", "", sub("\n", "", line)))

    f.close()
    return
