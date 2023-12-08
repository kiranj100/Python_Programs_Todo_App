def get_user_list() :
    with open("todo.txt","r") as file:
        set_user_list = file.readlines()
    return set_user_list

while True:
     user_input = input("Type add,show,edit,remove,exit : ")
     user_input = user_input.strip()

     if user_input.startswith("add") :

        todo = user_input[4:]

        user_list = get_user_list()

        user_list.append(todo + "\n" )

        with open("todo.txt","w") as file :
            file.writelines(user_list)

     elif user_input.startswith("show") :

        user_list = get_user_list()

        for index,item in enumerate(user_list) :
            item = item.strip("\n")
            row = f"{index + 1}-{item.capitalize()}"
            print(row)

     elif user_input.startswith("edit") :
         try:
            numbers = int(user_input[5:])
            print(numbers)
            numbers -= 1

            user_list = get_user_list()

            new_todo = input("Enter New Todos : ")
            user_list[numbers] = new_todo + "\n"

            with open("todo.txt","w") as file :
                file.writelines(user_list)
         except ValueError :
             print("Your Command is not Valid")
             continue

     elif user_input.startswith("remove") :
         try :                                  # try except handle the error
            numbers = int(user_input[7:])

            user_list = get_user_list()

            index = numbers - 1
            todo_to_remove = user_list[index].strip("\n")
            user_list.pop(index)

            with open("todo.txt","w") as file :
                file.writelines(user_list)

            message = f"Todo {todo_to_remove} Was Removed Successfully..."
            print(message)
         except IndexError :
             print("There is no Item with that Number")
             continue

     elif user_input.startswith("exit"):
            break

     else:
         print("Enter Valid Command")

print("Bye!")

