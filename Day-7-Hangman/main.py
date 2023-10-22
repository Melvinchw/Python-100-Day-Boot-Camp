import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages
from hangman_art import win
from hangman_art import lose
from replit import clear

#choose word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Set used and wrong list
used_list = []
wrong_list = []

#set game condition
end_of_game = False
lives = 6

#Start of game: Game logo
print(logo)
print(chosen_word)
#Create blanks for word generated
display = []
for _ in range(word_length):
    display += "_"

#Start of game: Get input
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
#Check if guess is used before
    if guess in used_list:
      print(f"These letters have been used before: {used_list}")
      print(f"Wrong list: {wrong_list}")
      print("You have chosen this letter before. Please try again!")
    else:
      used_list += guess

#Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

#Check if user is wrong.
    if guess not in chosen_word:
      
#Check if wrong word is in used list
      if guess not in wrong_list:
          wrong_list += guess
          lives -= 1
      print("Wrong letter chosen. Please try again!")
        
#End game if lives becomes zero
      if lives == 0:
          end_of_game = True
          print(f"You lose.\n{lose}")

#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

#Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(f"You win.\n{win}")

#Print number of lives left
    print(stages[lives])