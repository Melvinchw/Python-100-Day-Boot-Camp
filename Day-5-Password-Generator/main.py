#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

if nr_letters > 52 or nr_numbers > 10 or nr_symbols > 9:
  print("Invalid input. Please try again!")

else:
  rdm_letters = []
  random_letter = 0
  for letter in range(0,nr_letters):
    random_letter = random.randint(0, 51)
    rdm_letters.append(letters[random_letter])
  
  rdm_symbols = []
  random_symbols = 0
  for symbol in range(0,nr_symbols):
    random_symbols = random.randint(0, 8)
    rdm_symbols.append(symbols[random_symbols])
  
  rdm_numbers = []
  random_numbers = 0
  for number in range(0,nr_numbers):
    random_numbers = random.randint(0, 9)
    rdm_numbers.append(numbers[random_numbers])
  
  password = rdm_letters + rdm_numbers + rdm_symbols
  random.shuffle(password)
  password = ''.join(str(item) for item in password)
  print(f"Your password is:\n{password}\nPlease do not share this information with anyone else!\nThank you for using my password generator!")
  
  