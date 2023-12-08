
while True:
    user_input = input("Type add,show,edit,remove,exit : ")
    user_input = user_input.strip()

    match user_input :
        case "add" :
            todo = input("Enter the todo : ") + "\n"
            # file = open("todo.txt","r")        read the .txt file "r" read lines permission
            # user_list = file.readlines()      # this is traditional way
            # file.close()

            with open("todo.txt") as file:              # with clause we don't need to close file,recommended for Quality code
                user_list = file.readlines()        # this is modern way

            user_list.append(todo)

            # file = open("todo.txt",'w')       Save the "todos list permanent in .txt file
            # file.writelines(user_list)
            # file.close()

            with open("todo.txt","w") as file :
                file.writelines(user_list)

        case "show" :
            # file = open("todo.txt","r")
            # user_list = file.readlines()
            # file.close()

            with open("todo.txt","r") as file :
                user_list = file.readlines()

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

            with open("todo.txt",'r') as file :
                user_list = file.readlines()
          #  print("Here is Existing Todo's List : ",user_list)

            new_todo = input("Enter New Todos : ")
            user_list[numbers] = new_todo + "\n"
            with open("todo.txt","w") as file :
                file.writelines(user_list)

        case "remove" :
            numbers = int(input("Enter the number of item you want to remove : "))

            with open("todo.txt", 'r') as file:
                user_list = file.readlines()
            index = numbers - 1
            todo_to_remove = user_list[index].strip("\n")
            user_list.pop(index)

            with open("todo.txt","w") as file :
                file.writelines(user_list)

            message = f"Todo {todo_to_remove} Was Removed Successfully..."
            print(message)

        case "exit" :
            break
print("Bye!")

