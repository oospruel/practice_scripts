#This script creates a list of runners
total_runners = 1
with open("runner_list.txt", "r+") as file :
    
    for lines in file:
        total_runners = total_runners + 1 #adds to keep runner number updated

with open("runner_list.txt", "a") as file :
    
    name = input("Enter runner {} name: ".format(total_runners))
    file.write("{} is runner {}".format(name, total_runners))
    
    



    
