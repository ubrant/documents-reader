######
# Page Elements
####

# Section Element
class PageSection:
    def __init__(self) -> None:
        self.h1 = ""
        self.h2 = ""
        self.description = ""
        self.quote = ""
        self.quoteBy = ""
        self.background = ""
        return

    def append(self, h1: str = None, h2: str = None,
                     description: str = None,
                     quote: str = None, quoteBy: str = None,
                     background: str = None) -> str:
        
        if h1 != None and h1 != "":
            if self.h1 == "":
                self.h1 = h1
            else:
                return f"Page-section's H1 is already set to {self.h1}"
        
        if h2 != None and h2 != "":
            if self.h2 == "":
                self.h2 = h2
            else:
                return f"Page-section's H2 is already set to {self.h2}"
        
        if description != None and description != "":
            if self.description == "":
                self.description = description
            else:
                return f"Page-section's description is already set to {self.description}"
        
        if quote != None and quote != "":
            if self.quote == "":
                self.quote = quote
            else:
                return f"Page-section's quote is already set to {self.quote}"
        
        if quoteBy != None and quoteBy != "":
            if self.quoteBy == "":
                self.quoteBy = quoteBy
            else:
                return f"Page-section's quote by is already set to {self.quoteBy}"
        
        if background != None and background != "":
            if self.background == "":
                self.background = background
            else:
                return f"Page-section's background is already set to {self.background}"
        
        return ""

# Base for Text
class TextElement:
    def __init__(self, text: str) -> None:
        self.text = ""
        self.append(text)
        return

    def append(self, text: str) -> str:
        if self.text == "":
            self.text = text
        else:
            self.text = self.text + " " + text
        return ""

# Headings
class PageHeading1(TextElement):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        return

class PageHeading2(TextElement):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        return

class PageHeading3(TextElement):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        return

class PageHeading4(TextElement):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        return

class PageHeading5(TextElement):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        return

class PageHeading6(TextElement):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        return

# Para
class PagePara(TextElement):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        return

# List
class PageUnorderedList:
    def __init__(self) -> None:
        self.textElements = []
        return

    def append(self, text: str) -> str:
        if text != "":
            self.textElements.append(TextElement(text))
        return ""

# Image
class PageImage:
    def __init__(self, caption: str, filename: str) -> None:
        self.caption = caption
        self.filename = filename
        return

    def append(self, text: str) -> str:
        return "Cannot append text to an image"

# Question
class PageQuestion:
    DIFFICULTY_EASY   = 1
    DIFFICULTY_MEDIUM = 2
    DIFFICULTY_HARD   = 3

    def __init__(self) -> None:
        self.difficulty: int = None
        self.text: str = None
        self.optA: str = None
        self.optB: str = None
        self.optC: str = None
        self.optD: str = None
        self.optE: str = None
        self.optF: str = None
        self.optG: str = None
        self.attempts: int = None
        self.answer: str = None
        self.explanation: str = None
        return

    def append(self, text: str) -> str:
        return "Cannot append text to a question"

