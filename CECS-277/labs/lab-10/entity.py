from abc import abstractmethod
from typing import Self


class Entity:
    def __init__(self, name: str, max_hp: int):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    def take_damage(self, dmg):
        self._hp -= dmg

        if self._hp < 0:
            self._hp = 0

    def heal(self):
        self._hp = self._max_hp

    @abstractmethod
    def attack(self, entity: Self):
        pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def hp(self) -> int:
        return self._hp

    def __str__(self):
        return f'{self.name}\nHP: {self.hp}/{self._max_hp}'
