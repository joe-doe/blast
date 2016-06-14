import os
import sys
from sprites.animated_sprite import AnimatedSprite


class ExplosionOne(AnimatedSprite):

    def __init__(self, pos):
        super(ExplosionOne, self).__init__(False)

        self.rect.centerx, self.rect.centery = pos.centerx, pos.centery

    def set_image_set_folder(self):
        self.image_set_folder = os.path.join(sys.path[0],
                                             'resources/explosions/a_1')

    def update(self):
        self.load_next_image()

