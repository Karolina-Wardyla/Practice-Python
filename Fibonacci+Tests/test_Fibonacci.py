import unittest
from Fibonacci import fibonacci_sequence


class TestFibonacciNumbersGenerator(unittest.TestCase):
    """Tests for 'Fibonacci.py'."""

    def test_number_1(self):
        formatted_sequence = fibonacci_sequence(1)
        self.assertEqual(formatted_sequence, [0])

    def test_number_2(self):
        formatted_sequence = fibonacci_sequence(2)
        self.assertEqual(formatted_sequence, [0, 1])

    def test_positive_number_bigger_than_2(self):
        formatted_sequence = fibonacci_sequence(10)
        self.assertEqual(formatted_sequence, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_another_positive_number(self):
        formatted_sequence = fibonacci_sequence(15)
        self.assertEqual(formatted_sequence, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])

    def test_number_zero(self):
        formatted_sequence = fibonacci_sequence(0)
        self.assertEqual(formatted_sequence, [])

    def test_negative_number(self):
        formatted_sequence = fibonacci_sequence(-10)
        self.assertEqual(formatted_sequence, [])


if __name__ == '__main__':
    unittest.main()