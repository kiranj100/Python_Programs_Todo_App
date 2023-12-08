user_list = []

while True:
    user_input = input("Type add,show,edit,exit : ")
    user_input = user_input.strip()

    match user_input:
        case "add":
            todo = input("Enter The Todo's : ")
            user_list.append(todo)
        case "show":
            for index,item in enumerate(user_list):
                row = f"{index + 1}-{item}"
                print(row)
        case "edit":
                numbers = int(input("Enter the Number : "))
                numbers = numbers - 1
                new_todo = input("Enter New Todo's : ")
                user_list[numbers] = new_todo
        case "exit":
            break
        case _:
            print("Enter The Valid Key Word")

print("Bye!")