import random

rock = '''
    _______
---'   ____)
      (______)
      (_______)
      (______)
---.__(_____)
'''

paper = '''
    _______
---'   ____)______
          ________)
          __________)
         _________)
---.____________)
'''

scissors = '''
    _______
---'   ____)______
          ________)_
       _____________)
      (_____)
---.__(____)
'''

#Write your code below this line 👇
player_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors!\n"))
computer_hand = random.randint(0, 2) 
hands = [rock, paper, scissors]

if player_hand < 3 and player_hand >= 0:
  print("You chose:")
  print(hands[player_hand])
  
  print("Computer chose:")
  print(hands[computer_hand])
  
  if player_hand == (computer_hand + 1) or player_hand == 0 and computer_hand == 2:
    print("You win!")
  elif player_hand == computer_hand:
    print("Draw.")
  else:
    print("You lose.")
else: 
  print("Invalid choice! You lose.")