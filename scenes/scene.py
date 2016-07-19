import threading
import pygame
from constants import *


class Scene(threading.Thread):
    background = None
    extra_sprites = None
    load_next_scene = None

    def __init__(self):
        super(Scene, self).__init__()

        self.load_next_scene = False
        self.setDaemon(True)
        self.extra_sprites = pygame.sprite.Group()
        self.initialize_scene()

    def initialize_background(self):
        """
        Must override in derived classes
        """
        pass

    def initialize_sprites(self):
        """
        Must override in derived classes
        """
        pass

    def update(self):
        """
        Called in main loop
        """
        pass

    def draw(self, screen):
        """
        Called in main loop
        """
        pass

    def initialize_scene(self):
        self.initialize_background()
        self.initialize_sprites()

    def print_out(self, screen, string, position, size=30, color=WHITE):

        font = pygame.font.Font(None, size)

        print_text = font.render(
            string,
            True,
            color)

        pos = (0, 0)
        offset = 50

        if position == 'top-left':
            pos = (
                offset,
                offset
            )
        elif position == 'top-center':
            pos = (
                (WINDOW_WIDTH / 2) - (print_text.get_width() / 2),
                offset
            )
        elif position == 'top-right':
            pos = (
                WINDOW_WIDTH - print_text.get_width() - offset,
                offset
            )
        elif position == 'center-left':
            pos = (
                offset,
                WINDOW_HEIGHT / 2
            )
        elif position == 'center':
            pos = (
                (WINDOW_WIDTH / 2) - (print_text.get_width() / 2),
                WINDOW_HEIGHT / 2
            )
        elif position == 'center-right':
            pos = (
                WINDOW_WIDTH - print_text.get_width() - offset,
                WINDOW_HEIGHT / 2
            )
        elif position == 'bottom-left':
            pos = (
                offset,
                WINDOW_HEIGHT - print_text.get_height() - offset
            )
        elif position == 'bottom-center':
            pos = (
                (WINDOW_WIDTH / 2) - (print_text.get_width() / 2),
                WINDOW_HEIGHT - print_text.get_height() - offset
            )
        elif position == 'bottom-right':
            pos = (
                WINDOW_WIDTH - print_text.get_width() - offset,
                WINDOW_HEIGHT - print_text.get_height() - offset
            )

        screen.blit(print_text, pos)
