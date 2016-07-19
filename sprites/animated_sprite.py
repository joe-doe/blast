from sprite import Sprite
from threading import Lock


class AnimatedSprite(Sprite):
    """
    subclasses should implement feed_data
    """
    current_image_idx = 0
    next_image_lock = None

    def __init__(self):
        super(AnimatedSprite, self).__init__()
        self.next_image_lock = Lock()

    def update(self):
        super(AnimatedSprite, self).update()
        self.load_next_image()

    def load_next_image(self):
        if not self.next_image_lock.acquire(False):
            return
        else:
            try:
                self.image = self.sprite_data.get_image_from_set(
                    self.current_image_idx
                )

                if self.sprite_data.loop_forever:
                    if self.current_image_idx == self.sprite_data.image_set_length - 1:
                        self.current_image_idx = 0
                    else:
                        self.current_image_idx += 1
                else:
                    self.current_image_idx += 1
            except IndexError:
                self.kill()
            finally:
                self.next_image_lock.release()


class AnimatedControlledSprite(Sprite):
    """
    subclasses should implement feed_data
    """
    current_image_idx = 0

    def __init__(self):
        super(AnimatedControlledSprite, self).__init__()
        self.current_image_idx = self.sprite_data.get_starting_image_idx()
        self.image = self.sprite_data.get_image_from_set(
            self.current_image_idx
        )

    def update(self):
        super(AnimatedControlledSprite, self).update()

    def go_left(self, speed=0):
        super(AnimatedControlledSprite, self).go_left()

        try:
            self.current_image_idx -= 1
            if self.current_image_idx < 0:
                raise IndexError
            self.image = self.sprite_data.get_image_from_set(
                self.current_image_idx
            )
        except IndexError:
            self.current_image_idx += 1

    def go_right(self, speed=0):
        super(AnimatedControlledSprite, self).go_right()

        try:
            self.current_image_idx += 1
            self.image = self.sprite_data.get_image_from_set(
                self.current_image_idx
            )
        except IndexError:
            self.current_image_idx -= 1

    def get_straight(self, from_left):

        if from_left:
            while self.current_image_idx != 3:
                self.go_right()
        else:
            while self.current_image_idx != 3:
                    self.go_left()
