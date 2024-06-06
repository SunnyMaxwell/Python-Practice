a = [12,24,35,24,88,120,155,88,120,155]

remove_duplicates ={}

for i in range(len(a)):
    if remove_duplicates.get(a[i]) == None:
        remove_duplicates[a[i]] = 1
    else:
        remove_duplicates[a[i]] += 1
print( [i for i in remove_duplicates.keys()])


