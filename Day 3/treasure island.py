print('''
********************************************************************************
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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction1=input('you are at cross road. Where do you want to go? Type "left" or "Right."\n')
dir_1=direction1.lower()

if dir_1 == "left":
  direction2= input('you came to a lake.there is an island in the middle of the lake.Type "wait" to wait or type "swin" to swim across \n')
  dir_2=direction2.lower()

  if dir_2 == "wait":
    colour=input('You arrive at the island unharmed. there is a house with 3 door. 1 red,1 yellow, & 1 blue. Which colour do you choose \n')
    colour=colour.lower()

    if colour == "yellow":
      print("You Win!")
    elif colour == "red":
      print("Bruned by fire.Game Over")
    elif colour=="blue":
      print("eaten by beast.Ha Ha Ha")
  else:
    print("You are attack by trut.Game Over")

else:
  print("you fell in a hole. Game Over")

# input("You're at a cross road. Where do you want to go? Type "+'"Left or Right" ')
# input("You came to a lake. There is an isalnd in the middle of the lake." + 'Type "wait" to wait for a boat'+'Type "swim" to swim across')
