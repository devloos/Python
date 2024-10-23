from entity import Entity
from dragon import Dragon
from random import randint


class Flying:
    def swoop(self: Dragon, opp: Entity) -> str:
        if self.special_attacks == 0:
            return f'{self.name} tries to swoop {opp.name}, but it is all out of fuel.'

        dmg = randint(4, 8)
        opp.take_damage(dmg)
        self.decrement_special_attacks()

        return f'{self.name} swoops {opp.name} from underneath for {dmg} damage!'

    def windblast(self: Dragon, opp: Entity) -> str:
        if self.special_attacks == 0:
            return f'{self.name} tries to windblast {opp.name}, but it is all out of fuel.'

        dmg = randint(3, 7)
        opp.take_damage(dmg)
        self.decrement_special_attacks()

        return f'{self.name} windblasts {opp.name} for {dmg} damage!'
