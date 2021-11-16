######
# Page Elements
####
class PageItemId:
    PAGE_ELEMENT_NONE                  = 0

    # Section Element
    PAGE_ELEMENT_SECTION_H1            = 1
    PAGE_ELEMENT_SECTION_H2            = 2
    PAGE_ELEMENT_SECTION_DESCRIPTION   = 3
    PAGE_ELEMENT_SECTION_QUOTE         = 4
    PAGE_ELEMENT_SECTION_QUOTE_BY      = 5
    PAGE_ELEMENT_SECTION_BACKGROUND    = 6
    
    # Headings
    PAGE_ELEMENT_H1                    = 11
    PAGE_ELEMENT_H2                    = 12
    PAGE_ELEMENT_H3                    = 13
    PAGE_ELEMENT_H4                    = 14
    PAGE_ELEMENT_H5                    = 15
    PAGE_ELEMENT_H6                    = 16
    
    # Para
    PAGE_ELEMENT_PARA                  = 21
    
    # Unordered List
    PAGE_ELEMENT_UNORDERED_LIST        = 31
    
    # Image
    PAGE_ELEMENT_IMAGE                 = 41
    
    # Styling
    PAGE_ELEMENT_BEGIN_BOLD            = 61
    PAGE_ELEMENT_END_BOLD              = 62
    PAGE_ELEMENT_BEGIN_ITALIC          = 63
    PAGE_ELEMENT_END_ITALIC            = 64
    
    # Linking
    PAGE_ELEMENT_LINK_URL              = 71
    PAGE_ELEMENT_LINK_DOCUMENTATION    = 72

class Page:
    def __init__(self) -> None:
        self.id = 0
        self.title = ""
        return

    def setTitleIfEmpty(self, title: str) -> bool:
        if (self.title == ""):
            self.title = title
            return True
        return False

    # Section
    def addSectionH1(self, text: str) -> str:
        return ""
    def addSectionH2(self, text: str) -> str:
        return ""
    def addSectionDescription(self, text: str) -> str:
        return ""
    def addSectionQuote(self, text: str) -> str:
        return ""
    def addSectionQuoteBy(self, text: str) -> str:
        return ""
    def addSectionBackground(self, filename: str) -> str:
        return ""

    # Headings
    def addH1(self, text: str) -> str:
        return ""
    def addH2(self, text: str) -> str:
        return ""
    def addH3(self, text: str) -> str:
        return ""
    def addH4(self, text: str) -> str:
        return ""
    def addH5(self, text: str) -> str:
        return ""
    def addH6(self, text: str) -> str:
        return ""

    # Para
    def addPara(self, text: str) -> str:
        return ""

    # List
    def addUnorderedList(self, text: str) -> str:
        return ""

    # Image
    def addImage(self, caption: str, filename: str) -> str:
        return ""

    # Text without Tags
    def appendText(self, text: str) -> str:
        return ""

######
# Section Element
####
class Section:
    def __init__(self) -> None:
        self.id = 0
        self.title = ""
        self.pages = []
        return

    def getOrAddNewPageElementById(self, id: int) -> Page:
        for page in self.pages:
            if (page.id == id):
                return page
        
        page = Page()
        page.id = id
        self.pages.append(page)
        return page

    def setTitleIfEmpty(self, title: str) -> bool:
        if (self.title == ""):
            self.title = title
            return True
        return False

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

######
# Minor Element
####
class Minor:
    def __init__(self) -> None:
        self.id = 0
        self.title = ""
        self.sections = []
        return

    def getOrAddNewSectionElementById(self, id: int) -> Section:
        for section in self.sections:
            if (section.id == id):
                return section
        
        section = Section()
        section.id = id
        self.sections.append(section)
        return section

    def setTitleIfEmpty(self, title: str) -> bool:
        if (self.title == ""):
            self.title = title
            return True
        return False

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

