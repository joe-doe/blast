from sprite import Sprite
from constants import WINDOW_HEIGHT


class Background(Sprite):

    def __init__(self, background_data):
        super(Background, self).__init__(background_data)

    def initialize_sprite(self):
        self.rect.x = 0
        self.rect.y = WINDOW_HEIGHT - self.rect.h

    def update(self):
        super(Background, self).update()

        self.rect.y += self.sprite_data.y_step
        self.rect.x += self.sprite_data.x_step
