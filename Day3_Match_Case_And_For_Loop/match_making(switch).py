resultlist = []
while True:
    user_input = input("Type Add or Show or exit: ")
    match user_input:
        case 'Add':
            todo = input("Enter a todo: ")
            resultlist.append(todo)
        case 'Show':
            print(resultlist)
        case 'exit':
            break




