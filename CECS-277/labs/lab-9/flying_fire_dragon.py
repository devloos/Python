from dragon import Dragon
from entity import Entity
from flying import Flying
from fire import Fire
from random import choice

SWOOP = 0
WINDBLAST = 1
FIREBALL = 2
FIREBLAST = 3


class FlyingFireDragon(Dragon, Flying, Fire):
    def __init__(self, name, max_hp, num_sp):
        super().__init__(name, max_hp, num_sp)

    def special_attack(self, opp: Entity):
        option = choice([
            SWOOP,
            WINDBLAST,
            FIREBALL,
            FIREBLAST
        ])

        if option == SWOOP:
            return self.swoop(opp)
        elif option == WINDBLAST:
            return self.windblast(opp)
        elif option == FIREBALL:
            return self.fireball(opp)
        elif option == FIREBLAST:
            return self.fireblast(opp)
