user_list = []

while True:
    user_input = input("Type Add,Show,Edit,Exit : ")
    user_input = user_input.strip()

    match user_input :
        case "Add":
            todo = input("Enter The Todo's : ")
            user_list.append(todo)
        case "Show":
            for index, item in enumerate(user_list):
                print(index,'-',item.capitalize())
        case "Edit":
            number = int(input("Enter The Number: "))
            number = number - 1
            new_todo = input("Enter The New Todo's : ")
            user_list[number] = new_todo
        case "Exit":
            break
        case _:
            print("Enter The Valid Key Word")

print("Bye!")