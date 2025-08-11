import random

dice = random.randint(1,6)

guess = int(input("Guess the dice roll\n"))

print("The computer rolled a " + str(dice))

if dice == guess:
    print("You guessed correctly")
else:
    print("Incorrect guess, try again")