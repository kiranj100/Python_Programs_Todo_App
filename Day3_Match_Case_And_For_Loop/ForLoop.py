user_list = []

while True:
    user_input = input("Type add,show,exit :")
    user_input = user_input.strip()

    match user_input :
        case "add" :
                todo = input("Enter TODO :")
                user_list.append(todo)
        case "show" :#| "display":         # | this operator is Bitwise OR
            for item in user_list:      #this for loop is inside the loop of match
                item = item.title()         # .title() convert into first letter of word UpperCase
                print(item)
        case "exit" :
                break
      #  case _:               #showing the messege for enter valid keyword
        #     print("Please Enter Valid Key Word")

print("Bye!")