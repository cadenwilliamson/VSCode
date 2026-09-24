"""
    https://www.w3resource.com/python-exercises/puzzles/index.php#:~:text=1.%20Check%20Nineteen,the%20sample%20solution
    1. Check Nineteen and Five Occurrences

    Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
    Input:
    [19, 19, 15, 5, 3, 5, 5, 2]
    Output:
    True
    Input:
    [19, 15, 15, 5, 3, 3, 5, 2]
    Output:
    False
    Input:
    [19, 19, 5, 5, 5, 5, 5]
    Output:
    True
    
    Click me to see the sample solution
        https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-1.php
"""

numList_1 = [19, 19, 15, 5, 3, 5, 5, 2]
numList_2 = [19, 15, 15, 5, 3, 3, 5, 2]
numList_3 = [19, 19, 5, 5, 5, 5, 5]

def DigitOccurrences(listOfNumbers : list):
    """_summary_

    Args:
        listOfNumbers (list): This is a list that's given to the function to parse through.

    Returns:
        _type_: Should return True or False, if it meets the criteria.
    """
    
    global numList_1, numList_2, numList_3

    fiveCount = 0
    nineteenCount = 0
    sep = "-" * 50


    for number in listOfNumbers:
        if number == 5:
            fiveCount += 1
        elif number == 19:
            nineteenCount += 1
    
    print(sep, "\n")
    print(f"List of Numbers: {listOfNumbers}")
    print(f"Occurences of 5: {fiveCount}")
    print(f"Occurences of 19: {nineteenCount}\n")
    
    
    if nineteenCount != 2:
        print("List does NOT have exactly 2 occurences of 19.")
        return False
    
    if fiveCount < 3:
        print("List does NOT have 3 or more occurences of 5.")
        return False
    
    if nineteenCount == 2 and fiveCount >= 3:
        print("List meets both requirements!")
        return True

DigitOccurrences(numList_1)
DigitOccurrences(numList_2)
DigitOccurrences(numList_3)