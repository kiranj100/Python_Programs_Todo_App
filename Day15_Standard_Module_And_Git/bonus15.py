import json

with open("questions.json","r") as file :
    content = file.read()

#print(type(content))    # type is string but we required list

data = json.loads(content)
#print(type(data))       # type is list


for question in data :
    print(question["Question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1}-{alternative}")

    user_input = int(input("Enter Your Answer : "))
    question["user_input"] = user_input


score = 0
for index, question in enumerate(data) :
    if question["user_input"] == question["Correct_Answer"]:
        score = score + 1
        result = "Correct Answer"
    else :
        result = "Wrong Answer"

    message = f"{index + 1} {result} - Your Answer: {question['user_input']}, " \
              f" Correct Answer is: {question['Correct_Answer']}"

    print(message)

print("Score is :",score, "/", len(data))