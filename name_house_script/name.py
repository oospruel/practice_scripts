#create people.txt file with choice of options.
with open ("people.txt", "a") as file: 
    names = input("enter name to go into file, ") 
    house = input("enter name of house ")
    age = input("enter age ")
    file.write("{}, {}, {}\n".format(names, house, age)) #writes names, house and age to txt file.