from random import randint
from typing import Self


class Die:
    """
    A Die class that represents a single die with customizable sides. The die can be rolled 
    to produce a random value, and it supports comparison operators for game logic.

    Attributes:
    -----------
    _sides : int
        The number of sides on the die (default is 6).
    _value : int
        The current value of the die after being rolled (default is 0).

    Methods:
    --------
    __init__(sides=6):
        Initializes the die with the specified number of sides (default is 6).

    roll():
        Rolls the die and sets its value to a random integer between 1 and the number of sides.
        Returns the value rolled.

    __str__():
        Returns a string representation of the die's current value.

    __lt__(other: Self):
        Compares if the value of this die is less than the value of another die.

    __eq__(other: Self):
        Checks if the value of this die is equal to the value of another die.

    __sub__(other: Self):
        Returns the difference between the values of this die and another die.
    """

    def __init__(self, sides=6):
        self._sides = sides
        self._value = 0

    def roll(self):
        self._value = randint(1, self._sides)

        return self._value

    def __str__(self):
        return str(self._value)

    def __lt__(self, other: Self):
        return self._value < other._value

    def __eq__(self, other: Self):
        return self._value == other._value

    def __sub__(self, other: Self):
        return self._value - other._value
