# Python-Test Repository

This repository contains a simple Python number guessing game for testing purposes.

## Description

A basic console-based number guessing game where the user tries to guess a randomly generated number between 1 and 100. The game provides hints ("too high" or "too low") after each guess to help the user find the correct number.

## Features

- Random number generation between 1 and 100
- Interactive console interface
- Input validation for non-numeric input
- Option to quit the game at any time
- Two game modes:
  - **Quick mode**: Play one game and exit (use `--quick` flag)
  - **Interactive mode**: Choose to play multiple games

## How to Play

1. Run the game: `python number_guessing_game.py`
2. Enter your guess when prompted
3. Get hints to help you guess the correct number
4. Type 'q' to quit at any time

### Quick Play

For a quick test, you can run:
```bash
python number_guessing_game.py --quick
```

## Files

- `number_guessing_game.py` - The main game implementation

## Requirements

- Python 3.x

## License

This is a test repository for demonstration purposes.