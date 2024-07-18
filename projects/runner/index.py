import pygame
from sys import exit
from random import choice

from pygame.sprite import Group, GroupSingle
from player import Player
from enemy import Enemy, TYPE_FLY, TYPE_SNAIL
from pygame.mixer import Sound

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

background_sound = Sound('audio/music.wav')
background_sound.set_volume(0.05)
background_sound.play(loops=-1)

player = GroupSingle()
player.add(Player((80, 300)))

enemies = Group()

obstacle_event = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_event, 1300)

sky_surf = pygame.image.load('graphics/sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()
title_surf = font.render('PIXEL RUNNER', False, (64, 64, 64))
instructions_surf = font.render('Press space to play!', False, (64, 64, 64))

player_stand_surf = pygame.image.load(
    'graphics/player/player_stand.png').convert_alpha()
player_stand_surf = pygame.transform.rotozoom(player_stand_surf, 0, 2)

title_rect = title_surf.get_rect(center=(SCREEN_WIDTH / 2, 35))
instructions_rect = instructions_surf.get_rect(center=(SCREEN_WIDTH / 2, 350))
player_stand_rect = player_stand_surf.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
)


def display_background():
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))


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


def collision(player: GroupSingle, enemies: Group) -> bool:
    return pygame.sprite.spritecollide(player.sprite, enemies, False)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_event:
                enemies.add(
                    Enemy(choice([TYPE_SNAIL, TYPE_SNAIL, TYPE_SNAIL, TYPE_FLY])))
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    enemies.empty()
                    start_time = int(pygame.time.get_ticks() / 1000)
                    game_active = True

    if game_active:
        if collision(player, enemies):
            game_active = False

        score = int(pygame.time.get_ticks() / 1000) - start_time

        display_background()
        display_score()

        enemies.draw(screen)
        enemies.update()

        player.draw(screen)
        player.update()
    else:
        display_menu()

    pygame.display.update()
    clock.tick(60)
