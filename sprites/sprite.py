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

    def bounce_x(self):
        if self.rect.x <= 0:
            self.sprite_data.x_step = -self.sprite_data.x_step

        if self.rect.x >= WINDOW_WIDTH - self.rect.w:
            self.sprite_data.x_step = -self.sprite_data.x_step

        self.rect.x += self.sprite_data.x_step

    def bounce_y(self):
        if self.rect.y <= 0:
            self.sprite_data.y_step = -self.sprite_data.y_step

        if self.rect.y >= WINDOW_HEIGHT - self.rect.h:
            self.sprite_data.y_step = -self.sprite_data.y_step
        self.rect.y += self.sprite_data.y_step

    def update(self):
        if self.rect.x <= - self.rect.w - 1\
                or self.rect.x >= WINDOW_WIDTH + 1 \
                or self.rect.y <= - self.rect.h - 1\
                or self.rect.y >= WINDOW_HEIGHT + self.rect.h + 1:
            self.sprite_data.out_of_bounds = True
