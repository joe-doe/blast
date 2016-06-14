import pygame
from constants import *
from sprite import Sprite
from os import listdir
from os.path import isfile, join


class AnimatedSprite(Sprite):

    image_set = None
    image_set_length = 0
    image_set_folder = None
    loop_forever = False
    current_image_idx = 0

    def __init__(self, loop_forever):
        super(AnimatedSprite, self).__init__()

        self.loop_forever = loop_forever
        self.image_set = []
        self.setup()

    def set_image_set_folder(self):
        pass

    def start(self):
        pass

    def setup(self):
        self.set_image_set_folder()

        path = self.image_set_folder+'/01.png'
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.load_image_set()

        self.start()

    def load_image_set(self):
        image_files = [f for f in listdir(self.image_set_folder)
                       if isfile(join(self.image_set_folder, f))]
        image_files.sort()
        self.image_set_length = len(image_files)
        for img in image_files:
            image = join(self.image_set_folder, img)
            self.image_set.append(pygame.image.load(image).convert_alpha())

    def load_next_image(self):
        try:
            self.image = self.image_set[self.current_image_idx]
        except IndexError:
            self.kill()

        if self.loop_forever:
            if self.current_image_idx == self.image_set_length - 1:
                self.current_image_idx = 0
            else:
                self.current_image_idx += 1
        else:
            self.current_image_idx += 1

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

