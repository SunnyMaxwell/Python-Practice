from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
encrypted_flag = False
reference_ID = input("Enter your reference_ID: ")
special_characters = '[$#@^*]'
if len(reference_ID) == 12:
    for i in reference_ID:
        if i in special_characters or reference_ID.isalnum():
            encrypted_string = f.encrypt(reference_ID.encode())
            encrypted_flag = True
            print("Hi Your Encrypted String for Your Reference ID is ",encrypted_string)
            decrypted_string = f.decrypt(encrypted_string)
            break
    
else:
    print("Invalid Reference Number Please try again")

if encrypted_flag :
    option = input("Hi do you need to decrypt for your Reference ID? Yes or No ")
    if (option == "Yes"):
        print("Your Decrypted String is: ", decrypted_string)

'''
output:

Case-1
Enter your reference_ID: 123asd$#@1wd
Hi Your Encrypted String for Your Reference ID is  b'gAAAAABmYSWisMHs6ctf_FJUWfg7IH2chiyZK0vYBcfdN9fIfTgNRSgsQU0FA9yXD5_NKk8_O_EKjgdO3-4c3hfNtNFO6rpRMQ=='
Hi do you need to decrypt for your Reference ID? Yes or NoYes
Your Decrypted String is:  b'123asd$#@1wd'

Case-2
Enter your reference_ID: scdvfsdfdsaaw322
Invalid Reference Number Please try again
'''