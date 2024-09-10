'''
Written by: Israel Fausto, Carlos Aguilera
Date: 09/09/24

Description:
    Hang man clone where the user has to guess a word by guessing letters.
    If the user guesses a letter that is not in the word, they lose a life.
    Six lives are given to the user. If the user runs out of lives, they lose.
    If the user guesses the word before they run out of lives, they win.
'''
from dictionary import words
from check_input import get_yes_no
import random

A_IN_ASCII = 65
Z_IN_ASCII = 90

LETTERS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

GALLOW_STATES = [
    '''
||
||
||
||
    ''',
    '''
||    o
||
||
||
    ''',
    '''
||    o
||    |
||
||
    ''',
    '''
||    o
||    |
||   /
||
    ''',
    '''
||    o
||    |
||   / \\
||
    ''',
    '''
||   \\o
||    |
||   / \\
||
    ''',
    '''
||   \\o/
||    |
||   / \\
||
    ''',
]


def display_gallows(number_incorrect: int):
    '''Depending on the number of incorrect letters
    we choose the state based on it.
    '''
    print('========')
    print('||/   |', end='')
    print(GALLOW_STATES[number_incorrect])


def display_letters(word: str, correct: list[str]):
    '''We create a copy of the correct letters because
    our algorithm needs to mutate the correct list.
    This is because we go through the desired word and
    as we find the letter from the correct list we remove it.
    This is so that we do not process duplicates.
    '''
    letters = []
    correct_copy = correct.copy()

    for letter in word:
        if letter in correct_copy:
            letters.append(letter)
            correct_copy.remove(letter)
        else:
            letters.append('_')

    print(' '.join(letters), end='\n\n')


def get_letters_remaining(incorrect, correct):
    '''From a constant list of letters we remove the ones
    included in incorrect and correct list. We then display the list.
    '''
    letters_left = [
        letter for letter in LETTERS if letter not in incorrect and letter not in correct
    ]

    print('Letters remaining: ', end='')

    for letter in letters_left:
        print(letter, end=' ')

    print()


def main():
    game_running = True

    while game_running:
        incorrect = []
        correct = []
        random_word = random.choice(words)

        while True:
            # display incorrect selections
            print('Incorrect selections:', end=' ')

            for letter in incorrect:
                print(letter, end=' ')

            print()

            # display main ui
            display_gallows(len(incorrect))
            display_letters(random_word, correct)
            get_letters_remaining(incorrect, correct)

            # check if user won or lost
            if len(correct) == len(random_word):
                print('You win!')
                game_running = get_yes_no('Play again (Y/N)? ')
                break

            if len(incorrect) == 6:
                print('You lost!')
                print('The word was:', random_word)
                game_running = get_yes_no('Play again (Y/N)? ')
                break

            letter = input('Enter a letter: ').upper()

            # checking if empty or not in range of A - Z
            if letter == '' or ord(letter) < A_IN_ASCII or ord(letter) > Z_IN_ASCII:
                print('That is not a letter.', end='\n\n')
                continue

            # if letter is in incorrect or if letter is in correct but we account for repeated letters
            if letter in incorrect or (correct.count(letter) >= random_word.count(letter) and letter in random_word):
                print('You have already used that letter.', end='\n\n')
                continue

            # if in desired word than correct otherwise incorrect
            if letter in random_word:
                correct.append(letter)
                print('Correct!')
            else:
                incorrect.append(letter)
                print('Incorrect!')

            correct.sort()
            incorrect.sort()

            print()


main()
