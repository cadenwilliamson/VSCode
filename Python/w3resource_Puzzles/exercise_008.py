"""
    https://www.w3resource.com/python-exercises/puzzles/index.php#:~:text=8.%20Split%20String,the%20sample%20solution
    8. Split String into Words and Separators

    Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.
    
    Input: W3resource Python, Exercises.
    Output:
    [['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
    
    Input: The dance, held in the school gym, ended at midnight.
    Output:
    [['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
    
    Input: The colors in my studyroom are blue, green, and yellow.
    Output:
    [['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]
    
    Click me to see the sample solution
    https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-8.php
"""

exampleString_1 = "W3resource Python, Exercises."
exampleString_2 = "The dance, held in the school gym, ended at midnight."
exampleString_3 = "The colors in my studyroom are blue, green, and yellow."

def StringSplitter(inputString : str):
    import re
    
    sep = "-" * 70
    
    """
        The beef of this function is here.
        This function takes the re(regex) library, and uses it to split the strings into lists.
        
        First, an 'r' is used to signify that what is within the following string is using
        regex. Then, a regex formula is surrounded by parenthases(). This isolates the action,
        and basically takes each thing that it finds in the given string that meets the criteria
        of the regex expression, and makes it it's own item in the list.
        
        The regex formula used is '([ ,]+)'
        
        Breakdown:
        
    """
    splitList = re.split(r"([ ,]+)", inputString)
    
    print(sep)
    print(f"Input String:\n{inputString}\n")
    print("Seperated Words List:")
    print([splitList[::2]], "\n") 
    print("Seperated Punctuation List:")
    print([splitList[1::2]], "\n")

StringSplitter(exampleString_1)
StringSplitter(exampleString_2)
StringSplitter(exampleString_3)