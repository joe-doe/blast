from sprite import Sprite
from sprites.sprite_data import SpriteData


class Bullet(Sprite):
    igniter = None

    def __init__(self, igniter):
        self.igniter = igniter
        super(Bullet, self).__init__()

    def initialize_sprite(self):
        super(Bullet, self).initialize_sprite()

        self.rect.centerx = self.igniter.rect.centerx
        self.rect.centery = self.igniter.rect.centery - self.rect.h/2 - 20

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
            image_path='resources/enemies/enemy_bullet.png',
            x_step=0,
            y_step=8,
            pos_relative_to=self.igniter.rect
        )


class EnemyBulletTwo(Bullet):

    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/enemies/enemy_bullet_big.png',
            x_step=0,
            y_step=8,
            pos_relative_to=self.igniter.rect
        )


# weapons
class BattleshipWeaponOne(object):

    def get_bullets(self, igniter):

        bullet_one = BulletOne(igniter)

        return bullet_one


class BattleshipWeaponTwo(object):

    def get_bullets(self, igniter):
        bullets = []

        bullet_one = BulletOne(igniter)
        bullet_one.rect.x += 10
        bullets.append(bullet_one)

        bullet_two = BulletOne(igniter)
        bullet_two.rect.x -= 10
        bullets.append(bullet_two)

        return bullets


class EnemyWeaponOne(object):

    def get_bullets(self, igniter):

        enemy_bullet_one = EnemyBulletOne(igniter)
        return enemy_bullet_one


class EnemyWeaponTwo(object):

    def get_bullets(self, igniter):

        enemy_bullet_two = EnemyBulletTwo(igniter)
        return enemy_bullet_two