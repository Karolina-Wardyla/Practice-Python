# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

chosen_word = input("Please enter a word: ")

reversed_chosen_word = chosen_word[::-1]
if chosen_word == reversed_chosen_word:
    print("Your word is a palindrome.")
else:
    print("Your word is not a palindrome.")


