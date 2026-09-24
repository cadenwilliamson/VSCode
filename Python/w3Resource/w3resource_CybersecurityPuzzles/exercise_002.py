'''
2. Write a Python program that defines a function to generate random passwords of a specified length. The function takes an optional parameter length, which is set to 8 by default. If no length is specified by the user, the password will have 8 characters.
Click me to see the sample solution
'''
from string import printable
import random

def randPassGen(passLength):
    
    if type(passLength) is not int:
        print("Not integer, try again...\n")
        exit()
    
    if passLength < 8:
        print("Password must be at least 8 characters long.")
        passLength = 8
    
    print(f"Password Length: {passLength}")
    
    # Remove all whitespace characters (space, newline, tab, etc.) from printable
    printable_filtered = "".join(char for char in printable if not char.isspace())
    
    pw = ""
    
    for _ in range(passLength):
        pw += random.choice(printable_filtered)
    
    print(f"Generated Password:\n{pw}")

try:
    userInput = int(input("Please input required password length...\n"))
except ValueError:
    print("Input must be an integer. Exiting...")
    exit()

randPassGen(userInput)