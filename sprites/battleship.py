from constants import *
from sprites.animated_sprite import AnimatedControlledSprite
from sprites.sprite_data import AnimatedSpriteData
from sprites.bullet import BulletOne
import os
import sys


class Battleship(AnimatedControlledSprite):

    friend_bullets = None
    weapon = None

    def __init__(self, battleship_data, friend_bullets):
        super(Battleship, self).__init__(battleship_data)

        self.friend_bullets = friend_bullets
        self.weapon = BulletOne(self)

    def initialize_sprite(self):
        self.rect.x = WINDOW_WIDTH/2 - self.rect.w/2
        self.rect.y = WINDOW_HEIGHT - self.rect.h*3

    def fire(self):
        self.friend_bullets.add(self.weapon.get_bullet())

    def set_weapon(self, new_weapon):
        self.weapon = new_weapon

    def update(self):
        # we do not want battleship out of bounds
        # if self.rect.y >= WINDOW_HEIGHT-self.rect.h:
        #     self.sprite_data.y_step = 0
        pass


class BattleshipOne(object):
    battleship = None

    def __init__(self, friend_bullets):
        super(BattleshipOne, self).__init__()

        battleship_data = AnimatedSpriteData(
            image_set_folder=os.path.join(
                sys.path[0],
                'resources/spaceship/spaceship'
            ),
            x_step=6,
            y_step=6,
            starting_image='/04.png'
        )

        self.battleship = Battleship(battleship_data, friend_bullets)
