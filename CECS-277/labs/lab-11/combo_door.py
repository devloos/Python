from door import Door
from random import randint


class ComboDoor(Door):
    def __init__(self):
        self._solution = randint(1, 10)
        self._input = 0

    def examine_door(self) -> str:
        return 'A door with a combination lock. You can spin the dial to a number 1-10.'

    def menu_options(self) -> str:
        return 'Enter # 1-10: '

    def get_menu_max(self) -> int:
        return 10

    def attempt(self, option: int):
        self._input = option

        print(f'You turn the dial to... {option}')

    def is_unlocked(self) -> bool:
        return self._input == self._solution

    def clue(self):
        if self._input > self._solution:
            return 'Too High.'
        else:
            return 'Too Low.'

    def success(self):
        return 'You found the correct value and opened the door.'
