'''
url = https://www.w3resource.com/python-exercises/cybersecurity/python-cybersecurity-exercise-1.php
1. Write a Python program that defines a function and takes a password string as input and returns its SHA-256 hashed representation as a hexadecimal string.
Click me to see the sample solution
'''
import hashlib

# userInput = input("Input Password to Hash...\n")

def passHash(password : str) -> hash:
    
    encoded = password.encode('utf-8')
    hash_obj = hashlib.sha256(encoded)
    hex_hash = hash_obj.hexdigest()
    
    return hex_hash

userInput = "password"
hashed_password = passHash(userInput)
print(f"Your hashed password is: {hashed_password}")