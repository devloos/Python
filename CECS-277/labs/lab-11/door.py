from abc import abstractmethod


class Door:
    """
    Abstract base class representing a door in an adventure or puzzle game.

    This class defines a standard interface for doors that players can interact with, examine,
    attempt to unlock, and receive clues or success messages from. Each subclass of `Door`
    should implement the following methods to provide specific behaviors and responses 
    for different types of doors.

    Methods
    -------
    examine_door() -> str
        Describes the appearance or characteristics of the door to the player.

    menu_options() -> str
        Provides a list of options for interacting with the door.

    get_menu_max() -> int
        Returns the maximum number of options available in the door's menu.

    attempt(option) -> str
        Attempts an interaction with the door based on the given option, and returns the outcome.

    is_unlocked() -> bool
        Checks if the door is unlocked.

    clue() -> str
        Provides a clue to the player to help in unlocking the door.

    success() -> str
        Returns a success message for the player upon successfully unlocking or passing through the door.
    """

    @abstractmethod
    def examine_door(self) -> str:
        pass

    @abstractmethod
    def menu_options(self) -> str:
        pass

    @abstractmethod
    def get_menu_max(self) -> int:
        pass

    @abstractmethod
    def attempt(self, option) -> str:
        pass

    @abstractmethod
    def is_unlocked(self) -> bool:
        pass

    @abstractmethod
    def clue(self) -> str:
        pass

    @abstractmethod
    def success(self) -> str:
        pass
