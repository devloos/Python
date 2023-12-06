from egcd import extended_gcd

KEY_ALPHA = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,  'h': 8, 'i': 9,  'j': 10, 'k': 11,  'l': 12, 'm': 13,
             'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,  'w': 23, 'x': 24, 'y': 25,  'z': 26, ' ': 27}
KEY_DIGIT = dict(map(reversed, KEY_ALPHA.items()))
ENCODED_COUNT = 27


def digits_to_string(digits: [int]) -> str:
    message = ''
    for digit in digits:
        message += KEY_DIGIT[digit]

    return message


def encrypt(message: str, a: int, b: int) -> str:
    encrypted_message = ''
    digits = []
    for c in message:
        i = KEY_ALPHA[c.lower()]

        mod = (a * i + b) % ENCODED_COUNT

        if (mod == 0):
            mod = ENCODED_COUNT

        digits.append(mod)

    encrypted_message += digits_to_string(digits)

    return encrypted_message


def mod_inverse(a, m) -> int:
    _, coefs = extended_gcd(a, m)

    return coefs[0] % m


def decrypt(message: str, a, b) -> str:
    a_inverse = mod_inverse(a, ENCODED_COUNT)
    decrypted_message = ''
    digits = []
    for c in message:
        i = KEY_ALPHA[c.lower()]

        res = (a_inverse * (i - b)) % ENCODED_COUNT

        if (res == 0):
            res = ENCODED_COUNT

        digits.append(res)

    decrypted_message += digits_to_string(digits)

    return decrypted_message


def main():
    message = 'The quick brown fox'
    encrypted_message = encrypt(message, 5, 3)
    print(encrypted_message)

    decrypted_message = decrypt(encrypted_message, 5, 3)
    print(decrypted_message)


main()
