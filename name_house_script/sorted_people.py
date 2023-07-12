import operator

tmp_list = []
with open("people.txt") as file:
    for line in file:
        line = line.strip().split(",")
        name = line[0]
        house = line[1]
        age = line[2]
        students = {"name": name, "house": house, "age": age} # creates dictionary and assigns keys and values
        tmp_list.append(students) #Append to list
#print(sorted(tmp_list, key= operator.itemgetter("age")))   REMOVE POUND TO VIEW SORTED LIST
print("{} is{},and lives at{}".format(students["name"], students["age"], students["house"]))
