def geet(message) :
    new_message = message.capitalize()
    print("Hey Hello!")
    return new_message

user_input = input("What greeting you want ? ")
greeting = geet(user_input)
print(greeting)