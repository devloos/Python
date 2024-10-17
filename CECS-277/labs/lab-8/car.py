from vehicle import Vehicle
from random import randint


class Car(Vehicle):
    """
    Represents a Car in the Rad Racer game, inheriting from the Vehicle class.

    The Car is characterized by a name 'Lightning Car', an initial, and a speed range
    between 6 and 8 units per turn. It also has a special move called "Nitro Boost" 
    that allows it to move 1.5 times its normal speed when used, at the cost of energy.

    Methods:
        description_string() -> str:
            Returns a description of the car including its speed range and special move.

        special_move(dist_to_obstacle) -> str:
            Performs the car's special move, "Nitro Boost", which moves the car forward 
            by 1.5 times its normal speed. If the car does not have enough energy, it 
            cannot perform the move. If the move reaches or exceeds the distance to 
            the next obstacle, the car crashes into the obstacle.
    """

    def __init__(self):
        super().__init__('Lightning Car', 'C', 6, 8)

    def description_string(self) -> str:
        return 'Lightning Car - a fast car (6-8 units). Special: Nitro Boost (1.5x speed)'

    def special_move(self, dist_to_obstacle) -> str:
        if self._energy < 15:
            return f'{self._name} does not have enough energy for a special move.'

        spaces_to_move = int(randint(self._min_speed, self._max_speed) * 1.5)
        self._energy -= 15

        if spaces_to_move >= dist_to_obstacle:
            self._position += dist_to_obstacle - 1
            return f'{self._name} CRASHES into an obstacle!'

        self._position += spaces_to_move
        return f'{self._name} uses nitro boost and moves {spaces_to_move} units!'
