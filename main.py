
from readwrite import readFromStudent
from TestData import Test
from QuestionsClass import Question
from Mangerclass import Manger
from lectureClass import lecturer
import datetime
from readwrite import readFromManger
from readwrite import FileTolecturer
from readwrite import FileToManger
from readwrite import FileToQuestions
from readwrite import FileToSection
from readwrite import FileToStudent
from readwrite import FileToTest
from readwrite import readFromlecturer
from readwrite import readFromTest
from readwrite import readFromSection
from readwrite import readFromQuestions
from readwrite import readFromManger
from studentClass import student
from cutPdf import PDFsplit #מקבל קובץ פידיאף וטווח
import os
def writhtologfile(txt):
   with open ("logfile.txt",'a') as file:
        file.writelines(txt)

"""the list of data by type"""
sectionlist=[]
questionslist=[]
testlist=[]
studentlist=[]
lecturerlist=[]
mangerlist=[]
"""read from file the data to list of obj"""
studentlist=FileToStudent(studentlist)
#questionslist=FileToQuestions(questionslist)
#testlist=FileToTest(testlist)
#sectionlist=FileToSection(sectionlist)
lecturerlist=FileTolecturer(lecturerlist)
mangerlist=FileToManger(mangerlist)
"""the main manager-for cheking"""
#f = open('test1' + '.pdf')
#dp = os.path.realpath(f.name)
#a=Test('2.4.19','a','test1','3','3','3',dp)
#testlist.append(a)
"""enter username and password -chcing if the user in data base"""
def enter():
    print("enter your user name, password")
    userName=input()
    password=input()
    for i in studentlist:
        if userName==i.getName():
            if password==i.getpassword():
                return "s"
    for i in mangerlist:
        if userName==i.getName():
            if password==i.getpassword():
                return "m"
    for i in lecturerlist:
        if userName == i.getName():
            if password == i.getpassword():
                return "l"
    print("you dont have excess to the progrem")
    writhtologfile("error dosent have excess to the progrem " + str(datetime.datetime.now()))
    return
def opManger():
    choice=0
    while choice != 10:
        print("1=add test\n2=remove test\n3=update test")
        print("4=add lectucer\n5=remove lectucer\n6=update lectucer")
        print("7=add student\n8=remove student\n9=update student\n10=end\n")
        choice=int(input())

        if choice==1:
            name=input("exam name")
            f = open(name+'.pdf')
            datapath=os.path.realpath(f.name)
            x=Test(input("date"),input("semester"),name,input("number of quetion"),input("student level"),input("manger level"),datapath)
            testlist.append(x)
            questions=[]
            for i in x.getnumberOfQuestions():
                if x.getnumberOfQuestions()==1:
                    splits=[1,1]
                    PDFsplit(x.getexaminername() + '.pdf', splits)
                else:
                    range1 = input("enter the first page you want")
                    range2 = input("enter the last page you want")
                    splits = [int(range1), int(range2)]
                    PDFsplit(x.getexaminername() + '.pdf', splits)
                p =x.getexaminername()
                path = os.getcwd() + '\\' + p +i +'.pdf'
                questions.append(y=Question(x.getDate(), x.getsemester(), x.examinername, x.getnumberOfQuestions(), '0', input("enter level"),i,path,input("enter serial number"),'0','0','0',x.getTestpath() ))

            f.close()
        if choice==2:
            testname = input("enter test name you want to remove")

            date = input("enter test date you want to remove")
            for i in testlist:
                if testname == i.getexaminername():
                    if date == i.getDate():
                        i.remove()
        if choice==3:
            testname=input("enter test name you want to update")
            date=input("enter test date you want to update")
            for i in testlist:
                if testname == i.getexaminername():
                    if date == i.getDate():
                        print("1=update date\n2=update semester\n3=update name\n")
                        print("4=update number of question\n5=update manager level\n")
                        c=int(input())
                        if c==1:
                            i.setDate(input("enter date"))
                        if c==2:
                            i.setsemester(input("enter semester"))
                        if c==3:
                            i.setexaminername(input("enter name"))
                        if c==4:
                            i.setnumberOfQuestions(input("enter number of question"))
                        if c==5:
                            i.setMangerlevel(input("enter test level"))
        if choice==4:
            x = lecturer(input("name"), input("type"), input("password"), input("phone"),input("serial_number"))
            lecturerlist.append(x)
            writhtologfile("lecturer added "+str(datetime.datetime.now()))
        if choice==5:
            serialNumber = input("enter serial number of lecturer you want to remove")
            for i in lecturerlist:
                if serialNumber == i.getserial_number():
                    i.remove()
        if choice==6:
            serialNumber = input("enter serial number of lecturer you want to update")
            for i in lecturerlist:
                if serialNumber == i.getserial_number():
                    print("1=update name\n2=update type\n3=update password\n4=update phone\n")
                    c = int(input())
                    if c==1:
                        i.setName(input("enter name"))
                    if c==2:
                        i.setType(input("enter type"))
                    if c==3:
                        i.setpassword(input("enter password"))
                    if c==4:
                        i.setPhone(input("enter phone"))
        if choice==7:
            x = student(input("name"), input("type"), input("password"), input("phone"),"0")
            studentlist.append(x)
            writhtologfile("student added " + str(datetime.datetime.now()))
        if choice==8:
            serialNumber = input("enter serial number of student you want to remove")
            for i in studentlist:
                if serialNumber == i.getserial_number():
                    i.remove()
        if choice==9:
            serialNumber = input("enter serial number of student you want to update")
            for i in studentlist:
                if studentlist == i.getserial_number():
                    print("1=update name\n2=update type\n3=update password\n4=update phone\n")
                    c = int(input())
                    if c == 1:
                        i.setName(input("enter name"))
                    if c == 2:
                        i.setType(input("enter type"))
                    if c == 3:
                        i.setpassword(input("enter password"))
                    if c == 4:
                        i.setPhone(input("enter phone"))
    if choice==10:
        print("good bey")
        return
