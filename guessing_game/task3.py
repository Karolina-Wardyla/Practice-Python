# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

num = random.randint(1, 9)
tries = 0

while True:
    guess = input("Please enter a number from 1 to 9 or 'exit': ")
    if guess != "exit":
        guess = int(guess)
        if guess < num:
            print("Too low.")
        elif guess > num:
            print("Too high.")
        else:
            print("Exactly right.")
            num = random.randint(1, 9)
            tries += 1
    else:
        print("You played " + str(tries) + " games.")
        break
