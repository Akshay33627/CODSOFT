"""
WORKFLOW OF PROJECT:
1 - input from user (rock, paper, scissor)
2 - computer choice (computer will choose randomly not conditionally)
3 - result print

cases:
A - rock
rock - rock = tie
rock - paper = paper win
rock - scissor = rock win

B - paper
paper - paper = tie
paper - scissor = scissor win
paper - rock = paper win

C - scissor
scissor - scissor = tie
scissor - paper = scissor win
scissor - rock = rock win

"""

import random
item_list = ["rock", "paper", "scissor"]

user_choice = input("enter your move = rock, paper, scissor=")
computer_choice = random.choice (item_list)

print(f"user choice = {user_choice}, computer choice = {computer_choice}")

if user_choice == computer_choice:
    print("both chooses same: = match tie")

elif user_choice == "rock":
    if computer_choice == "paper":
        print("paper covers rock = computer")
    else:
        print("rock smashes scissor = you win")

elif user_choice == "paper":
    if computer_choice == "scissor":
        print("scissor cuts paper , computer win")
    else:
        print("paper cover rock , you win")

elif user_choice == "scissor":
    if computer_choice == "paper":
        print("scissor cuts paper , you win")
    else:
        print("rock smashes scissor , computer win")