
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for fil in filenames:
    file = open(fil, 'w')
    file.write("Hello")
    file.close()