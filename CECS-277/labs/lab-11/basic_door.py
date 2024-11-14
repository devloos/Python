from door import Door
from random import randint

MAPPED_OPTION = ['pushed', 'pulled']


class BasicDoor(Door):
    def __init__(self):
        self._solution = randint(1, 2)
        self._input = 0

    def examine_door(self) -> str:
        return 'A basic door. You can either push or pull it to open.'

    def menu_options(self) -> str:
        return '1. Push\n2. Pull\nEnter choice: '

    def get_menu_max(self) -> int:
        return 2

    def attempt(self, option):
        self._input = option

        print(f'You {MAPPED_OPTION[option - 1]} the door.')

    def is_unlocked(self) -> bool:
        return self._input == self._solution

    def clue(self):
        return 'Try the other way.'

    def success(self):
        return 'Congratulations, you opened the door.'
