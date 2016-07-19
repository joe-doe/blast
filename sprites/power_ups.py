import os
import sys
from random import uniform
from sprites.animated_sprite import AnimatedSprite
from sprites.sprite_data import AnimatedSpriteData
from constants import *


class PowerUp(AnimatedSprite):

    def __init__(self):
        super(PowerUp, self).__init__()

    def enable_powerup(self, *args, **kwargs):
        pass

    def initialize_sprite(self):
        super(PowerUp, self).initialize_sprite()

        self.rect.x = uniform(0, WINDOW_WIDTH-self.rect.w)
        self.rect.y = -self.rect.h

    def update(self):
        super(PowerUp, self).update()

        self.rect.y += self.sprite_data.y_step
        self.rect.x += self.sprite_data.x_step


class UpgradeBattleshipWeapon(PowerUp):

    def feed_data(self):

        self.sprite_data = AnimatedSpriteData(
            image_set_folder=os.path.join(
                sys.path[0],
                'resources/powerups/Blue/'),
            loop_forever=True,
            y_step=2
        )

    def enable_powerup(self, battleship):
        battleship.upgrade_weapon()


class ShieldsOn(PowerUp):

    def feed_data(self):

        self.sprite_data = AnimatedSpriteData(
            image_set_folder=os.path.join(
                sys.path[0],
                'resources/powerups/Green/'),
            loop_forever=True,
            y_step=2
        )

    def enable_powerup(self, battleship):
        battleship.set_shields_on()
