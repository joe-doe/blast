from sprite import Sprite
from sprites.sprite_data import SpriteData


class Bullet(Sprite):
    igniter = None

    def __init__(self, igniter):
        self.igiter = igniter
        super(Bullet, self).__init__()

    def update(self):
        super(Bullet, self).update()

        self.rect.y += self.sprite_data.y_step
        self.rect.x += self.sprite_data.x_step


class BulletOne(Bullet):

    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/spaceship/bullet.png',
            x_step=0,
            y_step=-8,
            pos_relative_to=self.igniter.rect
        )


class EnemyBulletOne(Bullet):

    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/spaceship/enemy_bullet.png',
            x_step=0,
            y_step=8,
            pos_relative_to=self.igniter.rect
        )


# weapons
class BattleshipWeaponOne(object):
    bullets = None
    igniter = None

    def __init__(self, igniter):
        super(BattleshipWeaponOne, self).__init__()

        self.igniter = igniter
        self.bullets = []

        bullet_one = BulletOne(igniter)
        bullet_one.sprite_data.rect.x += 5
        self.bullets.append(bullet_one)

    def get_bullets(self):
        return self.bullets


class BattleshipWeaponTwo(object):
    bullets = None

    def __init__(self, igniter):
        super(BattleshipWeaponTwo, self).__init__()
        self.igniter = igniter
        self.bullets = []

        bullet_one = BulletOne(igniter)
        bullet_one.sprite_data.rect.x += 5
        self.bullets.append(bullet_one)

        bullet_two = BulletOne(igniter)
        bullet_two.sprite_data.rect.x += 5
        self.bullets.append(bullet_two)

    def get_bullets(self):
        return self.bullets