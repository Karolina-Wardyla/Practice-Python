# Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.


def list_ends(elements):
    return [elements[0], elements[-1]]


result = list_ends([19, 11, 2, 3, 5, 10, 20, 33, 28, 44])
print(result)