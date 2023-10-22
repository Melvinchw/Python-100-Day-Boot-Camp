#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

#generate a number from 1-100
#input easy or hard
#if easy 10 lives
#if hard 5 lives
#input guess, if correct end, if wrong -1live. compare more or less than number

import random
from replit import clear
from art import logo

def game():
  print(logo)
  number = random.randint(0, 100)
  print("Welcome to the number guess game!")
  print("I am thinking of a number from 1 - 100")
  user_choice = input("Do you want to play the game in easy or hard mode?: ")
  
  if user_choice == 'easy':
    i = 10
  elif user_choice == 'hard':
    i = 5
  print(f"You have {i} lives")
  while i != 0:
    guess = int(input("Make a guess: "))
    if guess == number:
      i = 0
      print("You win!")
    elif guess < number:
      i -= 1
      print("Too low.")
      print(f"You have {i} lives left. Try again!")
    elif guess > number:
      i -= 1
      print("Too high.")
      print(f"You have {i} lives left. Try again!")
  if guess != number:
      print("You have ran out of lives! Better luck next time")

new_game = True
while new_game:
  game()
  user = input("Press 'Y' for a new game or 'N' to pass.").lower()
  if user == 'y':
    clear()
  elif user == 'n':
    new_game == False
  else:
    print("Invalid input. Game will end!")
    new_game == False