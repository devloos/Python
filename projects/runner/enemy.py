
import pygame
from random import randint
from pygame.sprite import Sprite

TYPE_SNAIL = 'snail'
TYPE_FLY = 'fly'


class Enemy(Sprite):
    def __init__(self, type: str) -> None:
        super().__init__()

        self.frames: list[pygame.Surface] = []
        self.frame_index = 0
        self.type = type

        y_pos = 0

        if self.type == TYPE_SNAIL:
            snail_frame_1 = pygame.image.load(
                'graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load(
                'graphics/snail/snail2.png').convert_alpha()

            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300
        elif self.type == TYPE_FLY:
            fly_frame_1 = pygame.image.load(
                'graphics/fly/fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load(
                'graphics/fly/fly2.png').convert_alpha()

            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 200
        else:
            raise Exception()

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(bottomleft=(randint(800, 1000), y_pos))

    def update_animation(self):
        if self.type == TYPE_SNAIL:
            self.frame_index += 0.06
        elif self.type == TYPE_FLY:
            self.frame_index += 0.2

        self.image = self.frames[int(self.frame_index) % 2]

    def move(self):
        self.rect.x -= 7

    def check_destroy(self):
        if self.rect.right < 0:
            self.kill()

    def update(self):
        self.update_animation()
        self.move()
        self.check_destroy()
