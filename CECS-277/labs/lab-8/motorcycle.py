from vehicle import Vehicle
from random import randint, random


class Motorcycle(Vehicle):
    """
    Represents a Motorcycle in the Rad Racer game, inheriting from the Vehicle class.

    The Motorcycle is a fast and agile vehicle named 'Swift Bike' with a speed range between 6 and 8 units per turn.
    It has a special move called "Wheelie," which doubles its speed, but comes with a 25% chance of crashing.

    Methods:
        description_string() -> str:
            Returns a description of the motorcycle, including its speed range and special move.

        special_move(dist_to_obstacle: int) -> str:
            Performs the motorcycle's special move, "Wheelie," which moves the bike forward by 2x its normal speed.
            There is a 25% chance that the motorcycle will crash while attempting the wheelie.
            If the motorcycle does not have enough energy, it cannot perform the move.

        slow(dist_to_obstacle: int) -> str:
            Moves the motorcycle forward at 75% of its normal speed, with a higher chance of avoiding obstacles.
    """

    def __init__(self):
        super().__init__('Swift Bike', 'M', 6, 8)

    def description_string(self) -> str:
        return "Swift Bike - a speedy motorcycle (6-8 units). Special: Wheelie (2x speed but there's a chance you'll crash)."

    def special_move(self, dist_to_obstacle) -> str:
        if self._energy < 15:
            return f'{self._name} does not have enough energy for a special move.'

        # failed the probability
        if random() > 0.75:
            return f'{self._name} pops a wheelie and falls over!'

        spaces_to_move = int(randint(self._min_speed, self._max_speed) * 2)

        self._energy -= 15

        if spaces_to_move >= dist_to_obstacle:
            self._position += dist_to_obstacle - 1
            return f'{self._name} pops a wheelie crashes into an obstacle!'

        self._position += spaces_to_move
        return f'{self._name} pops a wheelie and moves {spaces_to_move} units!'

    def slow(self, dist_to_obstacle):
        spaces_to_move = int(randint(self._min_speed, self._max_speed) * 0.75)
        self._position += spaces_to_move

        if spaces_to_move >= dist_to_obstacle:
            return f'{self._name} slowly and safely moves around the obstacle {spaces_to_move} units!'

        return f'{self._name} slowly moves {spaces_to_move} units!'
