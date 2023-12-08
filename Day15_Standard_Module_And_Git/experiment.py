import glob

myfiles = glob.glob("files/*.txt") #it's a usefull when you have multiple text files
for files in myfiles :
    with open(files,"r") as file :
        result = file.read()
        print(result)