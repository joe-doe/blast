from os import listdir
from os.path import isfile, join
import pygame


class SpriteData(object):

    image_path = None
    x_step = None
    y_step = None
    direction = None
    out_of_bounds = None
    pos_relative_to = None

    def __init__(self,
                 image_path=None,
                 x_step=0,
                 y_step=0,
                 direction=1,
                 out_of_bounds=False,
                 pos_relative_to=None):
        super(SpriteData, self).__init__()

        self.image_path = image_path
        self.x_step = x_step
        self.y_step = y_step
        self.direction = direction
        self.out_of_bounds = out_of_bounds
        self.pos_relative_to = pos_relative_to

    def set_image_path(self, image_path):
        self.image_path = image_path

    def set_x_step(self, x_step):
        self.x_step = x_step

    def set_y_step(self, y_step):
        self.y_step = y_step

    def set_direction(self, direction):
        self.direction = direction

    def set_out_of_bounds(self, out_of_bounds):
        self.out_of_bounds = out_of_bounds


class AnimatedSpriteData(SpriteData):

    image_set = None
    image_set_length = 0
    image_set_folder = None
    loop_forever = False

    def __init__(self,
                 image_set_folder=None,
                 loop_forever=False,
                 x_step=0,
                 y_step=0,
                 direction=1,
                 out_of_bounds=False,
                 pos_relative_to=None):
        super(AnimatedSpriteData, self).__init__(
            image_path=None,
            x_step=x_step,
            y_step=y_step,
            direction=direction,
            out_of_bounds=out_of_bounds,
            pos_relative_to=pos_relative_to
        )

        self.image_set_folder = image_set_folder
        self.image_path = self.image_set_folder+'/01.png'
        self.image_set = self.load_image_set()
        self.image_set_length = len(self.image_set)
        self.loop_forever = loop_forever

    def load_image_set(self):
        image_set = []
        image_files = [f for f in listdir(self.image_set_folder)
                       if isfile(join(self.image_set_folder, f))]
        image_files.sort()

        for img in image_files:
            image = join(self.image_set_folder, img)
            image_set.append(pygame.image.load(image).convert_alpha())
        return image_set

    def set_image_set(self, image_set):
        self.image_set = image_set
        self.image_set_length = len(image_set)

    def set_image_set_folder(self, image_set_folder):
        self.image_set_folder = image_set_folder

    def set_loop_forever(self, loop_forever):
        self.loop_forever = loop_forever
