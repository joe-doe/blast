from sprites.sprite import Sprite
from sprites.sprite_data import SpriteData
from constants import *


class LabelSprite(Sprite):

    def __init__(self):
        super(LabelSprite, self).__init__()


class ShieldsOnLabel(LabelSprite):
    def initialize_sprite(self):
        super(ShieldsOnLabel, self).initialize_sprite()

        self.rect.x = WINDOW_WIDTH/2 - self.rect.w/2
        self.rect.y = WINDOW_HEIGHT/2 - self.rect.h/2

    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/labels/shields_on.png'
        )


class ShieldsOffLabel(LabelSprite):
    def initialize_sprite(self):
        super(ShieldsOffLabel, self).initialize_sprite()

        self.rect.x = WINDOW_WIDTH/2 - self.rect.w/2
        self.rect.y = WINDOW_HEIGHT/2 - self.rect.h/2

    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/labels/shields_off.png'
        )


class LevelCompleted(LabelSprite):
    def initialize_sprite(self):
        super(LevelCompleted, self).initialize_sprite()

        self.rect.x = WINDOW_WIDTH/2 - self.rect.w/2
        self.rect.y = WINDOW_HEIGHT/2 - self.rect.h/2

    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/labels/level_completed.png'
        )


class LevelLabel(LabelSprite):

    level_number = 1

    def __init__(self, level_number):
        super(LevelLabel, self).__init__()
        self.level_number = level_number

    def initialize_sprite(self):
        super(LevelLabel, self).initialize_sprite()

        self.rect.x = WINDOW_WIDTH/2 - self.rect.w/2
        self.rect.y = WINDOW_HEIGHT/2 - self.rect.h/2

    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/labels/level_0{}.png'.format(
                self.level_number
            )
        )


class WeaponUpgradeLabel(LabelSprite):
    def initialize_sprite(self):
        super(WeaponUpgradeLabel, self).initialize_sprite()

        self.rect.x = WINDOW_WIDTH/2 - self.rect.w/2
        self.rect.y = WINDOW_HEIGHT/2 - self.rect.h/2

    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/labels/weapon_upgrade.png'
        )

