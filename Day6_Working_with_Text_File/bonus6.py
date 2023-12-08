container = ["All the Best",
             "How are you Doing",
             "We Can Do it"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for contant,filename in zip(container,filenames):
    file = open(f"./bonus_program_File/{filename}","w")
    file .write(contant)