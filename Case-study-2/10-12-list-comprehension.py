# 1 - By using list comprehension, please write a program to print 
#the list after removing the value 24 in [12,24,35,24,88,120,155]

a = [12,24,35,24,88,120,155]

print("the list after removing 24 ", [i for i in a if i != 24])

# By using list comprehension, 
#please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
a = [12,24,35,70,88,120,155]

print("The list after removing the indexs of 0th,4th,5th are ",[a[i] for i in range(0,len(a)) if i not in [0,4,5]])

#By using list comprehension, 
#please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

a = [12,24,35,70,88,120,155]

print("the list that are divisible by both  5 and 7 are",[ a[i] for i in range(len(a)) if ((a[i]%5 == 0) and (a[i]%7) == 0) ])
