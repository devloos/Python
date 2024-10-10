from cipher import Cipher


class Caesar(Cipher):
    """
    A class used to represent the Caesar Cipher, a type of substitution cipher where each letter 
    in the plaintext is shifted by a certain number of positions in the alphabet.

    This class inherits from the Cipher class, which provides basic functionality for the Atbash cipher.

    Attributes
    ----------
    _shift : int
        The number of positions each letter is shifted in the alphabet.

    Methods
    -------
    _encrypt_letter(letter):
        Shifts the letter forward by the shift amount in the alphabet to encrypt it.

    _decrypt_letter(letter):
        Shifts the letter backward by the shift amount in the alphabet to decrypt it.
    """

    def __init__(self, shift):
        super().__init__()
        self._shift = shift

    def _encrypt_letter(self, letter):
        if letter not in self._alphabet:
            return letter
        index = self._alphabet.index(letter)
        new_index = (index + self._shift) % len(self._alphabet)
        return self._alphabet[new_index]

    def _decrypt_letter(self, letter):
        if letter not in self._alphabet:
            return letter
        index = self._alphabet.index(letter)
        new_index = (index - self._shift) % len(self._alphabet)
        return self._alphabet[new_index]
