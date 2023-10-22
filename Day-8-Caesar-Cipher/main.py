#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
"""def encrypt(txt, shft):
  textlen = len(txt)

  encryptedtxt = ""
  for position in range(textlen): 
    if txt[position] in alphabet:
      oldindex = alphabet.index(txt[position])
      newindex = (oldindex + shift) % len(alphabet) 
      encryptedtxt += alphabet[newindex]
      
  print(f"The encoded message is {encryptedtxt}")"""

"""def decrypt(txt, shft):
  textlen = len(txt)

  decryptedtxt = ""
  for position in range(textlen):
    oldindex = alphabet.index(txt[position])
    newindex = (oldindex - shft) % len(alphabet)
    decryptedtxt += alphabet[newindex]
  print(f"The decoded message is {decryptedtxt}")
"""
def casesar(dir, txt, shft):
  newtxt = ""
  textlen = len(txt)
  if dir == "decode":
      shft *= -1
  for letter in txt:
    if letter in alphabet:
      oldindex = alphabet.index(letter)
      newindex = (oldindex + shft) % len(alphabet)
      newtxt += alphabet[newindex]
    else:
      newtxt += letter
  print(f"The {dir} message is {newtxt}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

programme = True
while programme:
  casesar(dir = direction, txt = text, shft = shift)
  reuse = input("Would you like to use the programme again? Please insert 'Yes' or 'No': ").lower()
  if reuse == "yes":
    programme = True
  elif reuse == "no":
    programme = False
print("Thank you for using the Caesar Cipher Machine. Thank you. Bye Bye!")