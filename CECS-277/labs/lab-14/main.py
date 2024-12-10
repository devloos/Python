'''
Written by: Israel Fausto, Carlos Aguilera
Date: 12/09/24

Description:
    This lab uses the State pattern. Puppy simulator program that has two basic functions: to feed or
    play with the puppy. The puppy will react differently to these functions based on which state it
    is currently in. The puppy has three possible states: asleep, eating, or playing.
'''
from check_input import get_int_range
from puppy import Puppy


def main_menu() -> int:
    print('What would you like to do?')
    print('1. Feed the puppy')
    print('2. Play with the puppy')
    print('3. Quit')

    return get_int_range('Enter choice: ', 1, 3)


def main():
    print('Congratulations on your new puppy!')
    puppy = Puppy()

    while True:
        choice = main_menu()

        match choice:
            case 1:
                print(puppy.give_food())

            case 2:
                print(puppy.throw_ball())

            case 3:
                exit()


main()
