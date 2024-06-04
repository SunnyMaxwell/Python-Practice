a = input("Enter a sentence: ")

alpha_count=0
numeric_count = 0
for i in range(len(a)):
    if a[i].isalpha():
        alpha_count += 1
    elif a[i].isdigit():
        numeric_count += 1
print("LETTERS", alpha_count)
print("DIGITS", numeric_count)