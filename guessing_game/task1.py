# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# When guessed, ask the user if they want to play again.

import random

num = random.randint(1, 9)

while True:
    guess = int(input("Please enter a number from 1 to 9: "))
    if guess < num:
        print("Too low.")
    elif guess > num:
        print("Too high.")
    else:
        print("Exactly right.")
        num = random.randint(1, 9)
        play_again = input("Do you want to play again? Type: 'y' or 'n': ")
        if play_again == 'n':
            break







