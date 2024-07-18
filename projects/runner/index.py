import pygame
from collections import defaultdict
from sys import exit
from random import randint

# pygame setup
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Runner')

clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
player_gravity = 0
player_walk_index = 0
snail_frame_index = 0
fly_frame_index = 0

# list of string and Rect (string being surface type e.g. snail)
entities: list[list[str, pygame.Rect]] = []

obstacle_event = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_event, 1300)


sky_surf = pygame.image.load('graphics/sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
fly_frame_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
title_surf = font.render('PIXEL RUNNER', False, (64, 64, 64))
instructions_surf = font.render('Press space to play!', False, (64, 64, 64))
player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
player_walk_1 = pygame.image.load(
    'graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load(
    'graphics/player/player_walk_2.png').convert_alpha()
player_stand_surf = pygame.image.load(
    'graphics/player/player_stand.png').convert_alpha()
player_stand_surf = pygame.transform.rotozoom(player_stand_surf, 0, 2)


title_rect = title_surf.get_rect(center=(SCREEN_WIDTH / 2, 35))
instructions_rect = instructions_surf.get_rect(center=(SCREEN_WIDTH / 2, 350))
player_rect = player_walk_1.get_rect(midbottom=(80, 300))
player_stand_rect = player_stand_surf.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
)

player_walk = [player_walk_1, player_walk_2]
snail_frame = [snail_frame_1, snail_frame_2]
fly_frame = [fly_frame_1, fly_frame_2]


def display_score():
    score_surf = font.render(f'Score: {score}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(SCREEN_WIDTH / 2, 50))

    score_bg_rect = pygame.Rect((SCREEN_WIDTH / 2) - 90, 28, 180, 35)
    pygame.draw.rect(screen, '#C0E8EC', score_bg_rect, border_radius=5)
    screen.blit(score_surf, score_rect)


def display_menu():
    score_surf = font.render(f'Score: {score}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(SCREEN_WIDTH / 2, 75))

    screen.fill((94, 129, 162))
    screen.blit(player_stand_surf, player_stand_rect)
    screen.blit(title_surf, title_rect)
    screen.blit(instructions_surf, instructions_rect)

    if bool(score):
        screen.blit(score_surf, score_rect)


def display_entities(entities: list[tuple[str, pygame.Rect]]):
    global snail_frame_index, fly_frame_index

    if not entities:
        return

    for (type, rect) in entities:
        if type == 'snail':
            snail_frame_index += 0.1
            screen.blit(snail_frame[int(snail_frame_index) % 2], rect)
        elif type == 'fly':
            fly_frame_index += 0.1
            screen.blit(fly_frame[int(fly_frame_index) % 2], rect)


def move_entities(entities: list[tuple[str, pygame.Rect]]) -> list[tuple[str, pygame.Rect]]:
    if not entities:
        return []

    newEntities = []
    for (type, rect) in entities:
        rect.x -= 8

        if rect.right > 0:
            newEntities.append((type, rect))

    return newEntities


def entity_collision(entities: list[tuple[str, pygame.Rect]], player_rect: pygame.Rect) -> bool:
    if not entities:
        return False

    for (_, rect) in entities:
        if rect.colliderect(player_rect):
            return True

    return False


def display_background():
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))


def display_player():
    global player_walk_index

    if (player_rect.bottom < 300):
        screen.blit(player_jump, player_rect)
    else:
        player_walk_index += 0.1
        screen.blit(player_walk[int(player_walk_index) % 2], player_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE and player_rect.bottom >= 300):
                    player_gravity = -9.5

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -9.5

            if event.type == obstacle_event:
                type = 'snail' if bool(randint(0, 2)) else 'fly'
                entity_rect = None

                if type == 'snail':
                    entity_rect = snail_frame_1.get_rect(
                        bottomleft=(randint(800, 1000), 300)
                    )
                else:
                    entity_rect = fly_frame_1.get_rect(
                        bottomleft=(randint(800, 1000), 200)
                    )

                entities.append((type, entity_rect))
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    entities = []
                    player_gravity = 0
                    start_time = int(pygame.time.get_ticks() / 1000)
                    game_active = True

    if game_active:
        entities = move_entities(entities)

        if entity_collision(entities, player_rect):
            game_active = False

        player_gravity += 0.5
        player_rect.y += player_gravity

        if (player_rect.bottom > 300):
            player_gravity = 0
            player_rect.bottom = 300

        score = int(pygame.time.get_ticks() / 1000) - start_time

        display_background()
        display_score()
        display_entities(entities)
        display_player()
    else:
        display_menu()

    pygame.display.update()
    clock.tick(60)
