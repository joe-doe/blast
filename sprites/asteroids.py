
from constants import *
from sprite import Sprite


class Asteroids(Sprite):

    def __init__(self):
        super(Asteroids, self).__init__()

        self.setup()
        self.start()

    def setup(self):
        pass

    def start(self):
        pass

    def resurrect(self):
        self.start()

    def bounce(self):
        if self.rect.x <= 0:
            self.x_step = -self.x_step

        if self.rect.x >= WINDOW_WIDTH - self.rect.w:
            self.x_step = -self.x_step

        self.rect.x += self.x_step

        if self.rect.y <= 0:
            self.y_step = -self.y_step

        if self.rect.y >= WINDOW_HEIGHT - self.rect.h:
            self.y_step = -self.y_step
        self.rect.y += self.y_step

