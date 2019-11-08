# Ask the user for a number and determine whether the number is prime or not.
# Take this opportunity to practice using functions.


def is_prime(number_to_check):
    possible_divisors = range(1, number_to_check // 2 + 1)
    divisors = []

    for num in possible_divisors:
        if number_to_check % num == 0:
            divisors.append(num)

    divisors.append(number_to_check)
    if len(divisors) == 2:
        return True
    else:
        return False


result = is_prime(int(input("Enter a number: ")))
print(result)














#
# def check_primality():
#     return int(input("Give me a number: "))
#
#
# user_number = check_primality()
# possible_divisors = range(2, user_number + 1)
# divisors = []
#
# for number in possible_divisors:
#     if user_number % number == 0:
#         divisors.append(number)
#
# divisors.append(user_number)
# if len(divisors) == 2:
#     print("Your number is a prime.")
# else:
#     print("Your number is not a prime.")
#







