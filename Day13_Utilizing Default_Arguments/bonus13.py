feet_inches = input("Enter feet and inches : ")
#using decoupling.
#decoupling means as requirement crate two function
#and handle one task at a time to specific function.
def height(feet_inches ):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet" : feet,"inches": inches}

def convert(feet, inches) :
    meter = feet * 0.3048 + inches * 0.0254
    return meter


get_height = height(feet_inches)

result = convert(get_height['feet'], get_height['inches'])

print(f"{get_height['feet']} feet and {get_height['inches']} is equal to {result}")

if result < 1 :
    print("Kid is too small.")
else :
    print("Kid can use the slide.")
