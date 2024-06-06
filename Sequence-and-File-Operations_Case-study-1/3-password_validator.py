User_name =  input("Enter User_name: ")

has_lower = False
has_upper = False
has_digit = False
has_special_charector = False
special_charectors = "$#@"

count = 0
while count<=0:
    Pass_wd = input("Enter password: ")
    l = len(Pass_wd)
    if (6<=l<=12):
        for i in Pass_wd:
            if i.isupper():
                has_upper = True
            elif i.islower():
                has_lower = True
            elif i.isnumeric():
                has_digit = True
            elif i in special_charectors:
                has_special_charector = True
    if has_digit and has_lower and has_special_charector and has_upper:
        print("User is Created with Username: %s" %(User_name))
        count+=1
    else:
        print("The Enter Password is week. \nPlease make sure the following criteria \n \
                1. At least 1 letter between [a-z] \n \
                2. At least 1 number between [0-9] \n \
                3. At least 1 letter between [A-Z] \n \
                4. At least 1 character from [$#@] \n \
                5. Minimum length of transaction password: 6 \n \
                6. Maximum length of transaction password: 12 \n"
            )
