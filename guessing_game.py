# Created by Paul A. Gureghian in Oct 2020.

# Import library
import random

# Generate a new random number
def new_rand_num_generator():

    return random.randint(1, 10)

# Define 'start_game' function

def start_game():

    number_of_attempts = 0;

    print("")
    print("---------------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("---------------------------------------")
    print("")

    # Generate a randon number between 1 - 10
    rand_num = new_rand_num_generator()
    
    # Get user number
    number = int(input("Enter a number between 1 and 10: "))
    print("")

    if number > rand_num:
        print("It's lower")

    elif number < rand_num:
        print("It's higher")

    else:
        print("Got it")
        
    print("The game is over\n")    

start_game()
