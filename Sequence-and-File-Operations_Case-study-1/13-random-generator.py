import random
# for i in range(1,1000):
mylist = []

for i in range(1,1000):
    if len(mylist) < 5:
        a = random.randint(1,1000)
        if ( (a%5 == 0) and (a%7 == 0) ):
            mylist.append(a)
        else:
            continue
print(mylist)