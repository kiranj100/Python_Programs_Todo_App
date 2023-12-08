content = ["I am a","I am b","I am c"]
filename = ["a.txt","b.txt","c.txt"]

for cont,file in zip(content,filename) :
    file = open(file,"w")
    file = file.write(cont)
    print(file)

