#This script prints the imputs from people.txt created from the name.py script. 
import csv

tmp_list = []
with open("people.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        tmp_list.append(row)
for student in sorted(tmp_list, key=lambda x:x["home"]) :
    print("{} is {}, and lives at {}".format(student['name'], student['age'], student['home']))
