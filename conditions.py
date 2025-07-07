computer = "rock"
user = input("Do you choose rock, paper or scissors ?\n")

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
 