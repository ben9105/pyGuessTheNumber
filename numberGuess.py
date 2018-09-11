import random

print("Hello, what is your name?")

name = input()

print("Well then " + name + " let's get this started.  Guess a number.")

secretNumber = random.randint(1, 20)

for guessAmount in range(1, 7):
    print("Let's guess: ")
    guess = int(input())

    if guess > secretNumber:
        print("Your guess is too high.")
    elif guess < secretNumber:
        print("Your guess is too low.")
    else:
        break

if guess == secretNumber:
    print("Good job " + name + " you guessed in " + str(guessAmount) + " tries.")
else:
    print("You took too long, the number was " + str(secretNumber) + ".")
