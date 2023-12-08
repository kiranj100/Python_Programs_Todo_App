def get_read_lines(filepath="todo.txt") :
    with open(filepath,"r") as file:
        set_user_list = file.readlines()
    return set_user_list

 # non default parameter put first place and second place is default parameter this is right way
def get_write_lines(user_list_argument, filepath="todo.txt"):
    with open(filepath,'w') as file :
        file.writelines(user_list_argument)

while True:
     user_input = input("Type add,show,edit,remove,exit : ")
     user_input = user_input.strip()

     if user_input.startswith("add") :

        todo = user_input[4:]

        user_list = get_read_lines()

        user_list.append(todo + "\n" )

        get_write_lines(user_list)

     elif user_input.startswith("show") :

        user_list = get_read_lines()

        for index,item in enumerate(user_list) :
            item = item.strip("\n")
            row = f"{index + 1}-{item.capitalize()}"
            print(row)

     elif user_input.startswith("edit") :
         try:
            numbers = int(user_input[5:])
            print(numbers)
            numbers -= 1

            user_list = get_read_lines()

            new_todo = input("Enter New Todos : ")
            user_list[numbers] = new_todo + "\n"

            get_write_lines(user_list)

         except ValueError :
             print("Your Command is not Valid")
             continue

     elif user_input.startswith("remove") :
         try :                                  # try except handle the error
            numbers = int(user_input[7:])

            user_list = get_read_lines()

            index = numbers - 1
            todo_to_remove = user_list[index].strip("\n")
            user_list.pop(index)

            get_write_lines(user_list)

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

