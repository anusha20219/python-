import random
li = ["02-12-1999","05-20-2020","11-15-2006","04-03-2009","09-09-2000","12-22-2020","12-09-2000","03-30-2000","05-29-2020","10-10-1999"]


for i in range(10):
    ele = random.choice(li)
    f = open(ele+".txt",'w')
    li.remove(ele)
    f.close()
