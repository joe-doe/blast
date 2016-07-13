import thread

from constants import *
from sprites.bullet import Bullet
from sprites.sprite import Sprite
from sprites.sprite_data import SpriteData
from random import uniform, randint
import time


class Enemy(Sprite):
    enemy_bullets = None
    health = 0

    def __init__(self, enemy_data, enemy_bullets):
        super(Enemy, self).__init__(enemy_data)
        self.enemy_bullets = enemy_bullets

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

        if self.sprite_data.should_fire:
            if randint(0, 100) < 2:
                self.fire()
        self.rect.y += self.sprite_data.y_step
        self.rect.x += self.sprite_data.x_step


class EnemyOne(object):
    enemy = None

    def __init__(self, enemy_bullets):
        super(EnemyOne, self).__init__()

        enemy_data = SpriteData(
            image_path='resources/enemies/enemy_one.png',
            x_start=uniform(0, WINDOW_WIDTH),
            y_step=4
        )

        self.enemy = Enemy(enemy_data, enemy_bullets)


class EnemySet(object):
    enemy_set = None
    how_many = 0
    enemy_data = None
    start_here = None

    def __init__(self, how_many, start_here, enemy_bullets):
        super(EnemySet, self).__init__()

        self.enemy_set = []
        self.enemy_bullets = enemy_bullets
        self.how_many = how_many
        self.start_here = start_here
        self.initialize_set()

    def initialize_set(self):
        pass

    def start_movement(self):
        pass

    def get_enemy_set(self):
        for enemy in self.enemy_set:
            # time.sleep(0.5)
            yield enemy

    def go_right(self, speed=0, sleep_time=1):
        thread.start_new_thread(self.turn_right, (speed, ))
        delay = float(sleep_time)/self.how_many*speed
        time.sleep(delay)

    def go_left(self, speed=0, sleep_time=1):
        thread.start_new_thread(self.turn_left, (speed, ))
        delay = float(sleep_time)/self.how_many*speed
        time.sleep(delay)

    def go_down(self, speed=0, sleep_time=1):
        thread.start_new_thread(self.speed_up, (speed, ))
        delay = float(sleep_time)/self.how_many*speed
        time.sleep(delay)

    def go_up(self, speed=0, sleep_time=1):
        thread.start_new_thread(self.slow_down, (speed, ))
        delay = float(sleep_time)/self.how_many*speed
        time.sleep(delay)

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
        def __init__(self, how_many=3, start_here=100, enemy_bullets=None):
            super(EnemySetOne, self).__init__(how_many, start_here, enemy_bullets)

        def initialize_set(self):
            for i in range(self.how_many):
                enemy_data = SpriteData(
                    image_path='resources/enemies/enemy_one.png',
                    x_start=self.start_here,
                    y_start=-80,
                    y_step=0
                )
                self.enemy_set.append(Enemy(enemy_data, self.enemy_bullets))

        def start_movement(self):
            print "enter start_movement"
            time.sleep(1)

            self.go_down(speed=4, sleep_time=3)
            self.go_right(speed=7, sleep_time=5)
            self.go_left(speed=7, sleep_time=2)


class EnemySetTwo(EnemySet):
        def __init__(self, how_many=3, start_here=100, enemy_bullets=None):
            super(EnemySetTwo, self).__init__(how_many, start_here, enemy_bullets)

        def initialize_set(self):
            for i in range(self.how_many):
                enemy_data = SpriteData(
                    image_path='resources/enemies/enemy_two.png',
                    x_start=self.start_here,
                    y_step=0,
                    should_fire=True
                )
                self.enemy_set.append(Enemy(enemy_data, self.enemy_bullets))

        def start_movement(self):
            time.sleep(1)

            self.go_down(speed=4, sleep_time=3)
            self.go_left(speed=8, sleep_time=3)
            self.go_right(speed=8, sleep_time=4)
            self.go_up(speed=6, sleep_time=5)
            self.go_right(speed=8, sleep_time=2)
            self.go_up(speed=8, sleep_time=4)
