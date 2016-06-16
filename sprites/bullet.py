from sprite import Sprite


class Bullet(Sprite):

    def __init__(self, bullet_data):
        super(Bullet, self).__init__(bullet_data)

    def initialize_sprite(self):
        self.rect.x = self.sprite_data.pos_relative_to.x
        self.rect.y = self.sprite_data.pos_relative_to.y

    def update(self):
        if self.rect.y <= - self.rect.h:
            self.sprite_data.out_of_bounds = True
        self.rect.y -= self.sprite_data.y_step
