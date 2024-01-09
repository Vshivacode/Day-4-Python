# Rock, Paper, Scissors Game
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

game = [rock, paper, scissors]
user_choice = int(input("enter your choice: 0 for rock, 1 for paper, 2 for scissor: "))
print(game[user_choice])
computer_choice = random.randint(0,2)
if user_choice == 0 and computer_choice == 2:
    print(f"computer choice: {game[computer_choice]}")
    print("you won")
elif user_choice == 1 and computer_choice == 0:
    print(f"computer choice: {game[computer_choice]}")
    print("you won")
elif user_choice == 2 and computer_choice == 1:
    print(f"computer choice: {game[computer_choice]}")
    print("you won")
else:
    print(f"computer choice: {game[computer_choice]}")
    print("computer won")



# Output:
Sample - 1
enter your choice: 0 for rock, 1 for paper, 2 for scissor: 0

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

computer choice: 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

computer won


Sample -2:
enter your choice: 0 for rock, 1 for paper, 2 for scissor: 2

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

computer choice: 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

you won
