import pygame
from sprite import Sprite


class Bullet(Sprite):

    image = None
    rect = None
    should_die = False

    def __init__(self, spaceship_pos):
        super(Bullet, self).__init__()

        self.image = pygame.image.load('recources/'
                                       'spaceship/bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = spaceship_pos.x
        self.rect.y = spaceship_pos.y

    def update(self):
        if self.rect.y < 0:
            self.should_die = True
        self.rect.y -= 1

    def explode(self):
        print "battleship destroyed"
