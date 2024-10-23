from dragon import Dragon
from entity import Entity
from random import randint


class Fire:
    def fireblast(self: Dragon, opp: Entity) -> str:
        if self.special_attacks == 0:
            return f'{self.name} tries to engulf {opp.name} in flames, but it is all out of fuel.'

        dmg = randint(5, 9)
        opp.take_damage(dmg)
        self.decrement_special_attacks()

        return f'{self.name} engulfs {opp.name} in flames for {dmg} damage!'

    def fireball(self: Dragon, opp: Entity) -> str:
        if self.special_attacks == 0:
            return f'{self.name} tries to spit a fireball at {opp.name}, but it is all out of fuel.'

        dmg = randint(4, 8)
        opp.take_damage(dmg)
        self.decrement_special_attacks()

        return f'{self.name} spits a fireball at {opp.name} for {dmg} damage!'
