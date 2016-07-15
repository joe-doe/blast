import sys
import os
import time
from random import (
    randint,
    uniform
)
from constants import *
from sprites.animated_sprite import AnimatedSprite
from sprites.sprite_data import AnimatedSpriteData


class Asteroid(AnimatedSprite):
    """
    subclasses should implement feed_data
    """
    def __init__(self):
        super(Asteroid, self).__init__()

    def initialize_sprite(self):
        super(Asteroid, self).initialize_sprite()

        self.rect.x = uniform(0, WINDOW_WIDTH-self.rect.w)
        self.rect.y = uniform(-50, 0)
        self.sprite_data.x_step = uniform(-2, 2)
        self.sprite_data.y_step = uniform(1, 5)

        self.sprite_data.x_direction = randint(0, 1)

    def update(self):
        super(Asteroid, self).update()

        self.rect.y += self.sprite_data.y_step
        self.rect.x += self.sprite_data.x_step


class AsteroidAlpha(Asteroid):

    def feed_data(self):
        self.sprite_data = AnimatedSpriteData(
            image_set_folder=os.path.join(sys.path[0],
                                          'resources/asteroids/a_1'),
            loop_forever=True,
            y_step=2
        )


class AsteroidBelt(object):
    how_many = 0
    asteroid_set = None
    asteroid_data = None

    def __init__(self, how_many):
        super(AsteroidBelt, self).__init__()
        self.asteroid_set = []
        self.how_many = how_many
        self.initialize_set()

    def initialize_set(self):
        pass

    def get_asteroid_set(self):
        for asteroid in self.asteroid_set:
            time.sleep(0.5)
            yield asteroid


class AsteroidBeltOne(AsteroidBelt):
        def __init__(self, how_many=3):
            super(AsteroidBeltOne, self).__init__(how_many)

        def initialize_set(self):
            for i in range(self.how_many):
                self.asteroid_set.append(AsteroidAlpha())
