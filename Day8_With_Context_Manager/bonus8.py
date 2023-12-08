user_input = input("Enter today's date : ")
# print(user_input)
user_input2 = int(input("How do you rate Your mood today from 1 to 10 ? "))
# print(user_input2)
thought = input("Let your thoght flow : ")
with open(user_input,"w") as file :
    file.writelines("It was a good day in general. NO big event Happen")
with open(user_input,"r") as file :
    result = file.read()
    print(result)
