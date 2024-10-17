from abc import ABC, abstractmethod
from random import randint


class Vehicle(ABC):
    """
    Represents an abstract base class for different types of vehicles in the Rad Racer game.

    The Vehicle class defines common attributes such as name, initial, speed range, position, and energy. 
    It also includes methods for performing fast and slow movements, with the actual behavior of the vehicle's 
    special move and description string being implemented in derived classes.

    Attributes:
        _name (str): The name of the vehicle.
        _initial (str): The symbol representing the vehicle on the track.
        _min_speed (int): The minimum speed the vehicle can move per turn.
        _max_speed (int): The maximum speed the vehicle can move per turn.
        _position (int): The current position of the vehicle on the track.
        _energy (int): The vehicle's energy, which is consumed for performing fast moves and special moves.

    Methods:
        fast(dist_to_obstacle: int) -> str:
            Moves the vehicle forward by a random number of units within its speed range. 
            Consumes energy and may crash into an obstacle if it moves too fast.

        slow(dist_to_obstacle: int) -> str:
            Moves the vehicle slowly (half of its normal speed), with a higher chance of avoiding obstacles.

        description_string() -> str:
            Abstract method that returns a description of the vehicle. Must be implemented by subclasses.

        special_move(dist_to_obstacle: int) -> str:
            Abstract method that performs the vehicle's special move. Must be implemented by subclasses.
    """

    def __init__(self, name: str, initial: str, min_speed: int, max_speed: int):
        self._name = name
        self._initial = initial
        self._min_speed = min_speed
        self._max_speed = max_speed
        self._position = 0
        self._energy = 100

    def __str__(self) -> str:
        return f'{self._name} [Position - {self._position}, Energy - {self._energy}]'

    @property
    def initial(self):
        return self._initial

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos

    @property
    def energy(self):
        return self._energy

    def fast(self, dist_to_obstacle: int) -> str:
        if self._energy < 5:
            return f'{self._name} does not have enough energy for a fast move.'

        spaces_to_move = randint(self._min_speed, self._max_speed)
        self._energy -= 5

        if spaces_to_move >= dist_to_obstacle:
            self._position += dist_to_obstacle - 1
            return f'{self._name} CRASHES into an obstacle!'

        self._position += spaces_to_move
        return f'{self._name} quickly moves {spaces_to_move} units!'

    def slow(self, dist_to_obstacle) -> str:
        spaces_to_move = int(randint(self._min_speed, self._max_speed) * 0.5)
        self._position += spaces_to_move

        if spaces_to_move >= dist_to_obstacle:
            return f'{self._name} slowly and safely moves around the obstacle {spaces_to_move} units!'

        return f'{self._name} slowly moves {spaces_to_move} units!'

    @abstractmethod
    def description_string(self) -> str:
        pass

    @abstractmethod
    def special_move(self, dist_to_obstacle: int) -> str:
        pass
