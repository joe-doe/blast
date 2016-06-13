import pygame
from constants import WINDOW_HEIGHT


class Background(pygame.sprite.Sprite):
    image = None
    rect = None
    speed = 0

    def __init__(self, img, speed):
        super(Background, self).__init__()
        self.image = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()
        self.rect.y = WINDOW_HEIGHT - self.rect.h
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
