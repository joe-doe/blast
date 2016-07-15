from sprites.animated_sprite import AnimatedSprite
from sprites.sprite_data import AnimatedSpriteData

import os
import sys


class Explosion(AnimatedSprite):

    collided_item = None

    def __init__(self, collided_item):
        self.collided_item = collided_item
        super(Explosion, self).__init__()

    def initialize_sprite(self):
        super(Explosion, self).initialize_sprite()

        self.rect.centerx = self.sprite_data.pos_relative_to.centerx
        self.rect.centery = self.sprite_data.pos_relative_to.centery

    def update(self):
        super(Explosion, self).update()

        self.rect.y += self.sprite_data.y_step
        self.rect.x += self.sprite_data.x_step


class ExplosionOne(Explosion):

    def feed_data(self):

        self.sprite_data = AnimatedSpriteData(
                    image_set_folder=os.path.join(sys.path[0],
                                                  'resources/explosions/a_1'),
                    pos_relative_to=self.collided_item.rect
                )
