from entity import Entity
from random import choice, randint

POSSIBLE_ENEMY_NAMES = ['Goblin', 'Vampire', 'Ghoul', 'Skeleton', 'Zombie']


class Enemy(Entity):
    def __init__(self):
        super().__init__(choice(POSSIBLE_ENEMY_NAMES), randint(4, 8))

    def attack(self, entity: Entity):
        dmg = randint(1, 4)
        entity.take_damage(dmg)

        return f'{self.name} attacks a {entity.name} for {dmg} damage'

    def __str__(self):
        return f'You encountered a {self.name}\nHP: {self.hp}/{self._max_hp}'
