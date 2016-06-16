import sys
import os
from random import (
    randint,
    uniform
)
from constants import *
from sprites.animated_sprite import AnimatedSprite
from sprites.sprite_data import AnimatedSpriteData


class Asteroid(AnimatedSprite):

    def __init__(self, asteroid_data):
        super(Asteroid, self).__init__(asteroid_data)

    def initialize_sprite(self):
        self.rect.x = uniform(0, WINDOW_WIDTH-self.rect.w)
        self.rect.y = uniform(-50, 0)
        self.sprite_data.x_step = uniform(1, 2)
        self.sprite_data.y_step = uniform(1, 2)

        self.sprite_data.x_direction = randint(0, 1)

    def update(self):
        if self.rect.x > WINDOW_WIDTH + self.rect.w  \
                or self.rect.x < -self.rect.w  \
                or self.rect.y >= WINDOW_HEIGHT + self.rect.h:
            self.sprite_data.out_of_bounds = True
            return

        if self.sprite_data.x_direction == 0:
            self.go_right()
        else:
            self.go_left()

        self.go_down()
        self.load_next_image()

    def go_left(self):
        self.rect.x -= self.sprite_data.x_step

    def go_right(self):
        self.rect.x += self.sprite_data.x_step

    def go_up(self):
        self.rect.y -= self.sprite_data.y_step

    def go_down(self):
        self.rect.y += self.sprite_data.y_step


class AsteroidAlpha(object):

    asteroid = None

    def __init__(self):
        super(AsteroidAlpha, self).__init__()

        asteroid_data = AnimatedSpriteData(
            image_set_folder=os.path.join(sys.path[0],
                                          'resources/asteroids/a_1'),
            loop_forever=True
        )
        self.asteroid = Asteroid(asteroid_data)
