# Create a function encode_string(string) which takes a parameter made of lowercase latin alphabet letters and digits.
# Function calling encodes the given string (parameter) using these rules:
#     - letter 'a' is replaced by letter 'z', letter 'b' by letter 'y', letter 'c' by letter 'x';
#     - the function encodes only letters and digits stays the same;
#     - a few examples:
#       1) encode_string("abrakadabra") --> "zyizpzwzyiz"
#       2) encode_string("ab321z") --> "zy321a".


def encode_letter(letter):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    index = alphabet.index(letter)
    index = -(index + 1)
    encodedLetter = alphabet[index]
    return encodedLetter


def encode_string(string):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = ''

    for letter in string:
        if letter in digits:
            result = result + letter
        else:
            encodedLetter = encode_letter(letter)
            result = result + encodedLetter
    return result

# final_result = encode_string('aaaaaa')
# print(final_result)

