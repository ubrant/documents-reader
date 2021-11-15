class Page:
    def __init__(self) -> None:
        self.id = 0
        self.title = ""
        return

class Section:
    def __init__(self) -> None:
        self.id = 0
        self.title = ""
        self.pages = []
        return

    def sort(self):
        temp = []
        minId = 0
        maxId = 0

        # Finding Min and Max IDs
        for page in self.pages:
            if page.id < minId:
                minId = page.id
            if page.id > maxId:
                maxId = page.id

        # Sorting as per IDs
        for i in range(minId, maxId + 1):
            for p in self.pages:
                if p.id == i:
                    temp.append(p)

        # Replacing and returning
        self.pages = temp
        return self

class Minor:
    def __init__(self) -> None:
        self.id = 0
        self.title = ""
        self.sections = []
        return

    def sort(self):
        temp = []
        minId = 0
        maxId = 0

        # Finding Min and Max IDs
        for section in self.sections:
            if section.id < minId:
                minId = section.id
            if section.id > maxId:
                maxId = section.id

        # Sorting as per IDs
        for i in range(minId, maxId + 1):
            for s in self.sections:
                if s.id == i:
                    temp.append(s.sort())

        # Replacing and returning
        self.sections = temp
        return self

class Major:
    def __init__(self) -> None:
        self.id = 0
        self.title = ""
        self.minors = []
        return

    def sort(self):
        temp = []
        minId = 0
        maxId = 0

        # Finding Min and Max IDs
        for minor in self.minors:
            if minor.id < minId:
                minId = minor.id
            if minor.id > maxId:
                maxId = minor.id

        # Sorting as per IDs
        for i in range(minId, maxId + 1):
            for m in self.minors:
                if m.id == i:
                    temp.append(m.sort())

        # Replacing and returning
        self.minors = temp
        return self

class Data:
    def __init__(my) -> None:
        my.majors = []
        return
    
    def sort(me):
        temp = []
        minId = 0
        maxId = 0

        # Finding Min and Max IDs
        for major in me.majors:
            if major.id < minId:
                minId = major.id
            if major.id > maxId:
                maxId = major.id

        # Sorting as per IDs
        for i in range(minId, maxId + 1):
            for m in me.majors:
                if m.id == i:
                    temp.append(m.sort())

        # Replacing and returning
        me.majors = temp
        return me
