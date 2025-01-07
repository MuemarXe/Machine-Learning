#filePath ="C:\Users\Muema\Downloads\license.txt"
with open('Files&Exeptions\license.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
