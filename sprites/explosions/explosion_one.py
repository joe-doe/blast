import os
import sys
from ..animated_sprite import AnimatedSprite


class ExplosionOne(AnimatedSprite):

    def __init__(self):
        super(ExplosionOne, self).__init__()

        self.auto_start()

    def set_image_set_folder(self):
        self.image_set_folder = os.path.join(sys.path[0],
                                             'resources/explosions/a_1')

    def auto_start(self):
        self.rect.x = 1
        self.rect.y = 2
        self.x_step = 3
        self.y_step = 4

        self.x_direction = 0
