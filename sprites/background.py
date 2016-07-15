from sprite import Sprite
from sprite_data import SpriteData
from constants import WINDOW_HEIGHT


class Background(Sprite):

    def __init__(self):
        super(Background, self).__init__()

    def initialize_sprite(self):
        super(Background, self).initialize_sprite()

        self.rect.x = 0
        self.rect.y = WINDOW_HEIGHT - self.rect.h

    def update(self):
        super(Background, self).update()

        self.rect.y += self.sprite_data.y_step
        self.rect.x += self.sprite_data.x_step


class BackgroundOne(Background):
    def __init__(self):
        super(BackgroundOne, self).__init__()

    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/L1_background_800x600.png',
            y_step=1
        )


class BackgroundTwo(Background):
    def __init__(self):
        super(BackgroundTwo, self).__init__()

    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/L2_background_800x600.png',
            y_step=1
        )
