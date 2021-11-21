from typing import List

######
# Page Elements
####

# Section Element
class PageSection:
    def __init__(self) -> None:
        self.h1: str = ""
        self.h2: str = ""
        self.description: str = ""
        self.quote: str = ""
        self.quoteBy: str = ""
        self.background: str = ""
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
        self.text: str = ""
        self.append(text)
        return

    def append(self, text: str) -> str:
        if text == None or text == "": return ""

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
        self.textElements: List[TextElement] = []
        return

    def append(self, text: str) -> str:
        if text != "":
            self.textElements.append(TextElement(text))
        return ""

# Code
class PageCode:
    def __init__(self, language: str) -> None:
        self.language: str = language
        self.textElements: List[TextElement] = []
        self.tempTextElements: List[TextElement] = []
        return

    def append(self, textTrimmed: str, textFull: str) -> str:
        if textTrimmed == "":
            # Save blank lines if some code lines are already existing
            if len(self.textElements) > 0:
                self.tempTextElements.append(TextElement(textFull))
        else:
            for te in self.tempTextElements:
                self.textElements.append(te)
            self.tempTextElements.clear()
            self.textElements.append(TextElement(textFull))
        return ""

# Image
class PageImage:
    def __init__(self, caption: str, filename: str) -> None:
        self.caption: str = caption
        self.filename: str = filename
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
        self.id: int = 0
        self.title: str = ""
        self.section: PageSection = None
        self.elements = []
        self.lastElementIdentifier: int = Page.PAGE_LAST_ELEMENT_OTHER
        return

    def setTitleIfEmpty(self, title: str) -> bool:
        if (self.title == ""):
            self.title = title
            return True
        return False

    # Section
    def requirePageSection(self) -> PageSection:
        if self.section == None:
            self.section = PageSection()
        return self.section

    def addSectionH1(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_SECTION_H1
        return self.requirePageSection().append(text, None, None, None, None, None)
    def addSectionH2(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_SECTION_H2
        return self.requirePageSection().append(None, text, None, None, None, None)
    def addSectionDescription(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_SECTION_DESCRIPTION
        return self.requirePageSection().append(None, None, text, None, None, None)
    def addSectionQuote(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_SECTION_QUOTE
        return self.requirePageSection().append(None, None, None, text, None, None)
    def addSectionQuoteBy(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_SECTION_QUOTE_BY
        return self.requirePageSection().append(None, None, None, None, text, None)
    def addSectionBackground(self, filename: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_SECTION_BACKGROUND
        return self.requirePageSection().append(None, None, None, None, None, filename)

    # Headings
    def addH1(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        self.elements.append(PageHeading1(text))
        return ""
    def addH2(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        self.elements.append(PageHeading2(text))
        return ""
    def addH3(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        self.elements.append(PageHeading3(text))
        return ""
    def addH4(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        self.elements.append(PageHeading4(text))
        return ""
    def addH5(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        self.elements.append(PageHeading5(text))
        return ""
    def addH6(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        self.elements.append(PageHeading6(text))
        return ""

    # Para
    def addPara(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        self.elements.append(PagePara(text))
        return ""

    # List
    def addUnorderedList(self, text: str) -> str:
        tlist = PageUnorderedList()
        tlist.append(text)
        self.elements.append(tlist)
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        return ""

    # Code
    def addCode(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        self.elements.append(PageCode(text))
        return ""

    # Image
    def addImage(self, caption: str, filename: str) -> str:
        self.elements.append(PageImage(caption, filename))
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        return ""

    # Question
    def addQuestion(self) -> str:
        self.elements.append(PageQuestion())
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        return ""
    def addQuestionDifficulty(self, difficulty: int) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].difficulty = difficulty
        else:
            return "Cannot add difficulty level to any question"
        return ""
    def addQuestionText(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].text = text
        else:
            return "Cannot add text to any question"
        return ""
    def addQuestionOptA(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optA = text
        else:
            return "Cannot add Option A to any question"
        return ""
    def addQuestionOptB(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optB = text
        else:
            return "Cannot add Option B to any question"
        return ""
    def addQuestionOptC(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optC = text
        else:
            return "Cannot add Option C to any question"
        return ""
    def addQuestionOptD(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optD = text
        else:
            return "Cannot add Option D to any question"
        return ""
    def addQuestionOptE(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optE = text
        else:
            return "Cannot add Option E to any question"
        return ""
    def addQuestionOptF(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optF = text
        else:
            return "Cannot add Option F to any question"
        return ""
    def addQuestionOptG(self, text: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].optG = text
        else:
            return "Cannot add Option G to any question"
        return ""
    def addQuestionAttempts(self, attempts: int) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].attempts = attempts
        else:
            return "Cannot add attempts to any question"
        return ""
    def addQuestionAnswer(self, answer: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].answer = answer
        else:
            return "Cannot add answer to any question"
        return ""
    def addQuestionExplanation(self, explanation: str) -> str:
        self.lastElementIdentifier = Page.PAGE_LAST_ELEMENT_OTHER
        if len(self.elements) > 0 and type(self.elements[-1]) == PageQuestion:
            self.elements[-1].explanation = explanation
        else:
            return "Cannot add explanation to any question"
        return ""

    # Text without Tags
    def appendText(self, textTrimmed: str, textFull: str) -> str:
        if self.lastElementIdentifier == Page.PAGE_LAST_ELEMENT_SECTION_H1:
            return self.section.append(textTrimmed, None, None, None, None, None)
        elif self.lastElementIdentifier == Page.PAGE_LAST_ELEMENT_SECTION_H2:
            return self.section.append(None, textTrimmed, None, None, None, None)
        elif self.lastElementIdentifier == Page.PAGE_LAST_ELEMENT_SECTION_DESCRIPTION:
            return self.section.append(None, None, textTrimmed, None, None, None)
        elif self.lastElementIdentifier == Page.PAGE_LAST_ELEMENT_SECTION_QUOTE:
            return self.section.append(None, None, None, textTrimmed, None, None)
        elif self.lastElementIdentifier == Page.PAGE_LAST_ELEMENT_SECTION_QUOTE_BY:
            return self.section.append(None, None, None, None, textTrimmed, None)
        elif self.lastElementIdentifier == Page.PAGE_LAST_ELEMENT_SECTION_BACKGROUND:
            return self.section.append(None, None, None, None, None, textTrimmed)
        else:
            if len(self.elements) > 0:
                e = self.elements[-1]
                if type(e) == PageCode:
                    return e.append(textTrimmed, textFull)
                elif textTrimmed != "":
                    return e.append(textTrimmed)
            
            if textTrimmed != "":
                return "Cannot append text to any element"
            else:
                return ""

######
# Section Element
####
class Section:
    def __init__(self) -> None:
        self.id: int = 0
        self.title: str = ""
        self.pages: List[Page] = []
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

    def filterAndSort(self):
        temp: List[Page] = []
        minId: int = 0
        maxId: int = 0

        # Finding Min and Max IDs
        for page in self.pages:
            if page.id < minId:
                minId = page.id
            if page.id > maxId:
                maxId = page.id

        # Sorting as per IDs
        for i in range(minId, maxId + 1):
            for p in self.pages:
                if p.id >= 0 and p.id == i:
                    temp.append(p)

        # Replacing and returning
        self.pages = temp
        return self

######
# Minor Element
####
class Minor:
    def __init__(self) -> None:
        self.id: int = 0
        self.title: str = ""
        self.sections: List[Section] = []
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

    def filterAndSort(self):
        temp: List[Section] = []
        minId: int = 0
        maxId: int = 0

        # Finding Min and Max IDs
        for section in self.sections:
            if section.id < minId:
                minId = section.id
            if section.id > maxId:
                maxId = section.id

        # Sorting as per IDs
        for i in range(minId, maxId + 1):
            for s in self.sections:
                if s.id >= 0 and s.id == i:
                    temp.append(s.filterAndSort())

        # Replacing and returning
        self.sections = temp
        return self

######
# Major Element
####
class Major:
    def __init__(self) -> None:
        self.id: int = 0
        self.title: str = ""
        self.minors: List[Minor] = []
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

    def filterAndSort(self):
        temp: List[Minor] = []
        minId: int = 0
        maxId: int = 0

        # Finding Min and Max IDs
        for minor in self.minors:
            if minor.id < minId:
                minId = minor.id
            if minor.id > maxId:
                maxId = minor.id

        # Sorting as per IDs
        for i in range(minId, maxId + 1):
            for m in self.minors:
                if m.id >= 0 and m.id == i:
                    temp.append(m.filterAndSort())

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
    DEFAULT_MAJOR_ELEMENT_ID = -1
    DEFAULT_MINOR_ELEMENT_ID = -1
    DEFAULT_SECTION_ELEMENT_ID = -1
    DEFAULT_PAGE_ELEMENT_ID = -1
    
    def __init__(my) -> None:
        my.majors: List[Major] = []
        my.lastProcessedFilename: str = ""
        my.currentMajorElementId: int = Data.DEFAULT_MAJOR_ELEMENT_ID
        my.currentMinorElementId: int = Data.DEFAULT_MINOR_ELEMENT_ID
        my.currentSectionElementId: int = Data.DEFAULT_SECTION_ELEMENT_ID
        my.currentPageElementId: int = Data.DEFAULT_PAGE_ELEMENT_ID
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
        
        major: Major = Major()
        major.id = id
        my.majors.append(major)
        return major
    
    def getActivePage(my) -> Page:
        return (my.getOrAddNewMajorElementById(my.currentMajorElementId)
                  .getOrAddNewMinorElementById(my.currentMinorElementId)
                  .getOrAddNewSectionElementById(my.currentSectionElementId)
                  .getOrAddNewPageElementById(my.currentPageElementId))

    def filterAndSort(me):
        temp: List[Major] = []
        minId: int = 0
        maxId: int = 0

        # Finding Min and Max IDs
        for major in me.majors:
            if major.id < minId:
                minId = major.id
            if major.id > maxId:
                maxId = major.id

        # Sorting as per IDs
        for i in range(minId, maxId + 1):
            for m in me.majors:
                if m.id >= 0 and m.id == i:
                    temp.append(m.filterAndSort())

        # Replacing and returning
        me.majors = temp
        return me
