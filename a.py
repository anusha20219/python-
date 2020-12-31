import os



allfiles = os.listdir()

for i in allfiles:
    if i == "a.py" or i == "create.py":
        continue

    newlist = i.split("-")
    newname = newlist[1]+"-"+newlist[0]+"-"+newlist[2]
    os.rename(i,newname) 
