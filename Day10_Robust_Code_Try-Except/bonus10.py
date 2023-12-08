try:
    width = float(input("Enter rectangle width : "))
    length = float(input("Enter rectangle length : "))
    if width == length :
        exit("it's look like square")           # exit function exit the execution
    area = width * length
    print(area)
except ValueError :
    print("Pleas Enter Numbers")