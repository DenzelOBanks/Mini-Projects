import random
import string

def generate_password(min_length, numbers=True, special_character=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers: #if numbers is True add digits to the password
        characters += digits
    if special_character:
        characters += special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length: #while we dont meet criteria or password less than minimum lenght keep adding to password
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers: # if we have an number
            meet_criteria = has_number #if we do it = true else will be false
        if special_character:
            meet_criteria = meet_criteria and has_special #if we have a number and a special character it will be true if we have only one it will be false
    
    return pwd

min_length = int(input("Enter the minimum length "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y" #.lower() converts the input to lower case and checks if it == to y if so it is true
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is: " + pwd)