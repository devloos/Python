from pygame.sprite import Sprite
from util import load_png
from pygame import Rect
import pygame
import math


class Ball(Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector: pygame.Vector2):
        super().__init__()
        self.image, self.rect = load_png('snail.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def get_input(self):
        return pygame.mouse.get_pos()

    def update(self):
        newpos = self.get_input()

        self.rect.topleft = newpos

        if self.rect.collidepoint(self.area.right, 0):
            print('left collision')

    def calcnewpos(self, rect: Rect, vector: pygame.Vector2):
        (angle, z) = vector
        (dx, dy) = (z * math.cos(angle), z * math.sin(angle))

        return rect.move(dx, dy)
