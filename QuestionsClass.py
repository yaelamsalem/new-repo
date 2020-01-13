from TestData import Test
"""Constructor question"""

class Question(Test):
    def __init__(self, date, semester, examinername, numberOfQuestions, studentlevel, Mangerlevel, QuestionNumber,Questionspath,Serialnumber,
                 SeveralSections, levelQuestions, Topic,Testpath):
        super( date, semester, examinername, numberOfQuestions, studentlevel, Mangerlevel,Testpath).__init__(QuestionNumber, SeveralSections, levelQuestions, Topic,Questionspath,Serialnumber)
        self.QuestionNumber = QuestionNumber
        self.SeveralSections = SeveralSections
        self.levelQuestions = levelQuestions
        self.Topic = Topic
        self.Questionspath=Questionspath
        self.Serialnumber=Serialnumber

    def setQuestionNumber(self, QuestionNumber):
        self.QuestionNumber = QuestionNumber

    def getQuestionNumber(self):
        return self.QuestionNumber

    def setSeveralSections(self, SeveralSections):
        self.SeveralSections = SeveralSections

    def getSeveralSections(self):
        return self.SeveralSections

    def setlevelQuestions(self, levelQuestions):
        self.levelQuestions = levelQuestions

    def getlevelQuestions(self):
        return self.levelQuestions

    def setTopic(self, Topic):
        self.Topic = Topic

    def getTopic(self):
        return self.Topic

    def setQuestionspath(self, Questionspath):
        self.Questionspath = Questionspath

    def getQuestionspath(self):
        return self.Questionspath

    def setQuestionspath(self, Serialnumber):
        self.Serialnumber = Serialnumber

    def getQuestionspath(self):
        return self.Serialnumber

