from pygame.locals import *
from socket import *
from util import load_png
import pygame

VERSION = "0.4"


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((250, 250))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        screen.blit(background, (0, 0))
        screen.blit(text, textpos)

        pygame.display.flip()


if __name__ == '__main__':
    main()
