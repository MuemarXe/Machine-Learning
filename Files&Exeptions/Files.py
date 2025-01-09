filePath ="C:\Users\Muema\Downloads\license.txt"
with open(filePath) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
