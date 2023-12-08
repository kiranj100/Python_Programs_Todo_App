filename = ["1.doc","1.report","1.presentation"]
# Following are shortcut way
filename = [filename.replace('.', "-") + '.txt' for filename in filename]
print(filename)

for file in filename :               # this is Normal way
    rep = file.replace(".","-")
    print(f"{rep}.txt")
