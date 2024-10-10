'''
Written by: Israel Fausto, Carlos Aguilera
Date: 10/09/24

Description:
    This program offers a simple command-line interface for encoding and decoding
    messages using two classical encryption methods. It supports both Atbash and
    Caesar ciphers, allowing users to save encrypted messages to a file and later
    retrieve and decrypt them. Ideal for educational purposes or for adding a fun
    layer of secrecy to messages.
'''
from cipher import Cipher
from caesar import Caesar


def main_menu():
    first_choice = input('''Secret Decoder Ring:
1. Encrypt
2. Decrypt\n''')

    if first_choice == '1':
        encrypting()

    elif first_choice == '2':
        decrypting()

    else:
        print('Invalid choice.')
        return


def encrypting():
    encrypt_choice = input('''Enter encryption type:
1. Atbash
2. Caesar\n''')
    message = input('Enter message: ')
    if encrypt_choice == '1':
        cipher = Cipher()
    elif encrypt_choice == '2':
        shift = input('Enter shift value: ')
        cipher = Caesar(int(shift))
    else:
        print('Invalid choice.')
        return

    encrypted_message = cipher.encrypt_message(message)
    with open('message.txt', 'w') as file:
        file.write(encrypted_message)
    print('Encrypted message saved to "message.txt".')


def decrypting():
    decrypt_choice = input('''Enter decryption type:
1. Atbash
2. Caesar\n''')

    if decrypt_choice == '1':
        cipher = Cipher()

    elif decrypt_choice == '2':
        while True:
            try:
                shift = int(input('Enter shift value: '))
                if 0 <= shift <= 25:
                    cipher = Caesar(shift)
                    break
                else:
                    print('Invalid input.')
                    return
            except ValueError:
                print('Invalid input')
    else:
        print('Invalid choice.')
        return

    with open('message.txt', 'r') as file:
        encrypted_message = file.read()
        decrypted_message = cipher.decrypt_message(encrypted_message)

    print('Reading encrypted message from "message.txt".')
    print('Decrypted message: ' + decrypted_message)


main_menu()
