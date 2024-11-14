from door import Door
from random import randint

MAPPED_AREA = [
    'doormat', 'flower pot', 'fake rock'
]


class LockedDoor(Door):
    def __init__(self):
        self._solution = randint(1, 3)
        self._input = 0

    def examine_door(self) -> str:
        return 'A locked door. Look around, the key is hidden nearby.'

    def menu_options(self) -> str:
        return '1. Look under the doormat.\n2. Look under the flower pot.\n3. Look under the fake rock.\nEnter choice: '

    def get_menu_max(self) -> int:
        return 3

    def attempt(self, option: int):
        self._input = option

        print(f'You look under the {MAPPED_AREA[option - 1]}.')

    def is_unlocked(self) -> bool:
        return self._input == self._solution

    def clue(self):
        return 'Look somewhere else.'

    def success(self):
        return 'You found the key and opened the door.'
