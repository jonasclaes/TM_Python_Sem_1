import random

guess = int(input('Enter a positive number: '))
correct = random.randint(0, 1000)
guesses = 0

while guess != correct:
    guesses += 1
    if guess < correct:
        print("Higher!")
    elif guess > correct:
        print("Lower!")
    guess = int(input('Enter a positive number: '))
print("You have guessed the number", correct, "in", guesses, "turns.")
