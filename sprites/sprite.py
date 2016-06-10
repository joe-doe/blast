import pygame


class Sprite(pygame.sprite.Sprite):
    image = None
    rect = None
    should_die = False
    x_step = 0
    y_step = 0
    x_direction = None

    def __init__(self):
        super(Sprite, self).__init__()

    def go_left(self):
        pass

    def go_right(self):
        pass

    def go_up(self):
        pass

    def go_down(self):
        pass

    def explode(self):
        pass
