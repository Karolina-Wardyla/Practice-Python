# Take a random list and write a program that prints out all the elements of the list that are less than 5.

random_list = [1, 2, 4, 8, 9, 15, 18, 24, 31]
filtered_numbers = []

for x in random_list:
    if x < 5:
        filtered_numbers.append(x)
print(filtered_numbers)
