import pygame
from constants import *
from sprite import Sprite
from sprites.bullet import Bullet


class Battleship(Sprite):

    def __init__(self, friend_bullets):
        super(Battleship, self).__init__()

        self.friend_bullets = friend_bullets
        self.image = pygame.image.load('resources/spaceship/'
                                       'spaceship_1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_WIDTH/2 - self.rect.w/2
        self.rect.y = WINDOW_HEIGHT - self.rect.h*3

        self.x_step = 6
        self.y_step = 6

    def update(self):
        pass

    def fire(self):
        self.friend_bullets.add(Bullet(self.rect))

    def go_left(self):
        if self.rect.x == 0:
            self.rect.x = WINDOW_WIDTH - self.rect.w
        else:
            self.rect.x -= self.x_step

    def go_right(self):
        if self.rect.x == WINDOW_WIDTH - self.rect.w:
            self.rect.x = 0
        else:
            self.rect.x += self.x_step

    def go_up(self):
        if self.rect.y == 0:
            self.rect.y = WINDOW_HEIGHT - self.rect.h
        else:
            self.rect.y -= self.y_step

    def go_down(self):
        if self.rect.y == WINDOW_HEIGHT - self.rect.h:
            self.rect.y = 0
        else:
            self.rect.y += self.y_step
