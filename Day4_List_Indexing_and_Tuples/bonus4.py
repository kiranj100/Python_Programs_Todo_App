filename = ["1.Raw Data.txt", "2.Reports.txt","3.Presentations.txt"]
print("Old Output is : ", filename)
print("New Output is : ")
for files in filename:
    files = files.replace(".","-",1)
    print(files)