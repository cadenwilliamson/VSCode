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
    fourPower = 4 ** 4 # = 256
    inputModValue = InputNumber % 34
    sep = "-" * 50 ## Just separates text, nothing crazy

    print(sep) ## Prints separater for text readability

    print(
        f"Input Value: {InputNumber}\n"
        "4 ** 4 = 256\n"
        f"{InputNumber} % 34 = {inputModValue}\n"
    )

    if InputNumber > fourPower and inputModValue == 4:
        print(
            f"{InputNumber} is 'Greater Than' 4 ** 4 = 256.\n"
            f"{InputNumber}, when 'n%34' is applied, is equal to 4."
        )
        return True
    else:
        print("The given number does not meet the required criteria.")
        return False


GreaterThanFunc(num_1)
GreaterThanFunc(num_2)
GreaterThanFunc(num_3)
GreaterThanFunc(num_4)