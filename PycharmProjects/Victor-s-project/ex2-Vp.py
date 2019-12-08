

#The function reads Questions, Teachers, Permissions, Parameters Filters from the required file
# The function gets the names of the existing files in which the information that we want to transfer


def ReadAndWrithToFile(FileNameQuestions,FileNameTeachers,FileNamePermissions,FileNameParametersFilters):
    fileQuestions = open(FileNameQuestions, 'r+')
    fileTeachers = open(FileNameTeachers, 'r+')
    filePermissions = open(FileNamePermissions, 'r+')
    fileParametersFilters = open(FileNameParametersFilters, 'r+')

    Questions=fileQuestions.readlines
    Teachers = fileTeachers.readlines
    Permissions=filePermissions.readlines
    ParametersFilters=fileParametersFilter.readlines

    fileQuestions.close()
    fileTeachers.close()
    filePermissions.close()
    fileParametersFilters.close()


#The function writh  Questions, Teachers, Permissions, Parameters Filters to the required file


    fileQuestionsTarget=open(" fileQuestionsTarget.txt",'w+')
    fileTeachersTarget=open("fileTeachersTarget.txt",'w+')
    filePermissionsTarget=open(" filePermissionsTarget.txt",'w+')
    fileParametersFiltersTarget=open("fileParametersFiltersTarget.txt",'w+')

    fileQuestionsTarget.write(Questions)
    fileTeachersTarget.write(Teachers)
    filePermissionsTarget.write(Permissions)
    fileParametersFiltersTarget.write(ParametersFilters)

    fileQuestionsTarget.close()
    fileTeachersTarget.close()
    filePermissionsTarget.close()
    fileParametersFiltersTarget.close()
    return

