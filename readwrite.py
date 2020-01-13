from lectureClass import lecturer
from studentClass import student
from TestData import Test
from QuestionsClass import Question
from Mangerclass import  Manger
from sectionClass import section



def readFromStudent(self):
    fileStudent = open("fileStudent.txt", 'w+')
    fileStudent.write(str(self.getName()))
    fileStudent.write("\n")
    fileStudent.write(str(self.getType()))
    fileStudent.write("\n")
    fileStudent.write(str(self.getpassword()))
    fileStudent.write("\n")
    fileStudent.write(str(self.getPhone()))
    fileStudent.write("\n")
    fileStudent.write(str(self.getserial_number()))
    fileStudent.write("\n")
    fileStudent.close()
def readFromlecturer(self):
    filelecturer = open("fileLectucer.txt", 'w+')
    filelecturer.write(str(self.getName()))
    filelecturer.write("\n")
    filelecturer.write(str(self.getType()))
    filelecturer.write("\n")
    filelecturer.write(str(self.getpassword()))
    filelecturer.write("\n")
    filelecturer.write(str(self.getPhone()))
    filelecturer.write("\n")
    filelecturer.write(str(self.getserial_number()))
    filelecturer.write("\n")
    filelecturer.close()
def readFromManger(self):
    fileManger = open("fileManger.txt", 'w+')
    fileManger.write(str(self.getName()))
    fileManger.write("\n")
    fileManger.write(str(self.getType()))
    fileManger.write("\n")
    fileManger.write(str(self.getpassword()))
    fileManger.write("\n")
    fileManger.write(str(self.getPhone()))
    fileManger.write("\n")
    fileManger.write(str(self.getserial_number()))
    fileManger.write("\n")
    fileManger.close()
def readFromTest(self):
    fileTest = open("fileTest.txt", 'w+')
    fileTest.write(str(self.getDate()))
    fileTest.write("\n")
    fileTest.write(str(self.getsemester()))
    fileTest.write("\n")
    fileTest.write(str(self.getexaminername()))
    fileTest.write("\n")
    fileTest.write(str(self.getnumberOfQuestions()))
    fileTest.write("\n")
    fileTest.write(str(self.getstudentlevel()))
    fileTest.write("\n")
    fileTest.write(str(self.getMangerlevel()))
    fileTest.write("\n")
    fileTest.write(str(self.getTestpath()))
    fileTest.write("\n")
    fileTest.close()
def readFromSection(self):#לוותר זה ממש מוגזם אנחנו לא יודעות איך לחתוך חצי עמוד
    fileSection = open("fileSection.txt", 'w+')
    fileSection.write(str(self.getdate()))
    fileSection.write("\n")
    fileSection.write(str(self.getsemester()))
    fileSection.write("\n")
    fileSection.write(str(self.getexaminername()))
    fileSection.write("\n")
    fileSection.write(str(self.getnumberOfQuestions()))
    fileSection.write("\n")
    fileSection.write(str(self.getstudentlevel()))
    fileSection.write("\n")
    fileSection.write(str(self.Mangerlevel()))
    fileSection.write("\n")
    fileSection.write(str(self.QuestionNumber()))
    fileSection.write("\n")
    fileSection.write(str(self.SeveralSections()))
    fileSection.write("\n")
    fileSection.write(str(self.levelQuestions()))
    fileSection.write("\n")
    fileSection.write(str(self.Topic()))
    fileSection.close()
def readFromQuestions(self):
    fileQuestions = open("fileQuestions.txt", 'w+')
    fileQuestions.write(str(self.getDate()))
    fileQuestions.write("\n")
    fileQuestions.write(str(self.getsemester()))
    fileQuestions.write("\n")
    fileQuestions.write(str(self.getexaminername()))
    fileQuestions.write("\n")
    fileQuestions.write(str(self.getnumberOfQuestions()))
    fileQuestions.write("\n")
    fileQuestions.write(str(self.getstudentlevel()))
    fileQuestions.write("\n")
    fileQuestions.write(str(self.getMangerlevel()))
    fileQuestions.write("\n")
    fileQuestions.write(str(self.getQuestionNumber()))
    fileQuestions.write("\n")
    fileQuestions.write(str(self.getQuestionspath()))
    fileQuestions.write("\n")
    fileQuestions.write(str(self.getSerialnumber()))
    fileQuestions.write("\n")
    fileQuestions.write(str(self.getSeveralSections()))
    fileQuestions.write("\n")
    fileQuestions.write(str(self.getlevelQuestions()))
    fileQuestions.write("\n")
    fileQuestions.write(str(self.getTopic()))
    fileQuestions.write("\n")
    fileQuestions.close()




def FileToStudent(list):
    filename = open("fileStudent.txt", 'w+')
    for i in list:
        name = filename.readline()
        type = filename.readline()
        password = filename.readline()
        phone = filename.readline()
        slr = filename.readline()
        x = student(name, type, password, phone, slr)
        list.append(x)
    filename.close()
    return list
def FileToManger(list):
    filename = open("fileManger.txt", 'w+')
    for i in list:
        name=filename.readline()
        type = filename.readline()
        password = filename.readline()
        phone = filename.readline()
        slr = filename.readline()
        y=Manger(name,type,password,phone,slr)
        list.append(y)
    filename.close()
    return list
def FileTolecturer(list):
    filename=open("filelecturer.txt", 'r+')
    for i in list:
        name=filename.readline()
        type = filename.readline()
        password = filename.readline()
        phone = filename.readline()
        slr = filename.readline()
        y=lecturer(name,type,password,phone,slr)
        list.append(y)
    filename.close()
    return list
def FileToTest(list):
    filename=open("fileTest.txt", 'r+')
    for i in list:
        date=filename.readline()
        semester = filename.readline()
        examinername = filename.readline()
        numberOfQuestions = filename.readline()
        studentlevel = filename.readline()
        Mangerlevel = filename.readline()
        Testpath = filename.readline()
        y=Manger(date,semester,examinername,numberOfQuestions,studentlevel,Mangerlevel,Testpath)
        list.append(y)
    filename.close()
    return list
def FileToSection(list):
    filename = open("fileToSection.txt", 'r+')
    for i in list:
        date = filename.readline()
        semester = filename.readline()
        examinername = filename.readline()
        numberOfQuestions = filename.readline()
        studentlevel = filename.readline()
        Mangerlevel = filename.readline()
        QuestionNumber = filename.readline()
        SeveralSections= filename.readline()
        levelQuestions= filename.readline()
        Topic= filename.readline()
        y = Manger(date, semester, examinername, numberOfQuestions, studentlevel, Mangerlevel, QuestionNumber,SeveralSections,levelQuestions,Topic)
    list.append(y)
    filename.close()
    return list
def FileToQuestions(list):
    filename=open("fileQuestions.txt", 'r+')
    for i in list:
        date = filename.readline()
        semester = filename.readline()
        examinername = filename.readline()
        numberOfQuestions = filename.readline()
        studentlevel = filename.readline()
        Mangerlevel = filename.readline()
        QuestionNumber = filename.readline()
        Questionspath = filename.readline()
        Serialnumber = filename.readline()
        SeveralSections = filename.readline()
        levelQuestions = filename.readline()
        Topic = filename.readline()
        y = Manger(date, semester, examinername, numberOfQuestions, studentlevel, Mangerlevel, QuestionNumber,
                   Questionspath, Serialnumber, SeveralSections,levelQuestions,Topic)
    list.append(y)
    filename.close()
    return list






