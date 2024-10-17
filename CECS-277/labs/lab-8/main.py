'''
Written by: Israel Fausto, Carlos Aguilera
Date: 10/16/24

Description:
    This program is a text-based racing game called "Rad Racer!" where players can
    choose from three types of vehicles: a car, motorcycle, or truck, and race down
    a track while avoiding obstacles ('O'). The player controls their vehicle ('P')
    and can perform actions like speeding up, slowing down, or using a special move.
    Obstacles are randomly placed on the track, and players must strategically choose
    how to handle them to avoid crashing. The game ends when all vehicles reach the
    finish line, and their rankings are displayed based on who finishes first.
'''
from check_input import get_int_range
from car import Car
from motorcycle import Motorcycle
from truck import Truck
from vehicle import Vehicle
from random import randint


def main():
    print('Rad Racer!')
    print("Choose a vehicle and race it down the track (player = 'P').", end=' ')
    print("Slow down for obstacles ('0') or else you'll crash!")

    vehicles: list[Vehicle] = [
        Car(),
        Motorcycle(),
        Truck(),
    ]

    track: list[list[str]] = [
        ['-'] * 100,
        ['-'] * 100,
        ['-'] * 100,
    ]

    # display description
    for i in range(3):
        print(f'{i + 1}. {vehicles[i].description_string()}')

    # set obstacles
    for row in range(3):
        while True:
            obstacle_one = randint(2, 100)
            obstacle_two = randint(2, 100)

            if obstacle_one != obstacle_two and abs(obstacle_one - obstacle_two) > 2:
                break

        track[row][obstacle_one] = 'O'
        track[row][obstacle_two] = 'O'

    vehicle_choice = get_int_range('Choose your vehicle (1-3): ', 1, 3) - 1
    running = True
    vehicles_finished: list[Vehicle] = []

    while running:
        print()

        # print and set vehicle pos
        for (row, vehicle) in enumerate(vehicles):
            if row == vehicle_choice:
                track[row][vehicle.position] = 'P'
            else:
                track[row][vehicle.position] = vehicle.initial

            print(vehicle)

        # print track
        for row in range(3):
            for col in range(100):
                print(track[row][col], end='')

            print()

        # replace initial with *
        for (row, vehicle) in enumerate(vehicles):
            track[row][vehicle.position] = '*'

        if vehicles[vehicle_choice] not in vehicles_finished:
            user_action = get_int_range(
                'Choose action (1. Fast, 2. Slow, 3. Special Move): ', 1, 3
            )

        print()

        for (row, vehicle) in enumerate(vehicles):
            if vehicle in vehicles_finished:
                continue

            try:
                index_of_obstacle = track[row].index('O', vehicle.position)
                dist_to_obstacle = index_of_obstacle - vehicle.position
            except:
                # set to a number that would not be reached
                # this allows the user to always be less than the dist of object
                dist_to_obstacle = 1000

            action = randint(1, 3)

            if row == vehicle_choice and (vehicle not in vehicles_finished):
                action = user_action

            match action:
                case 1:
                    print(vehicle.fast(dist_to_obstacle))
                case 2:
                    print(vehicle.slow(dist_to_obstacle))
                case 3:
                    print(vehicle.special_move(dist_to_obstacle))

            if vehicle.position >= 99:
                vehicle.position = 99
                vehicles_finished.append(vehicle)

        if len(vehicles_finished) == 3:
            running = False

    print()

    print(f'1st place: {vehicles_finished[0]}')
    print(f'2nd place: {vehicles_finished[1]}')
    print(f'3rd place: {vehicles_finished[2]}')


main()
