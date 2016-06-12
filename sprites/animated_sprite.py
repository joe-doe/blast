import pygame
from constants import *
from sprite import Sprite
from os import listdir
from os.path import isfile, join


class AnimatedSprite(Sprite):

    image_set = []
    image_set_folder = None
    current_image_idx = 1
    should_explode = False

    def __init__(self):
        super(AnimatedSprite, self).__init__()

        self.set_image_set_folder()
        self.setup()

    def set_image_set_folder(self):
        pass

    def setup(self):
        path = self.image_set_folder+'/01.png'
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()

        self.load_image_set()

    def start(self):
        pass

    def load_image_set(self):
        image_files = [f for f in listdir(self.image_set_folder) if isfile(join(self.image_set_folder, f))]
        image_files.sort()
        for img in image_files:
            image = join(self.image_set_folder, img)
            self.image_set.append(pygame.image.load(image).convert_alpha())

    def load_next_image(self ):
        try:
            self.current_image_idx += 1
            self.image = self.image_set[self.current_image_idx]
        except IndexError:
            self.current_image_idx = 0

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

