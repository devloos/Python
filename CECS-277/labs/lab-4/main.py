'''
Written by: Israel Fausto, Carlos Aguilera
Date: 09/18/24

Description:
    This program is a text-based treasure-hunting game called "Treasure Hunt!"
    where the player navigates a grid to collect treasures while avoiding traps.
    The game is controlled by WASD keys for movement, L to look around, and Q to quit.
'''
VALID_CHOICES = ['W', 'A', 'S', 'D', 'L', 'Q']

DIRECTION_MAP = {
    'W': (-1, 0),
    'A': (0, -1),
    'S': (1, 0),
    'D': (0, 1),
}

UPPER_BOUND = 6

PLAYER_CHAR = 'P'
TREASURE_CHAR = 'T'
TRAP_CHAR = 'X'


class Player:
    '''Holds the position of player.
    Attributes:
        row: int
        col: int
    '''

    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    def get_pos(self) -> tuple[int, int]:
        return (self.row, self.col)


def read_map() -> list[list[str]]:
    '''
      Read the contents of map.txt and return a
      2D array.
    '''

    file = open('map.txt')
    game_map: list[list[str]] = []
    end_of_file = False

    while not end_of_file:
        line = file.readline().strip('\n')

        if (not line):
            end_of_file = True
            continue

        game_map.append(line.split(' '))

    return game_map


def display_map(map: list[list[str]], player: Player):
    '''
      Displays the player map, it also print
      P for the players current pos.
    '''
    player_pos = (player.row, player.col)

    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if player_pos == (row_idx, col_idx):
                print(PLAYER_CHAR, end=' ')
            else:
                print(col, end=' ')

        print()


def move_player(player: Player, dir: tuple[int, int], upper_bound: int) -> bool:
    '''
      Given a direction to move the player,
      we check bounds and update player position.
    '''
    new_row = player.row + dir[0]
    new_col = player.col + dir[1]

    if new_row < 0 or new_col < 0:
        return False

    if new_row > upper_bound or new_col > upper_bound:
        return False

    player.row = new_row
    player.col = new_col

    return True


def count_treasures_traps(map: list[list[str]], player: Player, upper_bound: int) -> tuple[int, int]:
    '''
      Given 8 possible directions, we check bounds and increase
      count for treasure_count or trap_count accordingly.
    '''
    directions = [
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    treasure_count = 0
    trap_count = 0

    for dir in directions:
        row = player.row + dir[0]
        col = player.col + dir[1]

        if row < 0 or row > upper_bound:
            continue

        if col < 0 or col > upper_bound:
            continue

        char = map[row][col]

        if char == TREASURE_CHAR:
            treasure_count += 1
        elif char == TRAP_CHAR:
            trap_count += 1

    return treasure_count, trap_count


def main():
    print('Treasure Hunt!')
    print('Find the 7 treasures without getting')
    print('caught in a trap. Look around to spot')
    print('nearby traps and treasures.')

    player = Player(0, 0)
    player_map = [['.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.']]

    game_map = read_map()

    # Storing treasure positions for easy tracking.
    treasure_positions = []

    for row_idx, row in enumerate(game_map):
        for col_idx, col in enumerate(row):
            if col == TREASURE_CHAR:
                treasure_positions.append((row_idx, col_idx))

    while True:
        display_map(player_map, player)
        choice = input(
            'Enter Direction (WASD or L to Look around or Q to quit): '
        ).upper()

        if choice not in VALID_CHOICES:
            print('Invalid input! Try again.')
            continue

        if choice == 'Q':
            print('Thanks for playing!')
            break

        if choice == 'L':
            treasure_count, trap_count = count_treasures_traps(
                game_map, player, UPPER_BOUND
            )

            print(f'You detect {treasure_count} treasures nearby.')
            print(f'You detect {trap_count} traps nearby.')
            continue

        # If we get here then the player wants to move
        direction = DIRECTION_MAP[choice]

        if not move_player(player, direction, UPPER_BOUND):
            print('You cannot move that direction.')

        # if player pos in treasure pos we update map and remove
        # treasure position
        if player.get_pos() in treasure_positions:
            treasure_positions.remove(player.get_pos())
            player_map[player.row][player.col] = TREASURE_CHAR

            print('You found treasure!')
            print(f'There are {len(treasure_positions)} treasures remaining.')

        if game_map[player.row][player.col] == TRAP_CHAR:
            print('You were caught in a trap!')
            print(f'You found {7 - len(treasure_positions)} treasures.')

            display_map(player_map, player)

            print('Game Over!')
            break

        if len(treasure_positions) == 0:
            print('You won! Come play again.')
            break


main()
