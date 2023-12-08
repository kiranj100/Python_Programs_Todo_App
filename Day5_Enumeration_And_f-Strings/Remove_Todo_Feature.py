user_list = []

while True:
    user_input = input("Tyep add,show,edit,remove,exit : ")
    user_input = user_input.strip()

    match user_input :
        case "add" :
            todo = input("Enter the Todo's : ")
            user_list.append(todo)

        case "show" :
            for index,item in enumerate(user_list) :
                row = f"{index + 1}-{item}"
                print(row)
        case "edit" :
            numbers = int(input("Enter The Number : "))
            numbers = numbers - 1
            new_todo = input("Enter the New Todo's : ")
            user_list[numbers] = new_todo
        case "remove" :
            numbers = int(input("Enter the number of item which want to remove : "))
            user_list.pop(numbers - 1)
        case "exit" :
            break
        case _ :
            print("Enter the Valid Key Word")
print("Bye!")
