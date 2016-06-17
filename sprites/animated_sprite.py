from constants import *
from sprite import Sprite


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



