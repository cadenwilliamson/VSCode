"""
    This is a random number guessing game. First you choose if you want to choose between 1 and 50, or 1 and 100.
    Then you just keep guessing the number, and when you guess it, you win!
"""
def RandomNumberGame():
    import random as r
    
    # Generates a random number between the given values.
    rand_num_100 = r.randint(1, 101)     # Range between 1 and 100
    rand_num_50 = r.randint(1, 51)       # Range between 1 and 50
    
    # Asks user which gamemade they want to play.
    userInput_gamemode = int(input("Press 1 to guess between 1 and 100\nPress 2 to guess between 1 and 50\n"))
    
    # Determins which gamemode was selected.
    if userInput_gamemode == 1:
        randNumber = rand_num_100
        gamechoice = "Guess a number between 1 and 100!\n"
    elif userInput_gamemode == 2:
        randNumber = rand_num_50
        gamechoice = "Guess a number between 1 and 50!\n"
    
    # Displays the game start message
    print(gamechoice, "\n")
    
    # Main Game loop
    while True:
        userInput_guess = int(input("Guess a Number: "))
        
        if userInput_guess == randNumber:
            print(f"\nCorrect! The number was {randNumber}!\nYou Win!!!\n")
            return False
        elif userInput_guess > randNumber:
            print(f"Nope! Try a lower number!")
        elif userInput_guess < randNumber:
            print(f"Nope! Try a higher number!")