## Page itself
class Page:
    PAGE_LAST_ELEMENT_OTHER                 = 0
    PAGE_LAST_ELEMENT_SECTION_H1            = 1
    PAGE_LAST_ELEMENT_SECTION_H2            = 2
    PAGE_LAST_ELEMENT_SECTION_DESCRIPTION   = 3
    PAGE_LAST_ELEMENT_SECTION_QUOTE         = 4
    PAGE_LAST_ELEMENT_SECTION_QUOTE_BY      = 5
    PAGE_LAST_ELEMENT_SECTION_BACKGROUND    = 6

    def __init__(self) -> None:
        self.id = 0
        self.title = ""
        self.section = None
        self.elements = []
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return

    def setTitleIfEmpty(self, title: str) -> bool:
        if (self.title == ""):
            self.title = title
            return True
        return False

    # Section
    def addSectionH1(self, text: str) -> str:
        self.lastElement = Page.PAGE_LAST_ELEMENT_SECTION_H1
        if self.section == None:
            self.section = PageSection()
        return self.section.append(text, None, None, None, None, None)
    def addSectionH2(self, text: str) -> str:
        self.lastElement = Page.PAGE_LAST_ELEMENT_SECTION_H2
        if self.section == None:
            self.section = PageSection()
        return self.section.append(None, text, None, None, None, None)
    def addSectionDescription(self, text: str) -> str:
        self.lastElement = Page.PAGE_LAST_ELEMENT_SECTION_DESCRIPTION
        if self.section == None:
            self.section = PageSection()
        return self.section.append(None, None, text, None, None, None)
    def addSectionQuote(self, text: str) -> str:
        self.lastElement = Page.PAGE_LAST_ELEMENT_SECTION_QUOTE
        if self.section == None:
            self.section = PageSection()
        return self.section.append(None, None, None, text, None, None)
    def addSectionQuoteBy(self, text: str) -> str:
        self.lastElement = Page.PAGE_LAST_ELEMENT_SECTION_QUOTE_BY
        if self.section == None:
            self.section = PageSection()
        return self.section.append(None, None, None, None, text, None)
    def addSectionBackground(self, filename: str) -> str:
        self.lastElement = Page.PAGE_LAST_ELEMENT_SECTION_BACKGROUND
        if self.section == None:
            self.section = PageSection()
        return self.section.append(None, None, None, None, None, filename)

    # Headings
    def addH1(self, text: str) -> str:
        self.elements.append(PageHeading1(text))
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addH2(self, text: str) -> str:
        self.elements.append(PageHeading2(text))
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addH3(self, text: str) -> str:
        self.elements.append(PageHeading3(text))
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addH4(self, text: str) -> str:
        self.elements.append(PageHeading4(text))
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addH5(self, text: str) -> str:
        self.elements.append(PageHeading5(text))
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addH6(self, text: str) -> str:
        self.elements.append(PageHeading6(text))
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""

    # Para
    def addPara(self, text: str) -> str:
        self.elements.append(PagePara(text))
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""

    # List
    def addUnorderedList(self, text: str) -> str:
        tlist = PageUnorderedList()
        tlist.append(text)
        self.elements.append(tlist)
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""

    # Image
    def addImage(self, caption: str, filename: str) -> str:
        self.elements.append(PageImage(caption, filename))
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""

    # Question
    def addQuestion(self) -> str:
        self.elements.append(PageQuestion())
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addQuestionDifficulty(self, difficulty: int) -> str:
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].difficulty = difficulty
        else:
            return "Cannot add difficulty level to any question"
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addQuestionText(self, text: str) -> str:
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].text = text
        else:
            return "Cannot add text to any question"
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addQuestionOptA(self, text: str) -> str:
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optA = text
        else:
            return "Cannot add Option A to any question"
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addQuestionOptB(self, text: str) -> str:
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optB = text
        else:
            return "Cannot add Option B to any question"
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addQuestionOptC(self, text: str) -> str:
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optC = text
        else:
            return "Cannot add Option C to any question"
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addQuestionOptD(self, text: str) -> str:
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optD = text
        else:
            return "Cannot add Option D to any question"
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addQuestionOptE(self, text: str) -> str:
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optE = text
        else:
            return "Cannot add Option E to any question"
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addQuestionOptF(self, text: str) -> str:
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optF = text
        else:
            return "Cannot add Option F to any question"
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addQuestionOptG(self, text: str) -> str:
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optG = text
        else:
            return "Cannot add Option G to any question"
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addQuestionAttempts(self, attempts: int) -> str:
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].attempts = attempts
        else:
            return "Cannot add attempts to any question"
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addQuestionAnswer(self, answer: str) -> str:
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].answer = answer
        else:
            return "Cannot add answer to any question"
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addQuestionExplanation(self, explanation: str) -> str:
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].explanation = explanation
        else:
            return "Cannot add explanation to any question"
        self.lastElement = Page.PAGE_LAST_ELEMENT_OTHER
        return ""

    # Text without Tags
    def appendText(self, text: str) -> str:
        if self.lastElement == Page.PAGE_LAST_ELEMENT_SECTION_H1:
            return self.section.append(text, None, None, None, None, None)
        elif self.lastElement == Page.PAGE_LAST_ELEMENT_SECTION_H2:
            return self.section.append(None, text, None, None, None, None)
        elif self.lastElement == Page.PAGE_LAST_ELEMENT_SECTION_DESCRIPTION:
            return self.section.append(None, None, text, None, None, None)
        elif self.lastElement == Page.PAGE_LAST_ELEMENT_SECTION_QUOTE:
            return self.section.append(None, None, None, text, None, None)
        elif self.lastElement == Page.PAGE_LAST_ELEMENT_SECTION_QUOTE_BY:
            return self.section.append(None, None, None, None, text, None)
        elif self.lastElement == Page.PAGE_LAST_ELEMENT_SECTION_BACKGROUND:
            return self.section.append(None, None, None, None, None, text)
        else:
            if len(self.elements) > 0:
                return self.elements[-1].append(text)
            return "Cannot append text to any element"

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
