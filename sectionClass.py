from QuestionsClass import Question
"""Constructor section"""

class section(Question):
    class section(Question):
        def __init__(self, date, semester, examinername, numberOfQuestions, studentlevel, Mangerlevel, QuestionNumber,
                     SeveralSections, levelQuestions, Topic, section, levelsection, topicsection):
            super().__init__(date, semester, examinername, numberOfQuestions, studentlevel, Mangerlevel, QuestionNumber,
                             SeveralSections, levelQuestions, Topic)
            self.section = section
            self.levelsection = levelsection
            self.topocsection = topicsection

        def setsection(self, section):
            self.section = section

        def getsection(self):
            return self.section

        def setlevelsection(self, levelsection):
            self.levelsection = levelsection

        def getlevelsection(self):
            return self.levelsection

        def settopicsection(self, topicsection):
            self.topicsection = topicsection

        def gettopicsection(self):
            return self.topicsection