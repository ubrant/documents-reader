class Minor:
    def __init__(self) -> None:
        return

class Major:
    def __init__(self) -> None:
        return

class Data:
    def __init__(me) -> None:
        me.majors = []
        return
    
    def processTextLine(me,
                foldername: str,
                filename: str,
                lineNumber: int, line: str) -> None:
        print(f"{lineNumber}->{line}")
        return
    
    def sort(me):
        return me