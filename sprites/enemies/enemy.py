from constants import *
from sprites.bullet import Bullet
from sprites.sprite import Sprite
from sprites.sprite_data import SpriteData
from random import uniform
import time


class Enemy(Sprite):

    def __init__(self, enemy_data):
        super(Enemy, self).__init__(enemy_data)

    def fire(self):
        bullet_data = SpriteData(
            image_path='resources/spaceship/enemy_bullet.png',
            x_step=0,
            y_step=8,
            pos_relative_to=self.rect
        )
        self.enemy_bullets.add(Bullet(bullet_data))

    def update(self):
        super(Enemy, self).update()

        self.rect.y += self.sprite_data.y_step
        self.rect.x += self.sprite_data.x_step


class EnemyOne(object):
    enemy = None

    def __init__(self):
        super(EnemyOne, self).__init__()

        enemy_data = SpriteData(
            image_path='resources/enemies/enemy_one.png',
            x_start=uniform(0, WINDOW_WIDTH),
            y_step=4
        )

        self.enemy = Enemy(enemy_data)


class EnemySet(object):
    enemy_set = None
    how_many = 0
    enemy_data = None
    start_here = None

    def __init__(self, how_many, start_here):
        super(EnemySet, self).__init__()

        self.enemy_set = []
        self.how_many = how_many
        self.start_here = start_here
        self.initialize_set()

    def initialize_set(self):
        pass

    def start_movement(self):
        pass

    def get_enemy_set(self):
        for enemy in self.enemy_set:
            time.sleep(0.5)
            yield enemy

    def turn_right(self, speed=0):
        for enemy in self.enemy_set:
            if speed:
                enemy.sprite_data.x_step += speed
            else:
                enemy.sprite_data.x_step += 1
            time.sleep(0.5)

    def turn_left(self, speed=0):
        for enemy in self.enemy_set:
            if speed:
                enemy.sprite_data.x_step -= speed
            else:
                enemy.sprite_data.x_step -= 1
            time.sleep(0.5)

    def slow_down(self, speed=0):
        for enemy in self.enemy_set:
            if speed:
                enemy.sprite_data.y_step -= speed
            else:
                enemy.sprite_data.y_step -= 1
            time.sleep(0.5)

    def speed_up(self, speed=0):
        for enemy in self.enemy_set:
            if speed:
                enemy.sprite_data.y_step += speed
            else:
                enemy.sprite_data.y_step += 1
            time.sleep(0.5)


class EnemySetOne(EnemySet):
        def __init__(self, how_many=3, start_here=100):
            super(EnemySetOne, self).__init__(how_many, start_here)

        def initialize_set(self):
            for i in range(self.how_many):
                enemy_data = SpriteData(
                    image_path='resources/enemies/enemy_one.png',
                    x_start=self.start_here,
                    y_step=2
                )
                self.enemy_set.append(Enemy(enemy_data))

        def start_movement(self):
            time.sleep(.7)

            self.turn_right(5)
            time.sleep(.3)

            self.turn_left(8)
            time.sleep(.5)

            self.turn_right(3)
            self.speed_up(4)


class EnemySetTwo(EnemySet):
        def __init__(self, how_many=3, start_here=100):
            super(EnemySetTwo, self).__init__(how_many, start_here)

        def initialize_set(self):
            for i in range(self.how_many):
                enemy_data = SpriteData(
                    image_path='resources/enemies/enemy_two.png',
                    x_start=self.start_here,
                    y_step=3
                )
                self.enemy_set.append(Enemy(enemy_data))

        def start_movement(self):
            time.sleep(1)

            self.turn_left(8)
            time.sleep(.5)

            self.turn_right(8)
            time.sleep(.3)

            self.slow_down(6)
            time.sleep(1.8)

            self.turn_right(8)
            self.speed_up(8)
            time.sleep(3)
