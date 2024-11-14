from door import Door
from random import choice

OPTIONS = ['X', 'O']


class CodeDoor(Door):
    def __init__(self):
        self._solution: list[str] = [choice(OPTIONS), choice(OPTIONS), choice(OPTIONS)]
        self._input: list[str] = ['O', 'O', 'O']

    def examine_door(self) -> str:
        return "A door with a coded keypad with three characters. Each key toggles a value with an 'X' or an 'O'."

    def menu_options(self) -> str:
        return '1. Press Key 1\n2. Press Key 2\n3. Press Key 3\nEnter choice: '

    def get_menu_max(self) -> int:
        return 3

    def attempt(self, option: int):
        index = option - 1

        current_char = self._input[index]

        if current_char == 'O':
            self._input[index] = 'X'
        else:
            self._input[index] = 'O'

    def is_unlocked(self) -> bool:
        return self._input == self._solution

    def clue(self) -> str:
        correct_chars = 0

        for i in range(3):
            if self._input[i] == self._solution[i]:
                correct_chars += 1

        return f'Number of correct characters: {correct_chars}'

    def success(self):
        return 'You entered the correct code and opened the door.'
