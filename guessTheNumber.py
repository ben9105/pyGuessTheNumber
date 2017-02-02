import math
import random
import sys

#Get number from user
guess = input("Please guess a number between one and ten.")
#gets a random number between 1 and 10
number = random.randint(1, 10)

#finally works, if/else statement to declare a winner.
if number > guess:
    print "You were a little low.", number
elif number < guess:
    print "You were too high.", number
elif number == guess:
    print "You got it right!"
