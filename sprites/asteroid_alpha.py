import pygame
from constants import *
from asteroids import Asteroids
from random import (
    randint,
    uniform
)


class AsteroidAlpha(Asteroids):

    images_set = []
    images_explosion_set = []
    current_image_idx = 1
    should_explode = False

    def __init__(self):
        super(AsteroidAlpha, self).__init__()

    def setup(self):
        self.load_images_set()
        self.load_images_explosion_set()
        self.image = pygame.image.load('recources/asteroids/'
                                       'a_1/1.png').convert_alpha()
        self.rect = self.image.get_rect()

    def start(self):
        self.rect.x = uniform(0, WINDOW_WIDTH-self.rect.w)
        self.rect.y = uniform(-50, 0)
        self.x_step = uniform(1, 2)
        self.y_step = uniform(1, 2)

        self.x_direction = randint(0, 1)

    def update(self):
        if self.rect.x > WINDOW_WIDTH + self.rect.w  \
                or self.rect.x < -self.rect.w  \
                or self.rect.y >= WINDOW_HEIGHT + self.rect.h:
            self.should_die = True
            return

        if self.x_direction == 0:
            self.go_right()
        else:
            self.go_left()

        self.go_down()
        if self.should_explode:
            self.load_next_image(self.images_explosion_set)
        else:
            self.load_next_image(self.images_set)

    def go_left(self):
        self.rect.x -= self.x_step

    def go_right(self):
        self.rect.x += self.x_step

    def go_up(self):
        self.rect.y -= self.y_step

    def go_down(self):
        self.rect.y += self.y_step

    def explode(self):
        for img in self.images_explosion_set:
            self.image = img

    def load_images_set(self):
        for i in range(1, 19, 1):
            self.images_set.append(pygame.image.load('recources'
                                                     '/asteroids/a_1/'
                                                     +str(i)
                                                     +'.png').convert_alpha())

    def load_images_explosion_set(self):
        for i in range(1, 8, 1):
            self.images_explosion_set.append(pygame.image.load('recources'
                                                               '/asteroids'
                                                               '/explosions'
                                                               '/a_1/'
                                                               +str(i)
                                                               +'.png')
                                             .convert_alpha())

    def load_next_image(self, img_list, ):
        try:
            self.current_image_idx += 1
            self.image = self.img_list[self.current_image_idx]
        except IndexError:
            self.current_image_idx = 0
