from sprite import Sprite
from sprites.sprite_data import SpriteData


class Bullet(Sprite):
    def __init__(self, bullet_data):
        super(Bullet, self).__init__(bullet_data)

    def initialize_sprite(self):
        pass

    def update(self):
        super(Bullet, self).update()

        self.rect.y += self.sprite_data.y_step
        self.rect.x += self.sprite_data.x_step


class BulletOne(object):
    bullet_one_data = None

    def __init__(self, igniter):
        super(BulletOne, self).__init__()

        self.bullet_one_data = SpriteData(
            image_path='resources/spaceship/bullet.png',
            x_step=0,
            y_step=-8,
            pos_relative_to=igniter.rect
        )

    def get_bullet(self):
        bullet = Bullet(self.bullet_one_data)
        bullet.rect.x = bullet.sprite_data.pos_relative_to.centerx - (bullet.rect.w / 2)
        bullet.rect.y = bullet.sprite_data.pos_relative_to.centery - bullet.rect.h - 5
        return bullet


class BulletTwo(object):
    bullet_two_data = None

    def __init__(self, igniter):
        super(BulletTwo, self).__init__()

        self.bullet_two_data = SpriteData(
            image_path='resources/spaceship/bullet.png',
            x_step=0,
            y_step=-8,
            pos_relative_to=igniter.rect
        )

    def get_bullet(self):
        bullets = []

        new_bullet = Bullet(self.bullet_two_data)
        new_bullet.rect.x = new_bullet.sprite_data.pos_relative_to.centerx + 5
        new_bullet.rect.y = new_bullet.sprite_data.pos_relative_to.centery - new_bullet.rect.h
        bullets.append(new_bullet)

        new_bullet = Bullet(self.bullet_two_data)
        new_bullet.rect.x = new_bullet.sprite_data.pos_relative_to.centerx - new_bullet.rect.w -5
        new_bullet.rect.y = new_bullet.sprite_data.pos_relative_to.centery - new_bullet.rect.h
        bullets.append(new_bullet)

        return bullets
