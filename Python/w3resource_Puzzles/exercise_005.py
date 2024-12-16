"""
    https://www.w3resource.com/python-exercises/puzzles/index.php#:~:text=5.%20Substring%20in,the%20sample%20solution
    5. Substring in String List Check

    Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.
    
    Input:
    ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
    Output:
    True
    
    Input:
    ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
    Output:
    False
    
    Input:
    ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
    Output:
    False
    
    Input:
    ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
    Output:
    True
    
    Click me to see the sample solution
    https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-5.php
"""

list_1 = ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
list_2 = ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
list_3 = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
list_4 = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']


def SubstringStuff(inputList : list) -> None:
    Substring = inputList[-2]
    LastString = inputList[-1]
    
    if Substring in LastString:
        print(f"'{Substring}' found in '{LastString}'\n")
        True
    else:
        print(f"'{Substring}' NOT found in '{LastString}'\n")
        False
    
    # print(fifthSub)
    # print(sixthSub, "\n")
        
SubstringStuff(list_1)
SubstringStuff(list_2)
SubstringStuff(list_3)
SubstringStuff(list_4)