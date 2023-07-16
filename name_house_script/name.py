#create people.txt file with choice of options.
import csv
name = input("enter name to go into file, ") 
home= input("enter name of house ")
age = input("enter age ")

with open ("people.csv", "a") as file: 
    writer = csv.DictWriter(file, fieldnames=["name", "home", "age"])
    writer.writerow({"name": name, "home": home, "age": age})