######
# Major Element
####
class Major:
    def __init__(self) -> None:
        self.id = 0
        self.title = ""
        self.minors = []
        return

    def getOrAddNewMinorElementById(self, id: int) -> Minor:
        for minor in self.minors:
            if (minor.id == id):
                return minor
        
        minor = Minor()
        minor.id = id
        self.minors.append(minor)
        return minor

    def setTitleIfEmpty(self, title: str) -> bool:
        if (self.title == ""):
            self.title = title
            return True
        return False

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

######
# Combined Data
# -------------
# 
# - Data is segregated into Major partitions
####
class Data:
    DEFAULT_MAJOR_ELEMENT_ID = 0
    DEFAULT_MINOR_ELEMENT_ID = 0
    DEFAULT_SECTION_ELEMENT_ID = 0
    DEFAULT_PAGE_ELEMENT_ID = 0
    
    def __init__(my) -> None:
        my.majors = []
        my.lastProcessedFilename = ""
        my.currentMajorElementId = Data.DEFAULT_MAJOR_ELEMENT_ID
        my.currentMinorElementId = Data.DEFAULT_MINOR_ELEMENT_ID
        my.currentSectionElementId = Data.DEFAULT_SECTION_ELEMENT_ID
        my.currentPageElementId = Data.DEFAULT_PAGE_ELEMENT_ID
        return

    def updateProcessingState(my,
                    updateFilename: str = None,
                    updateMajorElementId: int = None,
                    updateMinorElementId: int = None,
                    updateSectionElementId: int = None,
                    updatePageElementId: int = None) -> None:
        
        if (updateFilename != None and
            my.lastProcessedFilename != updateFilename):
            my.lastProcessedFilename = updateFilename
            my.currentMajorElementId = Data.DEFAULT_MAJOR_ELEMENT_ID
            my.currentMinorElementId = Data.DEFAULT_MINOR_ELEMENT_ID
            my.currentSectionElementId = Data.DEFAULT_SECTION_ELEMENT_ID
            my.currentPageElementId = Data.DEFAULT_PAGE_ELEMENT_ID
        
        if (updateMajorElementId != None):
            my.currentMajorElementId = updateMajorElementId
            my.currentMinorElementId = Data.DEFAULT_MINOR_ELEMENT_ID
            my.currentSectionElementId = Data.DEFAULT_SECTION_ELEMENT_ID
            my.currentPageElementId = Data.DEFAULT_PAGE_ELEMENT_ID

        if (updateMinorElementId != None):
            my.currentMinorElementId = updateMinorElementId
            my.currentSectionElementId = Data.DEFAULT_SECTION_ELEMENT_ID
            my.currentPageElementId = Data.DEFAULT_PAGE_ELEMENT_ID

        if (updateSectionElementId != None):
            my.currentSectionElementId = updateSectionElementId
            my.currentPageElementId = Data.DEFAULT_PAGE_ELEMENT_ID

        if (updatePageElementId != None):
            my.currentPageElementId = updatePageElementId
        
        return

    def resetProcessingState(my) -> None:
        my.lastProcessedFilename = ""
        my.currentMajorElementId = Data.DEFAULT_MAJOR_ELEMENT_ID
        my.currentMinorElementId = Data.DEFAULT_MINOR_ELEMENT_ID
        my.currentSectionElementId = Data.DEFAULT_SECTION_ELEMENT_ID
        my.currentPageElementId = Data.DEFAULT_PAGE_ELEMENT_ID
        return
    
    def getOrAddNewMajorElementById(my, id: int) -> Major:
        for major in my.majors:
            if (major.id == id):
                return major
        
        major = Major()
        major.id = id
        my.majors.append(major)
        return major
    
    def getActivePage(my) -> Page:
        return (my.getOrAddNewMajorElementById(my.currentMajorElementId)
                  .getOrAddNewMinorElementById(my.currentMinorElementId)
                  .getOrAddNewSectionElementById(my.currentSectionElementId)
                  .getOrAddNewPageElementById(my.currentPageElementId))

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
