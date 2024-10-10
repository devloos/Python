
class Cipher:
    """
    A class used to represent the Atbash Cipher, a simple substitution cipher where the alphabet is reversed.

    Attributes
    ----------
    _alphabet : list of str
        A list containing uppercase English letters A-Z.

    Methods
    -------
    encrypt_message(message):
        Encrypts a message by reversing the alphabet for each letter.

    decrypt_message(message):
        Decrypts a message by reversing the alphabet for each letter.

    _encrypt_letter(letter):
        Reverses the position of a given letter in the alphabet to encrypt it.

    _decrypt_letter(letter):
        Reverses the position of a given letter in the alphabet to decrypt it.
    """

    def __init__(self):
        self._alphabet = [chr(i) for i in range(65, 91)]

    def encrypt_message(self, message):
        message = message.upper()
        encrypted_message = ""

        for char in message:
            if char in self._alphabet:
                encrypted_message += self._encrypt_letter(char)
            else:
                encrypted_message += char

        return encrypted_message

    def decrypt_message(self, message):
        message = message.upper()
        decrypted_message = ""

        for char in message:
            if char in self._alphabet:
                decrypted_char = self._decrypt_letter(char)
                decrypted_message += decrypted_char
            else:
                decrypted_message += char

        return decrypted_message

    def _encrypt_letter(self, letter):
        index = self._alphabet.index(letter)
        reversed_index = 25 - index

        return self._alphabet[reversed_index]

    def _decrypt_letter(self, letter):
        index = self._alphabet.index(letter)
        reversed_index = 25 - index

        return self._alphabet[reversed_index]
