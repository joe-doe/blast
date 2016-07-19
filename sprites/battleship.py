from constants import *
from daemon_thread import DaemonThread
from sprites.animated_sprite import AnimatedControlledSprite
from sprites.sprite_data import AnimatedSpriteData
from sprites.bullet import (
    BattleshipWeaponOne,
    BattleshipWeaponTwo
)
from label import (
    ShieldsOnLabel,
    ShieldsOffLabel
)

import os
import sys
import time


class Battleship(AnimatedControlledSprite):

    friend_bullets = None
    weapons = None
    weapon = None
    weapon_selector = None
    shields_on = False

    def __init__(self, friend_bullets):
        super(Battleship, self).__init__()

        self.weapons = self.sprite_data.weapon
        self.weapon_selector = self.get_next_weapon()
        self.weapon = self.weapon_selector.next()
        self.friend_bullets = friend_bullets

    def initialize_sprite(self):
        super(Battleship, self).initialize_sprite()

        self.rect.x = WINDOW_WIDTH/2 - self.rect.w/2
        self.rect.y = WINDOW_HEIGHT - self.rect.h*3

    def fire(self):
        self.friend_bullets.add(self.weapon.get_bullets(self))

    def update(self):
        # we do not want battleship out of bounds
        # if self.rect.y >= WINDOW_HEIGHT-self.rect.h:
        #     self.sprite_data.y_step = 0
        pass

    # weapons behavior
    def upgrade_weapon(self):
        try:
            self.weapon = self.weapon_selector.next()
        except StopIteration:
            pass  # you already have the biggest gun

    def get_next_weapon(self):
        for weapon in self.weapons:
            yield weapon

    # shields behavior
    def set_shields_on(self, non_interactive_sprites):
        DaemonThread(
            target=self.shields_on,
            args=(non_interactive_sprites, )
        ).start()

    def shields_on(self, non_interactive_sprites):

        # set shields on flag true
        self.shields_on = True

        # update image set
        path = os.path.join(
                sys.path[0],
                'resources/spaceship/spaceship_shielded'
            )
        starting_image = '04'
        loop_forever = True

        self.sprite_data.reload_image_set(path, starting_image, loop_forever)
        self.reload_current_image(self.sprite_data.image_path)

        # show information label
        label = ShieldsOnLabel()
        non_interactive_sprites.add(label)
        time.sleep(1)
        non_interactive_sprites.remove(label)

        time.sleep(6)

        # show information label
        # and wait for 1 sec
        label = ShieldsOffLabel()
        non_interactive_sprites.add(label)
        time.sleep(1)
        non_interactive_sprites.remove(label)

        # update image set
        path = os.path.join(
            sys.path[0],
            'resources/spaceship/spaceship'
        )
        starting_image = '04'
        loop_forever = True

        self.sprite_data.reload_image_set(path, starting_image, loop_forever)
        self.reload_current_image(self.sprite_data.image_path)

        # set shields on flag false
        self.shields_on = False


class BattleshipOne(Battleship):

    def feed_data(self):
        self.sprite_data = AnimatedSpriteData(
            image_set_folder=os.path.join(
                sys.path[0],
                'resources/spaceship/spaceship'
            ),
            x_step=6,
            y_step=6,
            starting_image='03',
            weapon=[BattleshipWeaponOne(), BattleshipWeaponTwo()]
        )
