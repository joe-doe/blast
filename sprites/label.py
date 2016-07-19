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
