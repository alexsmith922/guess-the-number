#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

# print(logo)

RANDOM_NUMBER = random.randint(1, 101)

print(RANDOM_NUMBER)

print("Welcome to the Guessing Game!\nI'm thining of a number between 1 and 100.")
difficulty = input("Pick your poison. Type 'easy' or 'hard': ") == "easy"

def guess_selector(difficulty):
  if difficulty == "easy":
    user_guesses = 10
    return user_guesses
  elif difficulty == "hard":
    user_guesses = 5
    return user_guesses
  else:
    print("Try again homeslice")
    guess_selector(difficulty)

guess_selector(difficulty)

  
