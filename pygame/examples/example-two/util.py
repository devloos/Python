import os
import pygame
from pygame import Surface, Rect


def load_png(filename: str) -> tuple[Surface, Rect]:
    """ Load image and return image object"""
    fullname = os.path.join("assets", filename)

    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit

    return image, image.get_rect()
