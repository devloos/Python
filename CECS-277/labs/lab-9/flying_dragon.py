from dragon import Dragon
from entity import Entity
from flying import Flying
from random import randint


class FlyingDragon(Dragon, Flying):
    def __init__(self, name, max_hp, num_sp):
        super().__init__(name, max_hp, num_sp)

    def special_attack(self, opp: Entity) -> str:
        if bool(randint(0, 1)):
            return self.swoop(opp)

        return self.windblast(opp)
