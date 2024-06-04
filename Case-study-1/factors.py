a = int(input("Enter a number: "))
factors={}
for i in range(1,a+1):
    if a%i == 0:
        if i%2 == 0:
            factors[i] = "even"
        else:
            factors[i] = "odd"
print("The factors of given number, followed by its integer types are", factors)