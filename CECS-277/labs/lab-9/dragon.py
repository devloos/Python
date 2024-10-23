from entity import Entity
from random import randint


class Dragon(Entity):
    def __init__(self, name: str, max_hp: int, num_sp: int):
        super().__init__(name, max_hp)
        self._special_attacks = num_sp

    def decrement_special_attacks(self):
        if self._special_attacks > 0:
            self._special_attacks -= 1

    def basic_attack(self, opp: Entity) -> str:
        dmg = randint(3, 7)
        opp.take_damage(dmg)

        return f'{self.name} smashes you with its tail for {dmg} damage!'

    @property
    def special_attacks(self) -> int:
        return self._special_attacks

    def __str__(self):
        return super().__str__() + f'\nSpecial attacks remaining: {self._special_attacks}'
