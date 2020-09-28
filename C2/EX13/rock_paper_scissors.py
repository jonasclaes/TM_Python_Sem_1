import random

choice = input("What do you choose? Rock, paper or scissors? ")
print("You chose", choice)
computer_choice = random.choice(["rock", "paper", "scissors"])
print("I chose", computer_choice)

if choice == computer_choice:
    print("It's a tie.")
elif choice == "rock":
    if computer_choice == "paper":
        print("I win!")
    else:
        print("You win!")
elif choice == "paper":
    if computer_choice == "scissors":
        print("I win!")
    else:
        print("You win!")
elif choice == "scissors":
    if computer_choice == "rock":
        print("I win!")
    else:
        print("You win!")
