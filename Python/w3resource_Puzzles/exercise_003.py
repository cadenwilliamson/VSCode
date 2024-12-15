"""
    https://www.w3resource.com/python-exercises/puzzles/index.php#:~:text=3.%20Integer%20Greater,the%20sample%20solution
    3. Integer Greater Than 444^444 and Mod 34

    Write a Python program that accepts an integer and determines whether it is greater than 4^4 (4**4 = 256), and if n%34 is equal to 4.
    
    Input:
    922
    Output:
    4**4 = 256
    922 > 256
    True
    922 / 34 = 4
    True
    
    Input:
    914
    Output:
    4**4 = 256
    914 > 256
    True
    914 / 34 = 30
    False
    
    Input:
    854
    Output:
    4**4 = 256
    854 > 256
    True
    854 / 34 = 25
    False
    
    Input:
    745
    Output:
    4**4 = 256
    745 > 256
    True
    745 / 34 = 21
    False
    
    Click me to see the sample solution
        https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-3.php
"""

num_1 = 922
num_2 = 914
num_3 = 854
num_4 = 765

def GreaterThanFunc(InputNumber : int):
    modValue = 4 % 34 ## Gives value for 4 mod 34 (4)
    fourPower = 4 ** 4 ## Gives value of 4 to the power of 4 (256)
    sep = "-" * 50 ## Just separates text, nothing crazy
    inputModValue = InputNumber % 34


    print(sep) ## Prints separater for text readability
    
    print(
        f"Input Number: {InputNumber}\n"
        f"4 % 34 = {modValue}\n"
        f"4^4 = 4*4*4*4 = {fourPower}\n",
        f"{InputNumber} % 34 = {inputModValue}"
        )

    if InputNumber > fourPower:
        print(f"{InputNumber} > {fourPower}")
        return True

    if inputModValue == 4:
        print("")

    return



GreaterThanFunc(num_1)
GreaterThanFunc(num_2)
GreaterThanFunc(num_3)
GreaterThanFunc(num_4)