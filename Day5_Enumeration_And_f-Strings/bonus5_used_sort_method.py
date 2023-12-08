User_list = ["sen","binn","kan"]
User_list.sort()                    #Ascending Order : bin,kan,sen
# User_list.sort(reverse=True)      #descending Order : sen,kan,bin
for index,item in enumerate(User_list) :
    presentation = f"{index + 1}.{item.capitalize()}"
    print(presentation)