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
user_input=int(input("what do you want to choose? Type 0 for rock, 1 for paper and 2 for scissors\n"))

game_control_list=[rock,paper,scissors]
if user_input>=3 or user_input < 0:
  print("invalid input...get lost")
else:
  print(game_control_list[user_input])

  bot_input=random.randint(0,2)
  print(game_control_list[bot_input])

  if user_input==bot_input:
    print("it's a DRAW....")
  elif user_input==0:
    if bot_input == 1:
      print("you LOSE")
    elif bot_input == 2:
      print ("you WIN")
  elif user_input==1:
    if bot_input==0:
      print("You WIN")
    elif bot_input==2:
      print("you LOSE")
  elif user_input==2:
    if bot_input== 0:
      print("you LOSE")
    elif bot_input==1:
      print("you WIN")

  if user_input==bot_input:
    print("it's a draw.....")
  elif (user_input==0 and bot_input==1) or (user_input==1 and bot_input==2) or(user_input==2 and bot_input==0):
    print("you lose")
  elif (user_input==0 and bot_input==2) or (user_input==1 and bot_input==0) or(user_input==2 and bot_input==1):
    print("you win")


