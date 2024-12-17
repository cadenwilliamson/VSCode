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
        This function takes the re(regex) module, and uses it to split the strings into lists.
        
        The regex formula used is 'r"([ ,]+)"'
        
        Breakdown:
        r = Prefix that marks the string as a "raw string".
            -"\" are treated literally.
        ( .. ) = Capturing Group, grouping each occurence of the regex.
        [] = Defines a "Character Class". "One of" the included expression.
        " ," = This is what the regex is looking for. Both a space, and a comma
        + = Looks for one, or more, space or comma, of the previous pattern.
    """
    splitList = re.split(r"([ ,]+)", inputString)
    
    print(sep)
    print(f"Input String:\n{inputString}\n")
    print("Seperated Words List:")
    
    """
        Breakdown:
        Creating a list with two sublists using the "splitList" variable.
        
        [] = Meaning "list"
        splitList = The output of the variable "splitList"
        [::2] = Creating the sublist using "slicing syntax" [start:stop:step]. 
            Blank spaces indicate the defaults, both beginning and end of the list.
            The ":2" takes every second element, starting at 0.
        [1::2] = Similar to the previous slicing, but starts at the 1st index (second element)
    """
    print([splitList[::2]], "\n") 
    print("Seperated Punctuation List:")
    print([splitList[1::2]], "\n")

StringSplitter(exampleString_1)
StringSplitter(exampleString_2)
StringSplitter(exampleString_3)