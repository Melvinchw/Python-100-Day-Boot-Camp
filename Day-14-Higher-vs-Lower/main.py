from replit import clear
from game_data import data
from art import logo
from art import vs
import random

def  compare(user_input, a, b):
  if a > b:
    return user_input == 'a'
  else:
    return user_input == 'b'
def  format_data(account):
  name = account['name']
  description = account['description']
  country = account['country']
  return (f"{name}, a {description}, from {country}")

print (logo)
account_b = random.choice(data)
should_continue = True
score = 0

while should_continue:
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)
  
  
  print(f"Compare A: {format_data(account_a)}")
  print (vs)
  print(f"Against B: {format_data(account_b)}")
  
  user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
  a = account_a['follower_count']
  b = account_b['follower_count']
  clear()
  print(logo)
  is_correct = compare(user_input, a, b)
  if is_correct:
    score += 1
    print(f"You got it right. Current score: {score}")
  else:
    should_continue = False
    print(f"You got it wrong. Final score: {score}")
  