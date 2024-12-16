"""
    https://www.w3resource.com/python-exercises/puzzles/index.php#:~:text=3.%20Integer%20Greater,the%20sample%20solution
    4. Stone Piles Distribution

    We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must have more stones than the previous pile, but as few as possible. Write a Python program to find the number of stones in each pile.
    
    Input: 2
    Output:
    [2, 4]
    
    Input: 10
    Output:
    [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    
    Input: 3
    Output:
    [3, 5, 7]
    
    Input: 17
    Output:
    [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
    
    Click me to see the sample solution
    https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-4.php
"""

num_1 = 2
num_2 = 10
num_3 = 3
num_4 = 17

def Stones(InputNumber : int):
    stonePiles = [InputNumber]
    numOfPiles = InputNumber

    if InputNumber % 2 == 0:
        print(
            f"{InputNumber} = Even\n"
            f"{"All piles contain an Even amount of stones:\n"}"
        )
    elif InputNumber % 2 != 0:
        print(
            f"{InputNumber} = Odd\n"
            f"{"All piles contain an Odd amount of stones:\n"}"
        )    
    
    print(stonePiles, "\n")

    return

Stones(num_1)
Stones(num_2)
Stones(num_3)
Stones(num_4)