"""
    https://www.w3resource.com/python-exercises/puzzles/index.php#:~:text=2.%20Fifth%20Element,the%20sample%20solution
    2. Fifth Element and List Length Check

    Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
    
    Input:
    [19, 19, 15, 5, 5, 5, 1, 2]
    Output:
    True
    
    Input:
    [19, 15, 5, 7, 5, 5, 2]
    Output:
    False
    
    Input:
    [11, 12, 14, 13, 14, 13, 15, 14]
    Output:
    True
    
    Input:
    [19, 15, 11, 7, 5, 6, 2]
    Output:
    False
    
    Click me to see the sample solution
        https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-2.php
    """

numList_1 = [19, 19, 15, 5, 5, 5, 1, 2]
numList_2 = [19, 15, 5, 7, 5, 5, 2]
numList_3 = [11, 12, 14, 13, 14, 13, 15, 14]
numList_4 = [19, 15, 11, 7, 5, 6, 2]


def ListLengthCalc(listOfNumbers : list):
    global numList_1, numList_2, numList_3, numList_4

    sep = "-" * 50
    listLength = len(listOfNumbers)
    fifthPlace = listOfNumbers[4]
    reoccurenceCount = 0

    for num in listOfNumbers:
        if num == fifthPlace:
            reoccurenceCount += 1

    print("\n", sep, "\n")
    print(f"List of Numbers: {listOfNumbers}")
    print(f"Length of List: {listLength}")
    print(f"Number in 5th Place: {fifthPlace}")
    print(f"Occurences of 5th Place Number: {reoccurenceCount}")

    if listLength == 8 and reoccurenceCount == 3:
        print("\nThis list is 8 digits long, and the 5th number occurs exactly 3 times.")
        return True
    else:
        print("\nThis list does NOT meet the requirements.")
        return False



ListLengthCalc(numList_1)
ListLengthCalc(numList_2)
ListLengthCalc(numList_3)
ListLengthCalc(numList_4)