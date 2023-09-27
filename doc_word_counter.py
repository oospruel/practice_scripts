#!/usr/bin/python
file_name = input("Enter file path ") 
# try to open file
try:
    f = open(file_name)
except:
    print("not a valid path for file. Try again.")
    exit()
# create empty dicionary
tmpdic = {}
# strip lines into words, and add words to empty dictionary
for fn in f :
    fn = fn.strip()
    wds = fn.split()
    for splitw in wds:
        tmpdic[splitw] = tmpdic.get(splitw, 0) + 1

#create sorted tuples
tmptup = sorted( [ (v,k) for k,v in tmpdic.items()], reverse=True)
# create empty list
newtuplist = []
#rearrange tuple and add to the new empty list
for v,k in tmptup :
    newtup = k,v
    newtuplist.append(newtup)


print("top 15 repeated words ", newtuplist[:15])

    

