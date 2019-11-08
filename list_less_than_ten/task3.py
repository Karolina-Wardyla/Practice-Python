# Take a random list, ask the user for a number and return a list that contains only elements from the original list that are smaller than the number given by the user.

random_list = [1, 2, 4, 7, 8, 9, 15, 24, 31]
filtered_numbers = []

chosen_number = int(input("Please enter a number: "))
for x in random_list:
    if x < chosen_number:
        filtered_numbers.append(x)

print(filtered_numbers)
