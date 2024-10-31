'''
Written by: Israel Fausto, Carlos Aguilera
Date: 10/30/24

Description:
    This program is a dungeon and monster game where the user must
    traverse a maze in order to find the exit. All this while encountering
    spells, monsters, and nothingness. Choose which direction to move the user
    and whether to attack or run away from monsters. The primary focus of this
    program was to implement a singleton named Map that both the hero entity would
    use and the main function. Essentially the singleton main goal was to hold
    global state.
'''
from hero import Hero
from map import Map
from check_input import get_int_range
from enemy import Enemy

SCRIPTS = {
    'o': 'You cannot go that way...',
    'n': 'There is nothing here...',
    's': 'You need to get out of here...',
    'i': 'You found a Health Potion! You drink it to restore your health.',
    'f': 'Congratulations! You found the exit.'
}


def main():
    name = input('What is your name, traveler? ')

    hero = Hero(name)
    map = Map()

    while True:
        print(hero)
        print(map.show_map(hero.loc))

        print('1. Go North')
        print('2. Go South')
        print('3. Go East')
        print('4. Go West')
        print('5. Quit')

        option = get_int_range('Enter choice: ', 1, 5)

        char = ''
        match option:
            case 1:
                char = hero.go_north()
            case 2:
                char = hero.go_south()
            case 3:
                char = hero.go_east()
            case 4:
                char = hero.go_west()
            case 5:
                print('Better luck next time!')
                break

        if char in SCRIPTS:
            print(SCRIPTS[char])

        if char == 'm':
            enemy = Enemy()
            while True:
                print(enemy)
                print(f'1. Attack {enemy.name}')
                print('2. Run Away')

                option = get_int_range('Enter choice: ', 1, 2)

                # ran away
                if option == 2:
                    print('You ran away!')
                    break

                print(hero.attack(enemy))

                # enemy defeated
                if enemy.hp == 0:
                    print(f'You have slain a {enemy.name}')
                    map.remove_at_loc(hero.loc)
                    break

                print(enemy.attack(hero))
                print()

                if hero.hp == 0:
                    break

            if hero.hp == 0:
                print('You have been slain, better luck next time!')
                break

        elif char == 'i':
            hero.heal()
            map.remove_at_loc(hero.loc)
        elif char == 'f':
            break

        map.reveal(hero.loc)
        print()

    print('Game Over')


main()
