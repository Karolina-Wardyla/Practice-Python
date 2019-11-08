# Take two random lists and write a program that returns a new list that contains only the elements that are common between the given lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# Write this in one line of Python.

list1 = [10, 71, 22, 3, 5, 8, 13, 21, 55, 89, 19, 34, 14, 28, 33, 50]
list2 = [1, 2, 34, 3, 42, 5, 6, 71, 8, 9, 50, 14, 13, 10, 11, 12, 13, 19, 5]

new_list = [num for num in list1 if num in list2]
print(new_list)
