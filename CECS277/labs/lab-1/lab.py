
""" Guessing Game

Written by: Carlos Aguilera
Date: 08/26/24

Description:
    The program will generate a random number from 1-100. The user will have to guess the
    number generated. It will give the user hints like Too High or Too Low. After it will
    display the number of tries it took.
"""
from random import randint
from check_input import get_int_range


def main():
    print('- Guessing Game -')

    # setup
    target_num = randint(1, 100)
    guess = get_int_range('Make a guess (1-100): ', 1, 100)
    tries = 1

    while guess != target_num:
        # give user hints
        if (guess > target_num):
            print('Too high!', end='  ')
        else:
            print('Too low!', end='  ')

        # get input
        guess = get_int_range('Guess again (1-100): ', 1, 100)

        tries += 1

    print(f'Correct! You got it in {tries} tries.')


main()
