from constants import *
from sprite import Sprite
import time


class AnimatedSprite(Sprite):

    current_image_idx = 0

    def __init__(self, animated_sprite_data):
        super(AnimatedSprite, self).__init__(animated_sprite_data)

    def update(self):
        super(AnimatedSprite, self).update()
        self.load_next_image()

    def load_next_image(self):
        try:
            self.image = self.sprite_data.image_set[self.current_image_idx]
        except IndexError:
            self.kill()

        if self.sprite_data.loop_forever:
            if self.current_image_idx == self.sprite_data.image_set_length - 1:
                self.current_image_idx = 0
            else:
                self.current_image_idx += 1
        else:
            self.current_image_idx += 1

    def bounce(self):
        if self.rect.x <= 0:
            self.sprite_data.x_step = -self.sprite_data.x_step

        if self.rect.x >= WINDOW_WIDTH - self.rect.w:
            self.sprite_data.x_step = -self.sprite_data.x_step

        self.rect.x += self.sprite_data.x_step

        if self.rect.y <= 0:
            self.sprite_data.y_step = -self.sprite_data.y_step

        if self.rect.y >= WINDOW_HEIGHT - self.rect.h:
            self.sprite_data.y_step = -self.sprite_data.y_step
        self.rect.y += self.sprite_data.y_step


class AnimatedControlledSprite(Sprite):

    current_image_idx = 0

    def __init__(self, animated_controlled_sprite_data):
        super(AnimatedControlledSprite, self).\
            __init__(animated_controlled_sprite_data)

    def update(self):
        super(AnimatedControlledSprite, self).update()

    def go_left(self, speed=0):
        super(AnimatedControlledSprite, self).go_left()

        try:
            self.current_image_idx -= 1
            if self.current_image_idx < 0:
                raise IndexError
            self.image = self.sprite_data.image_set[self.current_image_idx]
        except IndexError:
            self.current_image_idx += 1

    def go_right(self, speed=0):
        super(AnimatedControlledSprite, self).go_right()

        try:
            self.current_image_idx += 1
            self.image = self.sprite_data.image_set[self.current_image_idx]
        except IndexError:
            self.current_image_idx -= 1

    def get_straight(self, from_left):
        if from_left:
            while self.current_image_idx != 3:
                self.go_right()
        else:
            while self.current_image_idx != 3:
                self.go_left()
