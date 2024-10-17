from vehicle import Vehicle
from random import randint


class Truck(Vehicle):
    """
    Represents a Truck in the Rad Racer game, inheriting from the Vehicle class.

    The Truck is a heavy vehicle named 'Behemoth Truck' with a speed range between 4 and 8 units per turn.
    It has a special move called "Ram" that doubles its speed and allows it to smash through obstacles 
    without stopping.

    Methods:
        description_string() -> str:
            Returns a description of the truck, including its speed range and special move.

        special_move(dist_to_obstacle: int) -> str:
            Performs the truck's special move, "Ram", which moves the truck forward by 2x its normal speed.
            If the truck does not have enough energy, it cannot perform the move. If the move reaches or 
            exceeds the distance to the next obstacle, the truck smashes through the obstacle.
    """

    def __init__(self):
        super().__init__('Behemoth Truck', 'T', 4, 8)

    def description_string(self) -> str:
        return "Behemoth Truck - a heavy truck (4-8 units). Special: Ram (2x speed and it smashes through obstacles)."

    def special_move(self, dist_to_obstacle) -> str:
        if self._energy < 15:
            return f'{self._name} does not have enough energy for a special move.'

        spaces_to_move = int(randint(self._min_speed, self._max_speed) * 2)

        self._energy -= 15

        self._position += spaces_to_move

        if spaces_to_move >= dist_to_obstacle:
            return f'{self._name} rams forward bashing through the Obstacle to go {spaces_to_move} units!'

        return f'{self._name} rams forward {spaces_to_move} units!'
