import pygame
from sprite import Sprite


class Bullet(Sprite):

    def __init__(self, spaceship_pos):
        super(Bullet, self).__init__()

        self.image = pygame.image.load('resources/'
                                       'spaceship/bullet.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = spaceship_pos.x
        self.rect.y = spaceship_pos.y

        self.x_step = 0
        self.y_step = 8

    def update(self):
        if self.rect.y < 0:
            self.out_of_bounds = True
        self.rect.y -= self.y_step
