from entity import Entity
from random import randint
from map import Map


class Hero(Entity):
    def __init__(self, name):
        super().__init__(name, 25)
        self._loc: list[int] = [0, 0]
        self.map = Map()

    def go_north(self) -> str:
        row, col = self._loc

        if row == 0:
            return 'o'

        row -= 1
        self._loc = [row, col]

        return self.map[row][col]

    def go_south(self) -> str:
        row, col = self._loc

        if row == len(self.map) - 1:
            return 'o'

        row += 1
        self._loc = [row, col]

        return self.map[row][col]

    def go_west(self) -> str:
        row, col = self._loc

        if col == 0:
            return 'o'

        col -= 1
        self._loc = [row, col]

        return self.map[row][col]

    def go_east(self) -> str:
        row, col = self._loc

        if col == len(self.map[row]) - 1:
            return 'o'

        col += 1
        self._loc = [row, col]

        return self.map[row][col]

    def attack(self, entity: Entity):
        dmg = randint(2, 5)
        entity.take_damage(dmg)

        return f'{self.name} attacks a {entity.name} for {dmg} damage'

    @property
    def loc(self) -> list[int]:
        return self._loc
