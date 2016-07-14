from sprite import Sprite
from sprite_data import SpriteData
from constants import *


class Logo(Sprite):
    sprite_data = None

    def __init__(self, sprite_data):
        super(Logo, self).__init__(sprite_data)
        self.sprite_data = sprite_data

    def initialize_sprite(self):
        self.rect.x = (WINDOW_WIDTH/2) - (self.rect.w/2)
        self.rect.y = 100


class IntroLogo(object):

    logo_data = None
    logo = None

    def __init__(self):
        super(IntroLogo, self).__init__()

        self.logo_data = SpriteData(
            image_path='resources/logo.png'
        )

        self.logo = Logo(self.logo_data)