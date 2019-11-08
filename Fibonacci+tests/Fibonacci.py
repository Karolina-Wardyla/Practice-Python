# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.


def fibonacci_sequence(elements):
    if elements >= 1:
        a = 0
        b = 1
        fib_numbers = []
        for i in range(elements):
            fib_numbers.append(a)
            a, b = b, a + b
        return fib_numbers
    else:
        return []


if __name__ == '__main__':
    number_of_numbers = input("Enter a number of numbers in the sequence: ")
    users_sequence = fibonacci_sequence(int(number_of_numbers))
    print(users_sequence)

