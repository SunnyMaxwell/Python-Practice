a = input("Enter a string to count each charactor: ")
count_character = {}

for i in range(len(a)):
    if count_character.get(a[i]) == None:
        count_character[a[i]] = 1
    else:
        count_character[a[i]] += 1
print(count_character)