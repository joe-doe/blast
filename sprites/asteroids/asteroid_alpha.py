import sys
import os
from random import (
    randint,
    uniform
)
from constants import *
from ..animated_sprite import AnimatedSprite


class AsteroidAlpha(AnimatedSprite):

    def __init__(self):
        super(AsteroidAlpha, self).__init__()

        self.auto_start()

    def set_image_set_folder(self):
        self.image_set_folder = os.path.join(sys.path[0],
                                             'resources/asteroids/a_1')

    def auto_start(self):
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
        self.load_next_image()

    def go_left(self):
        self.rect.x -= self.x_step

    def go_right(self):
        self.rect.x += self.x_step

    def go_up(self):
        self.rect.y -= self.y_step

    def go_down(self):
        self.rect.y += self.y_step

    def explode(self):
        print "BOOM"
