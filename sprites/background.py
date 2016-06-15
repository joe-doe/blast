import pygame
from sprite import Sprite
from constants import WINDOW_HEIGHT


class Background(Sprite):
    speed = None

    def __init__(self, img, speed):
        super(Background, self).__init__()

        self.speed = speed

        self.image = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = WINDOW_HEIGHT - self.rect.h

        self.x_step = 0
        self.y_step = self.speed

    def update(self):
        self.rect.y += self.y_step
