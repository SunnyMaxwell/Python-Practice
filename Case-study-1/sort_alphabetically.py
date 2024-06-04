n = int(input("Enter number of words as inputs: "))
words = []
for i in range(0,n):
    a = input("Enter a word: ")
    words.append(a)
words.sort()
print(words)