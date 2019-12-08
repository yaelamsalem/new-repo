class Question_characteristics:
    mainTopic=input("Name of main topic")
    questionCode=input("The code of the question")
    subTheme=input("The sub theme")
    difficulty=input("The level of difficulty")
    SolutionType=input("Enter the solution type (final, full, video")
    year=input("The year of the test")
    semester=input("Enter the semester 1/2/3")
    NumberOfTest=input("Enter the number of test 1/2/3")
    format=input("Enter the type of format (pdf/word")
ans=True
while ans:
    print (" 1.Add a lecturer\n2.Delete a lecturer\n3.Look Up test\n4.Adding a test\n5.Exit/Quit ")
    ans=input("What would you like to do? ")
    if ans=="1":
      print("\n lecturer Added")
    elif ans=="2":
      print("\n lecturer Deleted")
    elif ans=="3":
      print("\n Look Up test")
    elif ans=="4":
      print("\n Adding a test")
    elif ans == "5":
      print("\n Goodbye")
    elif ans !="":
      print("\n Not Valid Choice Try again")

