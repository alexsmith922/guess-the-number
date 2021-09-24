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

print(logo)

RANDOM_NUMBER = random.randint(1,101)

print(RANDOM_NUMBER)

print("I'm thinking of a number...between 0 and 100")
user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if user_difficulty == "easy":
  user_guesses_remaining = 10
  print(f"You have {user_guesses_remaining} attempts remaining")
if user_difficulty == "hard":
  user_guesses_remaining = 5
  print(f"You have {user_guesses_remaining} attempts remaining")

user_guess = int(input("Make a guess: "))

while user_guesses_remaining != 0 and user_guess != RANDOM_NUMBER:
  second_guess = int(input("Guess again: "))
  if second_guess > RANDOM_NUMBER:
    user_guesses_remaining -= 1
    print(f"Too high.\nGuess again.\nYou have {user_guesses_remaining}attempts remaining to guess the number")
  elif second_guess < RANDOM_NUMBER:
    user_guesses_remaining -=1
    print(f"Too low.\nGuess again.\nYou have {user_guesses_remaining} attempts remaining to guess the number")
  elif second_guess == RANDOM_NUMBER:
    print("You win!")
  
