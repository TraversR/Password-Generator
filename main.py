# Password Generator
# Travers Rollston
# 7/15/2021

import string
import random


def save_pass(generated):


    yorno_input = str(input("\n Enter a 1 to save password to a file, or just press enter to continue without saving"))
    if yorno_input == "1":

        print("Saving...")
        file = open('savedpass.txt', 'a')
        file.write("Password: " + generated + "\n \n")

        file.close()
        print("Password Saved. \n")
    else:
        print("Not saved \n")


# define generator
def generator(pass_type, pass_length):
    if pass_type == 1:
        generated = ''.join(random.choice(string.ascii_letters) for i in range(pass_length))
        print(generated)
        save_pass(generated)
    elif pass_type == 2:
        nlcharacters = string.ascii_letters + string.digits
        generated = ''.join(random.choice(nlcharacters) for i in range(pass_length))
        print(generated)
        save_pass(generated)
    elif pass_type == 3:
        nlscharacters = string.ascii_letters + string.digits + string.punctuation
        generated = ''.join(random.choice(nlscharacters) for i in range(pass_length))
        print(generated)
        save_pass(generated)
    else:
        print("not 1")


generating = True
# begin generating loop to get user input for type and length of password

while generating == True:

    valid_type = False
    while valid_type == False:
        try:
            print("------------------------------------------------------------------------------------")
            pass_type = int(input(
                "Enter the number for the type of password you'd like: \n 1.Letters Only \n 2.Numbers and Letters \n 3,Numbers, Letters, and Special Characters"))
            print("------------------------------------------------------------------------------------ \n")
            if pass_type >= 0 and pass_type <= 3:
                valid_type = True
        except:
            print("This field requires a numerical input of 1, 2 or 3.")
            continue
    valid_length = False
    while valid_length == False:

        try:

            pass_length = int(input("Enter the length of password desired."))
            if pass_length > 0:
                vslid_length = True
                print("------------------------------------------------------------------------------------ \n")
                print("Your generated password is: ") + generator(pass_type, pass_length) + "\n"
                print("None from here")
                break

        except:

            break
