import pygame
from pygame.sprite import Sprite
from pygame.mixer import Sound


class Player(Sprite):
    def __init__(self, pos: tuple):
        super().__init__()

        player_walk_1 = pygame.image.load(
            'graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load(
            'graphics/player/player_walk_2.png').convert_alpha()

        self.gravity = 0
        self.walk_frames = [player_walk_1, player_walk_2]
        self.walk_frame_index = 0
        self.jump = pygame.image.load(
            'graphics/player/jump.png').convert_alpha()
        self.jump_sound = Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.05)

        self.image = self.walk_frames[self.walk_frame_index]
        self.rect = self.image.get_rect(midbottom=pos)

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -10
            self.jump_sound.play()

        mouse_buttons = pygame.mouse.get_pressed()

        if mouse_buttons[0] and self.rect.collidepoint(pygame.mouse.get_pos()) and self.rect.bottom >= 300:
            self.gravity = -10
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 0.5
        self.rect.y += self.gravity

        if (self.rect.bottom > 300):
            self.gravity = 0
            self.rect.bottom = 300

    def update_animation(self):
        if (self.rect.bottom < 300):
            self.image = self.jump
        else:
            self.walk_frame_index += 0.2
            self.image = self.walk_frames[int(self.walk_frame_index) % 2]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.update_animation()
