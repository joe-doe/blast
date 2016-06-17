from constants import *
from sprites.sprite import Sprite
from sprites.sprite_data import SpriteData

from random import (
    randint,
    uniform
)


class Enemy(Sprite):

    def __init__(self, enemy_data):
        super(Enemy, self).__init__(enemy_data)

    def initialize_sprite(self):
        self.rect.x = uniform(0, WINDOW_WIDTH-self.rect.w)
        self.rect.y = uniform(-50, 0)
        self.sprite_data.x_step = 0
        self.sprite_data.y_step = 1

    def update(self):
        self.rect.y += self.sprite_data.y_step
        self.rect.x += self.sprite_data.x_step
        # print "x_step: {}".format(self.sprite_data.x_step)
        # print "y_step: {}".format(self.sprite_data.y_step)

    def fire(self):
        bullet_data = SpriteData(
            image_path='resources/spaceship/bullet.png',
            x_step=0,
            y_step=8,
            pos_relative_to=self.rect
        )
        self.friend_bullets.add(Bullet(bullet_data))

    def go_left(self):
        if self.rect.x <= - self.rect.w:
            self.rect.x = WINDOW_WIDTH
        else:
            self.rect.x -= self.sprite_data.x_step

    def go_right(self):
        if self.rect.x == WINDOW_WIDTH:
            self.rect.x = - self.rect.w
        else:
            self.rect.x += self.sprite_data.x_step

    def go_up(self):
        if self.rect.y <= - self.rect.h:
            self.rect.y = WINDOW_HEIGHT
        else:
            self.rect.y -= self.sprite_data.y_step

    def go_down(self):
        if self.rect.y >= WINDOW_HEIGHT + self.rect.h:
            self.rect.y = - self.rect.h
        else:
            self.rect.y += self.sprite_data.y_step


class EnemyOne(object):
    enemy = None

    def __init__(self):
        super(EnemyOne, self).__init__()

        enemy_data = SpriteData(
            image_path='resources/enemies/enemy_one.png',
            y_step=4
        )

        self.enemy = Enemy(enemy_data)