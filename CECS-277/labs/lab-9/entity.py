from abc import abstractmethod
from typing import Self


class Entity:
    """
    A base class representing a generic entity with health points (HP) and basic information.

    Attributes:
        _name (str): The name of the entity.
        _max_hp (int): The maximum health points for the entity.
        _hp (int): The current health points of the entity.

    Methods:
        take_damage(dmg: int): Reduces the entity's current HP by the given damage value, 
            ensuring it doesn't drop below zero.
        name() -> str: Returns the name of the entity.
        hp() -> int: Returns the current HP of the entity.
        basic_attack(opp: Self) -> str: Abstract method for a basic attack against an opponent.
            Must be implemented in subclasses.
        special_attack(opp: Self) -> str: Abstract method for a special attack against an opponent.
            Must be implemented in subclasses.
        __str__() -> str: Returns a string representation of the entity's name and HP in 
            the format "name: current_hp/max_hp".
    """

    def __init__(self, name: str, max_hp: int):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    def take_damage(self, dmg: int):
        self._hp -= dmg

        if self._hp < 0:
            self._hp = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    @abstractmethod
    def basic_attack(self, opp: Self) -> str:
        pass

    @abstractmethod
    def special_attack(self, opp: Self) -> str:
        pass

    def __str__(self) -> str:
        return f'{self._name}: {self._hp}/{self._max_hp}'
