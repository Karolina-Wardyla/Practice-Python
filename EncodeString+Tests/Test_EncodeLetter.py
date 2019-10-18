import unittest
from EncodeString import encode_letter


class TestEncodeLetter(unittest.TestCase):
    # Tests for encode_letter function from EncodeString.py

    def test_lowercase_letter(self):
        letter = 'a'
        result = encode_letter(letter)
        self.assertEqual(result, 'z')

    def test_other_lowercase_letter(self):
        letter = 'd'
        result = encode_letter(letter)
        self.assertEqual(result, 'w')


if __name__ == '__main__':
    unittest.main()