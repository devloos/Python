EMPTY_REVEALED_MAP = [
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
]
MAP_1 = [
    ['s', 'm', 'n', 'm', 'n'],
    ['n', 'n', 'm', 'n', 'i'],
    ['m', 'n', 'm', 'n', 'n'],
    ['m', 'i', 'n', 'm', 'm'],
    ['n', 'm', 'n', 'm', 'f'],
]


class Map:
    _instance = None
    _initialized = False

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if not Map._initialized:
            self._map: list[list[str]] = MAP_1
            self._revealed: list[list[bool]] = EMPTY_REVEALED_MAP

            Map._initialized = True

    def show_map(self, loc) -> str:
        formatted_str = ''

        for i, row in enumerate(self._map):
            for j, value in enumerate(row):
                if loc == [i, j]:
                    # player location
                    formatted_str += '*'
                elif self._revealed[i][j]:
                    # player has already visited
                    formatted_str += value
                else:
                    formatted_str += 'X'

                formatted_str += ' '

            formatted_str += '\n'

        return formatted_str

    def reveal(self, loc):
        row, col = loc
        self._revealed[row][col] = True

    def remove_at_loc(self, loc):
        row, col = loc
        self._map[row][col] = 'n'

    def __getitem__(self, row) -> list[str]:
        return self._map[row]

    def __len__(self) -> int:
        return len(self._map)
