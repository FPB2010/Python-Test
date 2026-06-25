#!/usr/bin/env python3
"""
Number Guessing Game

A simple console-based game where the player tries to guess a randomly generated number.
"""

import random
import sys
from typing import Optional

class NumberGuessingGame:
    def __init__(self, min_number: int = 1, max_number: int = 100):
        """
        Initialize the game with a range of numbers.
        
        Args:
            min_number: The minimum possible number (inclusive)
            max_number: The maximum possible number (inclusive)
        """
        self.min_number = min_number
        self.max_number = max_number
        self.target_number = random.randint(min_number, max_number)
        self.attempts = 0
        self.max_attempts = (max_number - min_number + 1) // 2  # Rough estimate
        self.game_over = False
        self.won = False
    
    def display_welcome(self) -> None:
        """Display the welcome message and game instructions."""
        print("\n" + "="*50)
        print("🎮 NUMBER GUESSING GAME 🎮")
        print("="*50)
        print(f"I'm thinking of a number between {self.min_number} and {self.max_number}")
        print(f"You have approximately {self.max_attempts} attempts to guess it!")
        print("\nEnter your guess when prompted.")
        print("I'll tell you if your guess is too high or too low.")
        print("="*50 + "\n")
    
    def get_player_guess(self) -> Optional[int]:
        """
        Get the player's guess with input validation.
        
        Returns:
            The player's guess as an integer, or None if they want to quit
        """
        while True:
            try:
                guess_input = input(f"Guess a number ({self.min_number}-{self.max_number}) or type 'quit' to exit: ")
                
                if guess_input.lower() in ['quit', 'exit', 'q']:
                    return None
                
                guess = int(guess_input)
                
                if guess < self.min_number or guess > self.max_number:
                    print(f"Please enter a number between {self.min_number} and {self.max_number}.")
                    continue
                
                return guess
                
            except ValueError:
                print("Please enter a valid number.")
                continue
    
    def check_guess(self, guess: int) -> bool:
        """
        Check if the guess is correct and provide feedback.
        
        Args:
            guess: The player's guess
            
        Returns:
            True if the guess is correct, False otherwise
        """
        self.attempts += 1
        
        if guess == self.target_number:
            self.won = True
            self.game_over = True
            return True
        elif guess < self.target_number:
            print("Too low! Try a higher number.")
            return False
        else:
            print("Too high! Try a lower number.")
            return False
    
    def display_result(self) -> None:
        """Display the final game result."""
        print("\n" + "="*50)
        if self.won:
            print("🎉 CONGRATULATIONS! 🎉")
            print(f"You guessed the number {self.target_number} correctly!")
            print(f"It took you {self.attempts} attempt(s).")
            
            # Performance feedback
            if self.attempts == 1:
                print("🔥 Lucky guess! Perfect!")
            elif self.attempts <= self.max_attempts:
                print("👏 Great job! You did it within the expected attempts!")
            else:
                print("👍 Good job! You figured it out!")
        else:
            print("😢 GAME OVER!")
            print(f"The number I was thinking of was {self.target_number}.")
            print(f"You made {self.attempts} attempt(s).")
        
        print("="*50 + "\n")
    
    def play_again(self) -> bool:
        """
        Ask the player if they want to play again.
        
        Returns:
            True if the player wants to play again, False otherwise
        """
        while True:
            choice = input("Would you like to play again? (yes/no): ").lower().strip()
            
            if choice in ['yes', 'y', 'sure', 'ok']:
                return True
            elif choice in ['no', 'n', 'nope', 'quit']:
                return False
            else:
                print("Please enter 'yes' or 'no'.")
                continue
    
    def run(self) -> None:
        """Main game loop."""
        while True:
            # Initialize new game
            self.target_number = random.randint(self.min_number, self.max_number)
            self.attempts = 0
            self.game_over = False
            self.won = False
            
            # Display welcome message
            self.display_welcome()
            
            # Game loop
            while not self.game_over:
                guess = self.get_player_guess()
                
                # Handle quit
                if guess is None:
                    print("\nThanks for playing! Goodbye! 👋")
                    return
                
                # Check the guess
                if self.check_guess(guess):
                    # Display result
                    self.display_result()
                    
                    # Ask to play again
                    if not self.play_again():
                        print("\nThanks for playing! See you next time! 🎲")
                        return
                    break  # Break to start new game

def main() -> None:
    """Main entry point for the game."""
    print("Starting Number Guessing Game...")
    
    try:
        game = NumberGuessingGame()
        game.run()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()