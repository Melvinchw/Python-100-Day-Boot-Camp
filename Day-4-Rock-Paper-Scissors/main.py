import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#Welcome message
print("Welcome to the Rock, Paper, Scissors Challenge!")
#Input prompt
answer = int(input("To play, please key 0 for 'Rock', 1 for 'Paper', 2 for 'Scissors': "))

if answer >= 3 or answer < 0:
  print("Invalid input. Please try again.")
else:
#Result generation
  results = random.randint(0,2)

#Create list
  list = [rock, paper, scissors]
  list2 = ["Rock", "Paper", "Scissors"]

#Print selection
  print(list[int(answer)])
  print(f"Your choice is: {list2[int(answer)]}")
  print(list[results])
  print(f"Computer chose: {list2[results]}")

#Comparison if draw
  if answer == results:
    print("It's a Draw!")

#Comparison if 0
  if answer == 0:
    if results == 1:
      print("You lose!")
    elif results == 2:
      print("You win!")

#Comparison if 1
  if answer == 1:
    if results == 0:
      print("You win!")
    elif results == 2:
      print("You lose!")

#Comparison if 2
  if answer == 2:
    if results == 1:
     print("You win!")
    elif results == 0:
     print("You lose!")