# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Your name: ")
age = int(input("Your age: "))
year = str((2019 - age) + 100)
print(name + ", your 100th birthday will be in " + str(year) + ".")
