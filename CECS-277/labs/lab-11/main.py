'''
Written by: Israel Fausto, Carlos Aguilera
Date: 11/13/24

Description:
    Escape room game to practice factory method pattern and inheritance.
    The user randomly gets assigned 3 doors where each door has a set of rules so that...
    that door could be unlocked. The user then is allowed to choose the difficulty of the
    doors and will be assigned doors based on that difficulty.
'''
from check_input import get_int_range
from door_factory import DoorFactory
from easy_door_factory import EasyDoorFactory
from difficult_door_factory import DifficultDoorFactory
from door import Door


def open_door(door: Door):
    print(door.examine_door())

    while True:
        option = get_int_range(door.menu_options(), 1, door.get_menu_max())

        door.attempt(option)

        if door.is_unlocked():
            print(door.success())
            break

        print(door.clue())


def main():
    print('Welcome to the Escape Room.')
    print('You must unlock 3 doors to escape...')

    difficulty = get_int_range('Enter Difficulty (1. Easy 2. Hard): ', 1, 2)

    door_factory: DoorFactory = EasyDoorFactory() if difficulty == 1 else DifficultDoorFactory()

    for _ in range(3):
        open_door(door_factory.create_door())

    print('Congratulations! You escaped...this time.')


main()
