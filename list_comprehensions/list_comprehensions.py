# We have a list saved in a variable: initial_list.
# Write one line of Python that takes this list and makes a new list that has only the even elements of this list in it.

initial_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new_list = [num for num in initial_list if num % 2 == 0]
print(new_list)