def opStudent_lecturer():
    category = 0
    while category != 13:
        print(" 1-date\n,2-semester\n,3-examinername\n,4-numberOfQuestions\n,5-studentlevel\n,6-Mangerlevel\n7-SeveralSections\n,8-levelQuestions\n,9-Topic\n10- section\n,11-levelsection\n,12- topicsection\n13-end\n")
        category = int(input("enter category:"))
        if category == 1:
            x = input("enter data xx.xx.xxxx")
            for i in testlist:
                if x == i.getDate():
                    y=i.getexaminername()
                    path = os.getcwd()+'\\'+y+'.pdf'
                    fp = open(path, 'r+')
        if category == 2:
            x = input("enter semester(a/b/c)")
            for i in testlist:
                if x == i.getsemester():
                    range1 = input("enter the first page you want")
                    range2 = input("enter the last page you want")
                    splits = [range1, range2]
                    PDFsplit(i.getexaminername+'.pdf', splits)
                elif (i == len(testlist) and x != i.getexaminername()):
                    print("the exam isn't found")
        if category == 3:
            x = input("enter test name:")
            for i in testlist:
                if x == i.getexaminername():
                    range1 = input("enter the first page you want")
                    range2 = input("enter the last page you want")
                    splits = [int(range1),int(range2)]
                    PDFsplit(i.getexaminername()+'.pdf', splits)
                elif (i== len(testlist) and x != i.getexaminername()):
                    print("the exam isn't found")
        if category == 4:
            for i in testlist:
                if x == i.getnumberOfQuestions():
                    range1 = input("enter the first page you want")
                    range2 = input("enter the last page you want")
                    splits = [int(range1),int(range2)]
                    PDFsplit(i.getexaminername()+'.pdf', splits)

        if category == 5:
            x = input("enter student level 1-10")
            # שנחשב ממוצע של רמת קושי נעגל למספר שלם
            # רמת מבחן נקבעת ממוצע השאלות שמורכבות ממוצע רמת הסעיפים
            for i in testlist:
                if x == i.getstudentlevel():
                    range1 = input("enter the first page you want")
                    range2 = input("enter the last page you want")
                    splits = [int(range1),int(range2)]
                    PDFsplit(i.getexaminername()+'.pdf', splits)

        if category == 6:
            x = input("enter  manger level 1-10")
            # שנחשב ממוצע של רמת קושי נעגל למספר שלם
            # רמת מבחן נקבעת ממוצע השאלות שמורכבות ממוצע רמת הסעיפים
            x = input("enter Manger level")
            for i in testlist:
                if x == i.getMangerlevel():
                    f=open(i.getTestpath())
                    range1 = input("enter the first page you want")
                    range2 = input("enter the last page you want")
                    splits = [int(range1),int(range2)]
                    PDFsplit(i.getexaminername()+'.pdf', splits)
                    ####איך לעשות אם לא מוצא ישלח הודעה מתאימה
        if category == 7:
            x = input("enter  Several Sections ")
            for i in testlist:
                if x == i.getSeveralSections():
                    range1 = input("enter the first page you want")
                    range2 = input("enter the last page you want")
                    splits = [int(range1),int(range2)]
                    PDFsplit(i.getexaminername()+'.pdf', splits)
        if category == 8:
            # שנחשב ממוצע של רמת קושי נעגל למספר שלם
            # רמת מבחן נקבעת ממוצע השאלות שמורכבות ממוצע רמת הסעיפים
            x = input("enter Questions level")
            for i in testlist:
                if x == i.getlevelQuestions():
                    range1 = input("enter the first page you want")
                    range2 = input("enter the last page you want")
                    splits = [int(range1),int(range2)]
                    PDFsplit(i.getexaminername()+'.pdf', splits)

        if category == 9:
            x = input("enter Topic")
            for i in testlist:
                x = input("enter Manger level")
                if x == i.getTopic():
                    range1 = input("enter the first page you want")
                    range2 = input("enter the last page you want")
                    splits = [int(range1),int(range2)]
                    PDFsplit(i.getexaminername()+'.pdf', splits)

        if category == 10:
            x = input("enter number of section ")
            for i in testlist:
                if x == i.getsection():
                    range1 = input("enter the first page you want")
                    range2 = input("enter the last page you want")
                    splits = [int(range1), int(range2)]
                    PDFsplit(i.getexaminername() + '.pdf', splits)

        if category == 11:
            x = input("enter levelsection")
            for i in testlist:
                if x == i.getlevelsection():
                    range1 = input("enter the first page you want")
                    range2 = input("enter the last page you want")
                    splits = [int(range1), int(range2)]
                    PDFsplit(i.getexaminername() + '.pdf', splits)

        if category == 12:
            x = input("enter topicsection")
            for i in testlist:
                if x == i.gettopicsection():
                    range1 = input("enter the first page you want")
                    range2 = input("enter the last page you want")
                    splits = [int(range1), int(range2)]
                    PDFsplit(i.getexaminername() + '.pdf', splits)
    if category==13:
        print("Good-bey")

"""opstin for main"""
userType=enter()
if userType=="m":
    opManger()
if userType=="s" or userType=="l":
    opStudent_lecturer()


    """wert to file befor exit from the program"""

readFromStudent(studentlist)
readFromManger(mangerlist)
readFromlecturer(lecturerlist)
#קריאה לקבצי מבחנים וכו








