password = input("Enter the password : ")

result = {}             #dictionary

if len(password) >= 8 :
    result["Password Length"] = True
else:
    result["Password Lenght"] = False

digit = False

for item in password :
    if item.isdigit():
        digit = True
result["Password Digit's"] = (digit)

uppercase = False
for item in password :
    if item.isupper() :
        uppercase = True

result["Password UpperCase Charactor"] = (uppercase)

#print(result)
#print(all(result))

if (all(result.values())) :
    print("Strong Password")
else:
    print("Weak Password")