# Write a program that:
# 1) randomly generate two lists
# 2) returns a new list that contains only the elements that are common between the given lists (without duplicates).
# Make sure your program works on two lists of different sizes.

import random

list1 = random.sample(range(50), 20)
list2 = random.sample(range(100), 30)
new_list = []

for num in list1:
    if num in list2:
        new_list.append(num)

new_list = list(set(new_list))
print(new_list)
