import random
from art import logo
from os import system, name

# Defining clear
def clear():    
    if name == 'nt': 
        _ = system('cls')

# Defining main game function
def play_game():
    
    print(logo)
    game_still_going = True
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")   
    # Computer chooses random number in range
    random_number = random.randrange(1, 101)
    
    # Choosing difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")      
    attempts = 0  
    if difficulty == 'easy':
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif difficulty == 'hard':
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number.")
    
    # While loop to let the player guess again
    while game_still_going:        
        
        guess = int(input("Make a guess: "))
        if guess < random_number:
            print("Too low.\nGuess again.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess > random_number:
            print("Too high.\nGuess again.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess == random_number:
            print(f"You got it! The number was {random_number}")
            game_still_going = False
            while input("Do you want to play another game? Type 'y' or 'n': ") == "y":
                clear()
                play_game()
        
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            game_still_going = False
            # Asking if the player wants to play again
            if input("Do you want to play another game? Type 'y' or 'n': ") == "y":
                clear()
                play_game()
            else:
                quit

play_game()