from abc import abstractmethod
from door import Door


class DoorFactory:
    """
    Abstract base class for a factory that creates `Door` objects.

    This factory class defines a method for creating doors, allowing for the 
    instantiation of different types of `Door` subclasses through a unified interface. 
    Subclasses of `DoorFactory` should implement the `create_door` method to provide 
    a specific type of door that can be used in a game or application setting.

    Methods
    -------
    create_door() -> Door
        Creates and returns an instance of a `Door` subclass.
    """

    @abstractmethod
    def create_door(self) -> Door:
        pass
