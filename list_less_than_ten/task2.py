# Take a random list and write a program that takes all the elements less than 5 from this list and print them out as a new list.
# Write this in one line of Python.

random_list = [1, 3, 4, 7, 9, 15, 24, 31, 49]
filtered_numbers = [x for x in random_list if x < 5]
print(filtered_numbers)

