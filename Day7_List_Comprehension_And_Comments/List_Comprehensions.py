
while True:
    user_input = input("Type add,show,edit,remove,exit : ")
    user_input = user_input.strip()

    match user_input :
        case "add" :
            todo = input("Enter the todo's : ") + "\n"
            file = open("Todos.txt","r")       # read the .txt file "r" read lines permission
            user_list = file.readlines()
            file.close()

            user_list.append(todo)

            file = open("Todos.txt",'w')       #Save the "todos list permanent in .txt file
            file.writelines(user_list)
            file.close()
        case "show" :
            file = open("Todos.txt","r")
            user_list = file.readlines()
            file.close()

            # new_user_list = []                        This is using normal way
            # for item in user_list :
            #     new_item  = item.strip("\n")
            #     new_user_list.append(new_item)
            # strip("\n") is used to not creating new line
            # new_user_list = [item.strip("\n") for item in user_list]    This way called List Comprehension

            for index,item in enumerate(user_list) :
                item = item.strip("\n")                     # effective way of using
                row = f"{index + 1}-{item.capitalize()}"
                print(row)

        case "edit" :
            numbers = int(input("Enter the number : "))
            numbers -= 1
            new_todo = input("Enter New Todos : ")
            user_list[numbers] = new_todo
        case "remove" :
            numbers = int(input("Enter the number of item you want to remove : "))
            user_list.pop(numbers - 1)
        case "exit" :
            break
print("Bye!")

