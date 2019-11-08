# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# Divisor is a number that divides evenly into another number.
# (For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

chosen_number = int(input("Please enter a number: "))
possible_divisors = range(1, chosen_number // 2 + 1)
divisors = []

for number in possible_divisors:
    if chosen_number % number == 0:
        divisors.append(number)

divisors.append(chosen_number)
print(divisors)
