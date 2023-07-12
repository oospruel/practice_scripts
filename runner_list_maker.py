with open("runner_list.txt", "r") as file :
    total_runners = 1
    for lines in file:
        total_runners = total_runners + 1

with open("runner_list.txt", "w") as file :
    
    name = input("Enter runner {} name: ".format(total_runners))
    file.write("{} is runner {}".format(name, total_runners))
    
    



    
