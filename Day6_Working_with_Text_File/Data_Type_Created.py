
while True:
    user_input = input("Type add,show,edit,remove,exit : ")
    user_input = user_input.strip()

    match user_input :
        case "add" :
            todo = input("Enter the todo's : ")
            file = open("Todo's.txt","r")       # read the .txt file "r" read lines permission
            user_list = file.readlines()
            file.close()

            user_list.append(todo)

            file = open("Todo's.txt",'w')       #Save the "todos list permanent in .txt file
            file.writelines(user_list)
            file.close()
        case "show" :
            file = open("Todo's.txt","r")
            user_list = file.readlines()
            file.close()
            for index,item in enumerate(user_list) :
                row = f"{index + 1}-{item.capitalize()}"
                print(row)
        case "edit" :
            numbers = int(input("Enter the number : "))
            numbers -= 1
            new_todo = input("Enter New Todo's : ")
            user_list[numbers] = new_todo
        case "remove" :
            numbers = int(input("Enter the number of item you want to remove : "))
            user_list.pop(numbers - 1)
        case "exit" :
            break
print("Bye!")

