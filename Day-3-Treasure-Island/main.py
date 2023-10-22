print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Laughtale.")
print("Your mission is to find the Great Treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input('Your New World logpost have registered 2 readings. Please choose "Left" or "Right". ').lower()

if direction == "right":
  print("You ended up at Marineford. Straight to Impel Down you go")

else:
  print("Nami continued navigating Thousand Sunny as you approaches Laughtale...")
  action = input('A whirlpool is preventing you from entering Laughtale. Do you want to "Swim" or "Wait"? ').lower()

  if action == "wait":
    print("The whirlpool sucks Thousand Sunny in along with the crew. The End")
  else:
    print("As you jumped into the Ocean, the whirlpool subsided.")
    land = input('As Laughtale comes in sight, you noticed the 3 places where it is safe to go ashore. "Dock", "Beach", "Underground Cave". Which will you choose? ').lower()

    if land == "dock":
      print("Garp's ship was hiding in ambush. He smashed your crew with Galaxy Impact.")
    elif land == "beach":
      print("Booby traps laid down by the Roger Pirates using the ancient weapons wipes out your crew.")
    elif land == "underground cave":
      print("As you enter the cave, you notice a familiar figure. It was none other than Oda himself. Handing you the One Piece and crowning you the Pirate King, drawing One Piece to a close after 30 years.")
    else:
      print("Wrong Choice. You got teleported back to where you first started. This time without the Gomu Gomu No Mi.")