feet_inches = input("Enter feet and inches : ")

def conver(feet_inches) :
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meter = feet * 0.3048 + inches * 0.0245
    return f"{feet} feet and {inches} inches is equal to {meter}meters"
result = conver(feet_inches)
if result < 1 :
    print("kid is too small")
else :
    print("kid can use the slide")