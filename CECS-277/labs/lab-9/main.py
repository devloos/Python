'''
Written by: Israel Fausto, Carlos Aguilera
Date: 10/16/24

Description:
    This program acts as a dragon; hero simulator. It takes advantage of multiple
    inheritance and mixins by creating various types of dragons and inheriting
    off of a base "Entity" class. Defeat all the dragons using either the
    heros basic or special attacks.
'''
from check_input import get_int_range
from hero import Hero
from dragon import Dragon
from flying_dragon import FlyingDragon
from fire_dragon import FireDragon
from flying_fire_dragon import FlyingFireDragon
from random import choice, randint


SWORD = 1
ARROW = 2


def main():
    print('What is your name, challenger?')
    hero_name = input()

    hero = Hero(hero_name, 50)

    dragons: list[Dragon] = [
        FireDragon('Gronkle', 15, 3),
        FlyingDragon('Timberjack', 10, 3),
        FlyingFireDragon('Deadly Nadder', 20, 2)
    ]

    is_hero_winner = False

    print(f'Welcome to dragon training, {hero.name}')
    print('You must defeat 3 dragons.')

    while True:
        print()
        print(hero)

        for i, dragon in enumerate(dragons):
            print(f'{i + 1}. {dragon}')

        index = get_int_range('Choose a dragon to attack: ', 1, 3) - 1

        print()
        print('Attack with:')
        print('1. Sword (2 D6)')
        print('2. Arrow (1 D12)')

        attack = get_int_range('Enter weapon: ', 1, 2)

        if attack == SWORD:
            print(hero.basic_attack(dragons[index]))
        elif attack == ARROW:
            print(hero.special_attack(dragons[index]))

        dragons = list(filter(lambda dragon: dragon.hp > 0, dragons))

        if len(dragons) == 0:
            is_hero_winner = True
            break

        dragon = choice(dragons)

        if bool(randint(0, 1)):
            print(dragon.basic_attack(hero))
        else:
            print(dragon.special_attack(hero))

        if hero.hp <= 0:
            is_hero_winner = False
            break

    if is_hero_winner:
        print('Congratulations! You have defeated all three dragons, you have passed the trials.')
    else:
        print('Sorry! You were knocked out cold by the dragons.')


main()
