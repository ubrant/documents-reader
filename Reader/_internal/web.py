from _internal.settings       import Settings
from _internal.data_elements  import *

from os                       import mkdir
from os.path                  import isdir, exists, join
from re                       import findall, sub, search

import webbrowser

######
# Helpers
####
def ensureDir(dirname: str) -> bool:
    if exists(dirname):
        if isdir(dirname):
            return True
        else:
            print(f"Error: {dirname} exists but it is not a directory")
    else:
        mkdir(dirname)
        if isdir(dirname):
            return True
    return False

def loadFileText(indent: str, filename: str):
    print(f"{indent}{filename}")
    f = open(filename)
    text = f.read()
    f.close()
    return text

def convertFilePathToURL(filename: str) -> str:
    return 'file://' + filename.replace("\\", "/")

def getOutputFilename(outputDir: str,
                      major: Major,
                      minor: Minor,
                      section: Section,
                      page: Page) -> str:
    
    return join(outputDir,
            f"P{major.id}.{minor.id}.{section.id}.{page.id}.html")
######
# Web Content Generator
####
class WebContentGenerator:
    def __init__(self, settings: Settings, data: Data) -> None:
        self.settings: Settings = settings
        self.data: Data = data
        self.firstWrittenFilename: str = None
        self.lastWrittenFilename: str = None

        self.templateContentHeading1: str = None
        self.templateContentHeading2: str = None
        self.templateContentHeading3: str = None
        self.templateContentHeading4: str = None
        self.templateContentHeading5: str = None
        self.templateContentHeading6: str = None
        self.templateContentImage: str = None
        self.templateContentLink: str = None
        self.templateContentListUnordered: str = None
        self.templateContentListUnorderedItem: str = None
        self.templateContentPara: str = None
        self.templateContentQuestion: str = None
        self.templateContentSection: str = None
        self.templateSideMajorItem: str = None
        self.templateSideMinorItem: str = None
        self.templateSideSectionItem: str = None
        self.templateSidePageItem: str = None
        self.templateSite: str = None

        self.loadTemplates()
        return

    def loadTemplates(self) -> None:
        print("Loading templates:")

        indent: str = " > "
        self.templateContentHeading1: str = loadFileText(indent, self.settings.templateContentHeading1File)
        self.templateContentHeading2: str = loadFileText(indent, self.settings.templateContentHeading2File)
        self.templateContentHeading3: str = loadFileText(indent, self.settings.templateContentHeading3File)
        self.templateContentHeading4: str = loadFileText(indent, self.settings.templateContentHeading4File)
        self.templateContentHeading5: str = loadFileText(indent, self.settings.templateContentHeading5File)
        self.templateContentHeading6: str = loadFileText(indent, self.settings.templateContentHeading6File)
        self.templateContentImage: str = loadFileText(indent, self.settings.templateContentImageFile)
        self.templateContentListUnordered: str = loadFileText(indent, self.settings.templateContentListUnorderedFile)
        self.templateContentListUnorderedItem: str = loadFileText(indent, self.settings.templateContentListUnorderedItemFile)
        self.templateContentPara: str = loadFileText(indent, self.settings.templateContentParaFile)
        self.templateContentQuestion: str = loadFileText(indent, self.settings.templateContentQuestionFile)
        self.templateContentSection: str = loadFileText(indent, self.settings.templateContentSectionFile)
        self.templateSideMajorItem: str = loadFileText(indent, self.settings.templateSideMajorItemFile)
        self.templateSideMinorItem: str = loadFileText(indent, self.settings.templateSideMinorItemFile)
        self.templateSideSectionItem: str = loadFileText(indent, self.settings.templateSideSectionItemFile)
        self.templateSidePageItem: str = loadFileText(indent, self.settings.templateSidePageItemFile)
        self.templateSite: str = loadFileText(indent, self.settings.templateSiteFile)

        return

    def getSelfAddressURL(self, majorId: int, minorId: int, sectionId: int, pageId: int) -> str:
        major = None
        minor = None
        section = None
        page = None

        for mj in self.data.majors:
            if major == None: major = mj
            if mj.id == majorId:
                major = mj
                break
        
        if major == None: return ""
        
        for mi in major.minors:
            if minor == None: minor = mi
            if mi.id == minorId:
                minor = mi
                break

        if minor == None: return ""
        
        for se in minor.sections:
            if section == None: section = se
            if se.id == sectionId:
                section = se
                break

        if section == None: return ""

        for pg in section.pages:
            if page == None: page = pg
            if pg.id == pageId:
                page = pg
                break
        
        if page == None: return ""
        return convertFilePathToURL(
            getOutputFilename(self.settings.outputDir, major, minor, section, page))

    def generateOutput(self) -> None:
        self.printHierarchy()
        self.lastWrittenFilename = ""

        if ensureDir(self.settings.outputDir):
            for major in self.data.majors:
                for minor in major.minors:
                    for section in minor.sections:
                        for page in section.pages:
                            self.writeHtmlPage(major, minor, section, page)
        return

    ###
    # HTML
    def writeHtmlPage(self, major: Major,
                            minor: Minor,
                            section: Section,
                            page: Page):
        
        self.lastWrittenFilename = getOutputFilename(self.settings.outputDir,
                                                     major, minor, section, page)

        if (self.firstWrittenFilename == None or self.firstWrittenFilename == ""):
            self.firstWrittenFilename = self.lastWrittenFilename
        
        f = open(self.lastWrittenFilename, "w")
        f.write(self.convertPageToHtml(major, minor, section, page))
        return

    ### Page to HTML
    def convertPageToHtml(self, major: Major,
                               minor: Minor,
                               section: Section,
                               page: Page) -> str:
        
        MajorID = f"{major.id}"
        MinorID = f"{minor.id}"
        SectionID = f"{section.id}"
        PageID = f"{page.id}"
        PageTitle = f"{page.title}"

        CSSBootstrapFileURL = convertFilePathToURL(self.settings.libCssBootstrapFile)
        CSSSiteStylesFileURL = convertFilePathToURL(self.settings.libCssSiteStylesFile)
        MajorListItems = self.getHtmlOfPageMajorItemsList()
        Content = self.getHtmlOfPageContent(page)
        JSjQueryFileURL = convertFilePathToURL(self.settings.libJsJQueryFile)
        JSBootstrapFileURL = convertFilePathToURL(self.settings.libJsBootstrapFile)
        JSSiteScriptFileURL = convertFilePathToURL(self.settings.libJsSiteScriptFile)
        
        return self.templateSite    \
                    .replace("@MajorID",              f"{MajorID}")                \
                    .replace("@MinorID",              f"{MinorID}")                \
                    .replace("@SectionID",            f"{SectionID}")              \
                    .replace("@PageID",               f"{PageID}")                 \
                    .replace("@PageTitle",            f"{PageTitle}")              \
                    .replace("@CSSBootstrapFileURL",  f"{CSSBootstrapFileURL}")    \
                    .replace("@CSSSiteStylesFileURL", f"{CSSSiteStylesFileURL}")   \
                    .replace("@MajorListItems",       f"{MajorListItems}")         \
                    .replace("@Content",              f"{Content}")                \
                    .replace("@JSjQueryFileURL",      f"{JSjQueryFileURL}")        \
                    .replace("@JSBootstrapFileURL",   f"{JSBootstrapFileURL}")     \
                    .replace("@JSSiteScriptFileURL",  f"{JSSiteScriptFileURL}")

    def getHtmlOfPageMajorItemsList(self) -> str:
        MajorListItems: str = ""
        for major in self.data.majors:
            MinorListItems = ""
            for minor in major.minors:

                SectionListItems = ""
                for section in minor.sections:
                    
                    PageListItems = ""
                    for page in section.pages:
                        PageListItems += \
                            self.templateSidePageItem   \
                                .replace("@MajorID", f"{major.id}")   \
                                .replace("@MinorID", f"{minor.id}")       \
                                .replace("@SectionID", f"{section.id}")  \
                                .replace("@PageID", f"{page.id}")  \
                                .replace("@PageName", page.title)  \
                                .replace("@PageURL",    \
                                    getOutputFilename(
                                        self.settings.outputDir,
                                        major, minor, section, page))
                    SectionListItems += \
                        self.templateSideSectionItem   \
                            .replace("@SectionID", f"{section.id}")  \
                            .replace("@SectionName", section.title)  \
                            .replace("@PageListItems", PageListItems)
                
                MinorListItems += \
                    self.templateSideMinorItem   \
                        .replace("@MinorID", f"{minor.id}")  \
                        .replace("@MinorName", minor.title)  \
                        .replace("@SectionListItems", SectionListItems)
            
            MajorListItems += \
                self.templateSideMajorItem   \
                    .replace("@MajorID", f"{major.id}")   \
                    .replace("@MajorName", major.title)   \
                    .replace("@MinorListItems", MinorListItems)
        
        return MajorListItems

    def getHtmlOfPageContent(self, page: Page) -> str:
        retHtml = self.getHtmlOfPageSection(page.section)
        for element in page.elements:
            retHtml += self.getHtmlOfPageElement(element)
        return retHtml

    def getHtmlOfPageSection(self, section: PageSection) -> str:
        if section == None: return ""

        H1Text = self.processSpecialTags(f"{section.h1}")
        H2Text = self.processSpecialTags(f"{section.h2}")
        ImageFile = convertFilePathToURL(section.background)
        DescriptionText = self.processSpecialTags(f"{section.description}")
        QuoteText = self.processSpecialTags(f"{section.quote}")
        QuoteByText = self.processSpecialTags(f"{section.quoteBy}")

        return self.templateContentSection \
                    .replace("@H1Text", H1Text)   \
                    .replace("@H2Text", H2Text)   \
                    .replace("@ImageFile", ImageFile)   \
                    .replace("@DescriptionText", DescriptionText)   \
                    .replace("@QuoteText", QuoteText)   \
                    .replace("@QuoteByText", QuoteByText)

    def getHtmlOfPageElement(self, element) -> str:
        # Headings
        if type(element) == PageHeading1:
            return self.templateContentHeading1 \
                        .replace("@HeadingText", self.processSpecialTags(element.text))
        if type(element) == PageHeading2:
            return self.templateContentHeading2 \
                        .replace("@HeadingText", self.processSpecialTags(element.text))
        if type(element) == PageHeading3:
            return self.templateContentHeading3 \
                        .replace("@HeadingText", self.processSpecialTags(element.text))
        if type(element) == PageHeading4:
            return self.templateContentHeading4 \
                        .replace("@HeadingText", self.processSpecialTags(element.text))
        if type(element) == PageHeading5:
            return self.templateContentHeading5 \
                        .replace("@HeadingText", self.processSpecialTags(element.text))
        if type(element) == PageHeading6:
            return self.templateContentHeading6 \
                        .replace("@HeadingText", self.processSpecialTags(element.text))
        
        # Para
        if type(element) == PagePara:
            return self.templateContentPara \
                        .replace("@ParaText", self.processSpecialTags(element.text))
        
        # List
        if type(element) == PageUnorderedList:
            ListItems = ""
            for li in element.textElements:
                ListItems += self.templateContentListUnorderedItem \
                    .replace("@ItemText", self.processSpecialTags(li.text))
            
            return self.templateContentListUnordered \
                                .replace("@ListItems", ListItems)
        
        # Image
        if type(element) == PageImage:
            return self.templateContentImage \
                        .replace("@ImageURL", convertFilePathToURL(element.filename))   \
                        .replace("@ImageCaption", self.processSpecialTags(element.caption))
        
        # Question
        if type(element) == PageQuestion:
            difficulty  = element.difficulty
            text        = self.processSpecialTags(element.text)
            attempts    = element.attempts
            answer      = self.processSpecialTags(element.answer)
            explanation = self.processSpecialTags(element.explanation)
            optA        = self.processSpecialTags(element.optA)
            optB        = self.processSpecialTags(element.optB)
            optC        = self.processSpecialTags(element.optC)
            optD        = self.processSpecialTags(element.optD)
            optE        = self.processSpecialTags(element.optE)
            optF        = self.processSpecialTags(element.optF)
            optG        = self.processSpecialTags(element.optG)

            if difficulty == None: difficulty = PageQuestion.DIFFICULTY_EASY
            if text == None: text = ""
            if attempts == None: attempts = 1
            if answer == None: answer = ""
            if explanation == None: explanation = ""
            if optA == None: optA = ""
            if optB == None: optB = ""
            if optC == None: optC = ""
            if optD == None: optD = ""
            if optE == None: optE = ""
            if optF == None: optF = ""
            if optG == None: optG = ""

            return self.templateContentQuestion \
                        .replace("@Difficulty", f"{difficulty}") \
                        .replace("@Text", text)                  \
                        .replace("@Attempts", f"{attempts}")     \
                        .replace("@Answer", answer)              \
                        .replace("@Explanation", explanation)    \
                        .replace("@OptA", optA)   \
                        .replace("@OptB", optB)   \
                        .replace("@OptC", optC)   \
                        .replace("@OptD", optD)   \
                        .replace("@OptE", optE)   \
                        .replace("@OptF", optF)   \
                        .replace("@OptG", optG)
        
        return ""

    def processSpecialTags(self, text: str) -> str:
        if text == None: return ""
        
        # :Link-URL:[TEXT][HINT](URL)
        # :Link-Site:[TEXT][HINT](Major-ID, Minor-ID, Section-ID, Page-ID)
        #   <a href="----" hint="----">----</a>
        text = sub('\:Link-URL\:\[(.*?)\]\[(.*?)\]\((.*?)\)', '<a href="\\3" class="link" title="\\2">\\1</a>', text)
        text = sub('\:Link-URL\:\[(.*?)\]\((.*?)\)',          '<a href="\\2" class="link" title="\\1">\\1</a>', text)
        while True:
            s1 = search("\:\s*Link-Site\s*\:\s*\[(.*?)\]\s*\[(.*?)\]\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", text)
            s2 = search("\:\s*Link-Site\s*\:\s*\[(.*?)\]\s*\[(.*?)\]\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", text)
            s3 = search("\:\s*Link-Site\s*\:\s*\[(.*?)\]\s*\[(.*?)\]\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)", text)
            s4 = search("\:\s*Link-Site\s*\:\s*\[(.*?)\]\s*\[(.*?)\]\s*\(\s*(\d+)\s*\)", text)
            s5 = search("\:\s*Link-Site\s*\:\s*\[(.*?)\]\s*\[(.*?)\]\s*\(\s*\)", text)
            
            if s1 == None and s2 == None and s3 == None and s4 == None and s5 == None:
                break

            m = ""
            sText = ""
            sHint = ""

            if s1 != None:
               m     = s1.group(0)
               sText = s1.group(1)
               sHint = s1.group(2)
            if s2 != None:
               m     = s2.group(0)
               sText = s2.group(1)
               sHint = s2.group(2)
            if s3 != None:
               m     = s3.group(0)
               sText = s3.group(1)
               sHint = s3.group(2)
            if s4 != None:
               m     = s4.group(0)
               sText = s4.group(1)
               sHint = s4.group(2)
            if s5 != None:
               m     = s5.group(0)
               sText = s5.group(1)
               sHint = s5.group(2)

            sMajor = None
            sMinor = None
            sSection = None
            sPage = None

            if s1 != None: sMajor = int(s1.group(3))
            if s2 != None: sMajor = int(s2.group(3))
            if s3 != None: sMajor = int(s3.group(3))
            if s4 != None: sMajor = int(s4.group(3))

            if sMajor == None:
                text = text.replace(m, f"<a href=\"{self.settings.baseUrl}\" class=\"link\" title=\"{sHint}\">{sText}</a>")
            else:
                if s1 != None: sMinor = int(s1.group(4))
                if s2 != None: sMinor = int(s2.group(4))
                if s3 != None: sMinor = int(s3.group(4))

                if s1 != None: sSection = int(s1.group(5))
                if s2 != None: sSection = int(s2.group(5))

                if s1 != None: sPage = s1.group(6)
            
                text = text.replace(m, f"<a href=\"{self.getSelfAddressURL(sMajor, sMinor, sSection, sPage)}\" class=\"link\" title=\"{sHint}\">{sText}</a>")
        
        # {text}
        #  <span class="boldfaced">----</span>
        text = sub('\{b\s*(.*?)\}', '<span class="boldfaced">\\1</span>', text)
        text = sub('\{B\s*(.*?)\}', '<span class="boldfaced">\\1</span>', text)

        # /text/
        #  <span class="italicized">----</span>
        text = sub('\{i\s*(.*?)\}', '<span class="italicized">\\1</span>', text)
        text = sub('\{I\s*(.*?)\}', '<span class="italicized">\\1</span>', text)
        
        return text

    ### Hierarchy
    def printHierarchy(self) -> None:
        print("Hierarchy:")
        for major in self.data.majors:
            print(f" > Major({major.id}): {major.title}")
            for minor in major.minors:
                print(f"    > Minor({minor.id}): {minor.title}")
                for section in minor.sections:
                    print(f"       > Section({section.id}): {section.title}")
                    for page in section.pages:
                        print(f"          > Page({page.id}): {page.title}")

    def openOutput(self) -> None:
        if (self.lastWrittenFilename != None and self.lastWrittenFilename != ""):
            webbrowser.open_new_tab(f"{self.firstWrittenFilename}")
        return