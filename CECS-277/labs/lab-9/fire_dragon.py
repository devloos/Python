from dragon import Dragon
from entity import Entity
from fire import Fire
from random import randint


class FireDragon(Dragon, Fire):
    def __init__(self, name, max_hp, num_sp):
        super().__init__(name, max_hp, num_sp)

    def special_attack(self, opp: Entity) -> str:
        if bool(randint(0, 1)):
            return self.fireball(opp)

        return self.fireblast(opp)
