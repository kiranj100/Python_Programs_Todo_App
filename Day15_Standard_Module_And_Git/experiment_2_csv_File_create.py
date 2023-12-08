import csv

with open("weather.csv", "r") as file :
    result = list(csv.reader(file))

    #enter name of city it's present in weather.csv file
city = input("Enter the City Name : ")

for data in result :
    if data[0] == city :
        print(data[1])
