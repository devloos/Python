from entity import Entity
from random import randint


class Hero(Entity):

    def basic_attack(self, opp: Entity) -> str:
        dmg = randint(2, 6)
        opp.take_damage(dmg)

        return f'{self.name} slashes the {opp.name} with their sword for {dmg} damage!'

    def special_attack(self, opp: Entity) -> str:
        dmg = randint(1, 12)
        opp.take_damage(dmg)

        return f'{self.name} hits the {opp.name} with an arrow for {dmg} damage'
