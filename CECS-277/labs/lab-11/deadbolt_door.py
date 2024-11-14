from door import Door
from random import choice

LOCKED = False
UNLOCKED = True


class DeadboltDoor(Door):
    def __init__(self):
        self._bolt1 = choice([LOCKED, UNLOCKED])
        self._bolt2 = choice([LOCKED, UNLOCKED])

    def examine_door(self) -> str:
        return "A double deadbolt door. Both need to be unlocked to open the door, but you can't tell by looking at them if they're locked or unlocked."

    def menu_options(self) -> str:
        return '1. Toggle bolt 1\n2. Toggle bolt 2\nEnter choice: '

    def get_menu_max(self) -> int:
        return 2

    def attempt(self, option):
        if option == 1:
            self._bolt1 = not self._bolt1
            print('You toggle the first bolt.')
        else:
            self._bolt2 = not self._bolt2
            print('You toggle the second bolt.')

    def is_unlocked(self) -> bool:
        return self._bolt1 and self._bolt2

    def clue(self):
        if self._bolt1 or self._bolt2:
            return 'You jiggle the door...it seems like one of the bolts is unlocked.'

        return "You jiggle the door... it seems like it's completely locked."

    def success(self):
        return 'You unlocked both deadbolts and opened the door.'
