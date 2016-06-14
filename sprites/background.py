import pygame
from sprite import Sprite
from constants import WINDOW_HEIGHT


class Background(Sprite):
    speed = 0

    def __init__(self, img, speed):
        super(Background, self).__init__()

        self.image = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = WINDOW_HEIGHT - self.rect.h

        self.x_step = 0
        self.y_step = 1

    def update(self):
        self.rect.y += self.y_step
