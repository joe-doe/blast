import pygame
from constants import WINDOW_WIDTH, WINDOW_HEIGHT


class Sprite(pygame.sprite.Sprite):
    image = None
    rect = None
    sprite_data = None

    def __init__(self, sprite_data):
        super(Sprite, self).__init__()

        self.image = pygame.image.load(sprite_data.image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.sprite_data = sprite_data

        self.initialize_sprite()

    def initialize_sprite(self):
        self.rect.x = self.sprite_data.x_start
        self.rect.y = self.sprite_data.y_start

    def go_left(self, speed=0):
        if speed:
            self.rect.x -= speed
        else:
            self.rect.x -= self.sprite_data.x_step

    def go_right(self, speed=0):
        if speed:
            self.rect.x += speed
        else:
            self.rect.x += self.sprite_data.x_step

    def go_up(self, speed=0):
        if speed:
            self.rect.y -= speed
        else:
            self.rect.y -= self.sprite_data.y_step

    def go_down(self, speed=0):
        if speed:
            self.rect.y += speed
        else:
            self.rect.y += self.sprite_data.y_step

    def update(self):
        if self.rect.x <= - self.rect.w \
                or self.rect.x >= WINDOW_WIDTH \
                or self.rect.y <= - self.rect.h \
                or self.rect.y >= WINDOW_HEIGHT + self.rect.h:
            self.sprite_data.out_of_bounds = True
