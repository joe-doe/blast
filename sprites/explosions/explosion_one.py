from sprites.animated_sprite import AnimatedSprite
from sprites.sprite_data import AnimatedSpriteData

import os
import sys


class Explosion(AnimatedSprite):

    def __init__(self, explosion_data):
        super(Explosion, self).__init__(explosion_data)

    def initialize_sprite(self):
        self.rect.centerx = self.sprite_data.pos_relative_to.centerx
        self.rect.centery = self.sprite_data.pos_relative_to.centery

    def update(self):
        self.load_next_image()


class ExplosionOne(object):
    explosion = None

    def __init__(self, collided_item):
        super(ExplosionOne, self).__init__()

        explosion_one_data = AnimatedSpriteData(
                    image_set_folder=os.path.join(sys.path[0],
                                                  'resources/explosions/a_1'),
                    pos_relative_to=collided_item.rect
                )
        self.explosion = Explosion(explosion_one_data)
