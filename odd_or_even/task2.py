# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("Enter a number: "))
check = int(input("Enter another number: "))

if num % check == 0:
    print(str(num) + " divides evenly by " + str(check) + ".")
else:
    print(str(num) + " does not divide evenly by " + str(check) + ".")