#!/usr/bin/env python3
"""
A simple number guessing game.

The user has to guess a random number between 1 and 100.
After each guess, the program tells the user whether to guess higher or lower.
The game continues until the user guesses the correct number.
"""

import random
import sys


def play_game():
    """Play the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = input("Enter your guess (or 'q' to quit): ")
            
            # Allow user to quit
            if guess.lower() == 'q':
                print(f"Thanks for playing! The number was {secret_number}.")
                break
            
            # Convert input to integer
            guess = int(guess)
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("Too low! Try guessing higher.")
            elif guess > secret_number:
                print("Too high! Try guessing lower.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break
                
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")


def main():
    """Main function to run the game."""
    try:
        # Check if the user wants to play in interactive mode
        if len(sys.argv) > 1 and sys.argv[1] == '--quick':
            # Quick mode: play one game and exit
            play_game()
        else:
            # Interactive mode: ask if user wants to play
            while True:
                response = input("Do you want to play a number guessing game? (y/n): ").lower()
                if response == 'y':
                    play_game()
                elif response == 'n':
                    print("Goodbye!")
                    break
                else:
                    print("Please enter 'y' or 'n'.")
                    
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()