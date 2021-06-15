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

choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n "))

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)

print("computer chose")

computer_choice = random.randint(0,2)
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)


# GAME LOGIC
if choice > computer_choice:
  if choice == 1:
    print("You win")
  elif choice == 2 and computer_choice != 0:
    print("You win")
  else:
    print("you lose")
elif choice == computer_choice:
  print("Draw")
else:
  print("You lose")
  