a = int(input("Enter a number: "))
original_Temp = a
reverseNum = 0

while a > 0:
    rem = a % 10
    reverseNum = reverseNum * 10 + rem
    a //=10
if original_Temp == reverseNum:
    print("The Given Number is Palindrome number")
else:
    print("The Given Number is Not Palindrome number")

# Method 2

rever_num = str(original_Temp)[::-1]
if original_Temp == int(rever_num):
    print("The Given Number is Palindrome number - Method-2")
else:
    print("The Given Number is Not Palindrome number - Method-2")