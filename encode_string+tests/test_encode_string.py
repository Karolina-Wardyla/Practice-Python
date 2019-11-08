import unittest
from encode_string import encode_string


class TestEncodeString(unittest.TestCase):
    """Tests for encode_string function from encode_string.py"""

    def test_lowercase_letters_string(self):
        string = 'abcdzwy'
        result = encode_string(string)
        self.assertEqual(result, 'zyxwadb')

    def test_letters_and_digits_string(self):
        string = 'abc123abc'
        result = encode_string(string)
        self.assertEqual(result, 'zyx123zyx')

    def test_only_digits_string(self):
        string = '123456789'
        result = encode_string(string)
        self.assertEqual(result, '123456789')

    def test_empty_string(self):
        string = ''
        result = encode_string(string)
        self.assertEqual(result, '')


if __name__ == '__main__':
    unittest.main()
