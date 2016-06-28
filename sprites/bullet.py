from sprite import Sprite
from sprites.sprite_data import SpriteData


class Bullet(Sprite):

    def __init__(self, bullet_data):
        super(Bullet, self).__init__(bullet_data)

    def initialize_sprite(self):
        self.rect.x = self.sprite_data.pos_relative_to.centerx
        self.rect.y = self.sprite_data.pos_relative_to.centery

    def update(self):
        super(Bullet, self).update()

        self.rect.y += self.sprite_data.y_step
        self.rect.x += self.sprite_data.x_step


class BulletOne(object):
    bullet = None

    def __init__(self, igniter):
        super(BulletOne, self).__init__()

        bullet_one_data = SpriteData(
            image_path='resources/spaceship/bullet.png',
            x_step=0,
            y_step=-8,
            pos_relative_to=igniter.rect
        )
        self.bullet = Bullet(bullet_one_data)
