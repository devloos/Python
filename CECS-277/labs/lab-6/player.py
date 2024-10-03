from die import Die


class Player:
    """
    A Player class that represents a player in a dice game. The player rolls three dice 
    and earns points based on specific patterns such as pairs, three-of-a-kinds, or series.

    Attributes:
    -----------
    _dice : list
        A list containing three Die objects, each representing a die that can be rolled.
    _points : int
        The total points accumulated by the player based on the patterns rolled.

    Methods:
    --------
    __init__():
        Initializes the player with three dice and 0 points.

    get_points():
        Returns the current number of points accumulated by the player.

    roll_dice():
        Rolls all dice and sorts them in ascending order.

    has_pair():
        Checks if the player rolled a pair of matching dice. 
        Awards 1 point if true and returns True; otherwise, returns False.

    has_three_of_a_kind():
        Checks if the player rolled three matching dice (three-of-a-kind).
        Awards 3 points if true and returns True; otherwise, returns False.

    has_series():
        Checks if the player rolled a series (three consecutive numbers).
        Awards 2 points if true and returns True; otherwise, returns False.
    """

    def __init__(self):
        self._dice = [Die(), Die(), Die()]
        self._points = 0

    def get_points(self):
        return self._points

    def roll_dice(self):
        for die in self._dice:
            die.roll()

        self._dice.sort()

    def has_pair(self):
        if (self._dice[0] == self._dice[1] or self._dice[1] == self._dice[2] or self._dice[0] == self._dice[2]):
            self._points += 1
            return True

        return False

    def has_three_of_a_kind(self):
        if (self._dice[0] == self._dice[1] == self._dice[2]):
            self._points += 3
            return True

        return False

    def has_series(self):
        if (self._dice[1] - self._dice[0] == 1) and (self._dice[2] - self._dice[1] == 1):
            self._points += 2
            return True

        return False

    def __str__(self):
        d1 = f'D1={self._dice[0]}'
        d2 = f'D2={self._dice[1]}'
        d3 = f'D3={self._dice[2]}'

        return f'{d1}, {d2}, {d3}'
