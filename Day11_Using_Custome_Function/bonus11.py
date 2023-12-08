def get_average() :
     with open("bonus.txt",'r') as file :
         data = file.readlines()
     value = data[1:]
     value = [float(i) for i in value]
     average_local = sum(value) / len(value)
     return average_local

average = get_average()
print(average)


