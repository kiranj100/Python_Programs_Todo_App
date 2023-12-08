
while True:
     user_input = input("Type add,show,edit,remove,exit : ")
     user_input = user_input.strip()

     if 'add' in user_input :

        todo = user_input[4:]

        with open("todo.txt") as file:
            user_list = file.readlines()

        user_list.append(todo)

        with open("todo.txt","w") as file :
            file.writelines(user_list)

     if 'show' in user_input :

        with open("todo.txt","r") as file :
            user_list = file.readlines()

        for index,item in enumerate(user_list) :
            item = item.strip("\n")
            row = f"{index + 1}-{item.capitalize()}"
            print(row)

     if 'edit' in user_input :
        numbers = int(user_input[5:])
        numbers -= 1

        with open("todo.txt",'r') as file :
            user_list = file.readlines()

        new_todo = input("Enter New Todos : ")
        user_list[numbers] = new_todo + "\n"
        with open("todo.txt","w") as file :
            file.writelines(user_list)

     if 'remove' in user_input :
        numbers = int(user_input[7:])

        with open("todo.txt", 'r') as file:
            user_list = file.readlines()
        index = numbers - 1
        todo_to_remove = user_list[index].strip("\n")
        user_list.pop(index)

        with open("todo.txt","w") as file :
            file.writelines(user_list)

        message = f"Todo {todo_to_remove} Was Removed Successfully..."
        print(message)


     if 'exit' in user_input :
            break

print("Bye!")

