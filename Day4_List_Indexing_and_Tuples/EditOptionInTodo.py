user_list = []

while True:
    user_input = input("Type add,show,edit or exit :")
    user_input = user_input.strip()

    match user_input :
        case "add" :
            todo = input("Enter the Todo List :")
            user_list.append(todo)
        case "show":
            for item in user_list :
                print(item.title())
        case "edit":
            number = int(input("Number of Todo Edit :"))  #int convert the number
            number = number - 1                            #indexing start with 0(zero so user enter 1 then input is show zero number index valiue
            new_todo = input("Enter New Todo :")
            user_list[number] = new_todo
        case "exit" :
            break

print("Bye!")