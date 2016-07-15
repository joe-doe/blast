from sprite import Sprite
from sprite_data import SpriteData
from constants import *


class Logo(Sprite):
    sprite_data = None

    def __init__(self, ):
        super(Logo, self).__init__()

    def initialize_sprite(self):
        super(Logo, self).initialize_sprite()

        self.rect.x = (WINDOW_WIDTH/2) - (self.rect.w/2)
        self.rect.y = 100


class IntroLogo(Logo):

    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/logo.png'
        )
