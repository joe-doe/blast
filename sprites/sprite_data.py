from os import listdir
from os.path import isfile, join
import pygame
from threading import Lock


class SpriteData(object):

    image_path = None
    x_start = None
    x_step = None
    y_start = None
    y_step = None
    direction = None
    out_of_bounds = None
    pos_relative_to = None
    should_fire = None
    health = None
    weapon = None

    def __init__(self,
                 image_path=None,
                 x_start=0,
                 x_step=0,
                 y_start=0,
                 y_step=0,
                 direction=1,
                 out_of_bounds=False,
                 pos_relative_to=None,
                 should_fire=False,
                 health=1,
                 weapon=None):
        super(SpriteData, self).__init__()

        self.image_path = image_path
        self.x_start = x_start
        self.x_step = x_step
        self.y_start = y_start
        self.y_step = y_step
        self.direction = direction
        self.out_of_bounds = out_of_bounds
        self.pos_relative_to = pos_relative_to
        self.should_fire = should_fire
        self.health = health
        self.weapon = weapon

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
    starting_image_idx = 0

    reload_lock = None

    def __init__(self,
                 image_set_folder=None,
                 loop_forever=False,
                 x_start=0,
                 x_step=0,
                 y_start=0,
                 y_step=0,
                 direction=1,
                 out_of_bounds=False,
                 pos_relative_to=None,
                 should_fire=False,
                 health=1,
                 weapon=None,
                 starting_image='01'):
        super(AnimatedSpriteData, self).__init__(
            image_path=None,
            x_start=x_start,
            x_step=x_step,
            y_step=y_step,
            y_start=y_start,
            direction=direction,
            out_of_bounds=out_of_bounds,
            pos_relative_to=pos_relative_to,
            should_fire=should_fire,
            health=health,
            weapon=weapon
        )

        self.get_image_lock = Lock()
        self.reload_lock = Lock()

        self.reload_image_set(image_set_folder, starting_image, loop_forever)

    def load_image_set(self):
        image_set = []
        image_files = [f for f in listdir(self.image_set_folder)
                       if isfile(join(self.image_set_folder, f))]
        image_files.sort()

        for img in image_files:
            image = join(self.image_set_folder, img)
            image_set.append(pygame.image.load(image).convert_alpha())

        return image_set

    def get_image_from_set(self, idx):
        with self.get_image_lock:
            return self.image_set[idx]

    def get_starting_image_idx(self):
        return self.starting_image_idx

    def reload_image_set(self, image_set_folder, starting_image, loop_forever):
        with self.reload_lock:
            self.starting_image_idx = int(starting_image)
            self.image_set_folder = image_set_folder
            self.image_path = self.image_set_folder\
                + '/'\
                + str(starting_image)\
                + '.png'
            self.image_set = self.load_image_set()
            self.image_set_length = len(self.image_set)
            self.loop_forever = loop_forever
