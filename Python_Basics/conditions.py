import random

computer = random.choice(["rock", "paper", "scissors"])
user = input("Do you choose rock, paper or scissors ?\n")

print("Computer selected "+ computer)

if computer == user :
    print("tie")
elif user == "paper" and computer == "rock":
    print("you win")
elif user == "scissors" and computer == "paper":
    print("you win")
elif user == "rock" and computer == "scissors":
    print("you win")
else:
    print("You lose")


 
