'''
Written by: Israel Fausto, Carlos Aguilera
Date: 10/02/24

Description:
    This code implements a simplified dice game inspired by Yahtzee. A `Player` object is created,
    and during each turn, the player rolls dice. The outcome is evaluated to check for special
    combinations like "three of a kind," a "series of three," or a "pair," with corresponding
    messages printed to the screen. The player's points are updated and displayed after each roll.
    The game continues in a loop until the player chooses to stop, at which point the final score
    is displayed. Input validation is handled through a `get_yes_no()` function to confirm whether 
    the player wants to play another round.
'''
from player import Player
from check_input import get_yes_no


def take_turn(player: Player):
    player.roll_dice()
    print(player)

    if player.has_three_of_a_kind():
        print('You got 3 of a kind!')
    elif player.has_series():
        print('You got a series of 3!')
    elif player.has_pair():
        print('You got a pair!')
    else:
        print('Aww. Too Bad.')

    print(f'Score = {player.get_points()}')


def main():
    player = Player()
    print('-Yahtzee-')

    while True:
        take_turn(player)

        if not get_yes_no('Play again? (Y/N): '):
            break

        print()

    print('Game Over.')
    print(f'Final Score = {player.get_points()}')


main()
