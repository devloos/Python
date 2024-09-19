""" Rock-Paper-Scissors

Written by: Carlos Aguilera
Date: 09/04/24

Description:
    This program is a Rock-Paper-Scissors (RPS) game. The user plays the computer which randomly
    chooses between RPS. User is also able to display the score and quit the game.
"""
from check_input import get_int_range
from random import choice

ROCK = 'R'
PAPER = 'P'
SCISSORS = 'S'

BACK = 'B'

VALID_CHOICES = [ROCK, PAPER, SCISSORS, BACK]
VALID_WEAPONS = [ROCK, PAPER, SCISSORS]

READABLE_WEAPONS = {
    ROCK: 'Rock',
    PAPER: 'Paper',
    SCISSORS: 'Scissors',
}

WINNING_MOVES = {
    ROCK: [SCISSORS],
    PAPER: [ROCK],
    SCISSORS: [PAPER],
}

TIE = 0
PLAYER = 1
COMPUTER = 2


def weapon_menu() -> str:
    """ Displays the weapon menu and gets user input.
    User input is validated and returned."""

    print('Choose your weapon:')
    print('R. Rock')
    print('P. Paper')
    print('S. Scissors')
    print('B. Back')

    choice = ''
    isInvalid = True

    while isInvalid:
        choice = input('Choice: ')

        if choice in VALID_CHOICES:
            isInvalid = False
        else:
            print(f'{choice} is not a valid choice.')

    return choice


def comp_weapon() -> str:
    return choice(VALID_WEAPONS)


def find_winner(player_weapon: str, computer_weapon: str) -> int:
    if player_weapon == computer_weapon:
        return TIE

    # if the computer weapon is in the winning moves of the player
    # then the player wins
    if computer_weapon in WINNING_MOVES[player_weapon]:
        return PLAYER

    return COMPUTER


def display_score(player_score: int, computer_score: int):
    print(f'Player = {player_score}')
    print(f'Computer = {computer_score}')


def main():
    menu_running = True
    player_score = 0
    computer_score = 0

    while (menu_running):
        print('RPS Menu:')
        print('1. Play game')
        print('2. Show Score')
        print('3. Quit')

        choice = get_int_range('Choice: ', 1, 3)

        match choice:
            case 1:
                while True:
                    player_weapon = weapon_menu()

                    if player_weapon == BACK:
                        break

                    computer_weapon = comp_weapon()

                    print(f'You chose {READABLE_WEAPONS[player_weapon]}')
                    print(f'Computer chose {READABLE_WEAPONS[computer_weapon]}')

                    winner = find_winner(player_weapon, computer_weapon)

                    if winner == TIE:
                        print('Tie')
                    elif winner == PLAYER:
                        player_score += 1
                        print('You win')
                    elif winner == COMPUTER:
                        computer_score += 1
                        print('Computer wins')

            case 2:
                display_score(player_score, computer_score)
            case 3:
                menu_running = False

    print('Final Score:')
    display_score(player_score, computer_score)


main()
