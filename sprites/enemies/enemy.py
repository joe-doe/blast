from daemon_thread import DaemonThread
from sprites.bullet import EnemyWeaponTwo
from sprites.sprite import Sprite
from sprites.sprite_data import SpriteData
from random import uniform, randint
import time


class Enemy(Sprite):
    enemy_bullets = None
    health = 0
    weapon = None

    # need to pass class for weapon because Weapon needs igniter
    def __init__(self, enemy_bullets):
        super(Enemy, self).__init__()
        self.enemy_bullets = enemy_bullets
        try:
            self.weapon = self.sprite_data.weapon
        except TypeError:
            pass

    def initialize_sprite(self):
        super(Enemy, self).initialize_sprite()

        self.rect.x = self.sprite_data.x_start
        self.rect.y = self.sprite_data.y_start

    def fire(self):
        self.enemy_bullets.add(self.weapon.get_bullets(self))

    def set_weapon(self, weapon):
        self.weapon = weapon

    def update(self):
        super(Enemy, self).update()

        if self.sprite_data.should_fire:
            if randint(0, 100) < 2:
                self.fire()
        self.rect.y += self.sprite_data.y_step
        self.rect.x += self.sprite_data.x_step


class EnemyOne(Enemy):

    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/enemies/enemy_one.png',
            x_start=100,
            y_start=-80,
            y_step=0
        )


class EnemyTwo(Enemy):

    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/enemies/enemy_two.png',
            x_start=700,
            y_start=-95,
            y_step=0,
            weapon=EnemyWeaponTwo(),
            should_fire=True
        )


class EnemySet(object):
    enemy_set = None
    how_many = 0
    enemy_data = None

    def __init__(self, how_many, enemy_bullets):
        super(EnemySet, self).__init__()

        self.enemy_set = []
        self.enemy_bullets = enemy_bullets
        self.how_many = how_many
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
        DaemonThread(target=self.turn_right, args=(speed, )).start()
        delay = float(sleep_time)/self.how_many*speed
        time.sleep(delay)

    def go_left(self, speed=0, sleep_time=1):
        DaemonThread(target=self.turn_left, args=(speed, )).start()
        delay = float(sleep_time)/self.how_many*speed
        time.sleep(delay)

    def go_down(self, speed=0, sleep_time=1):
        DaemonThread(target=self.speed_up, args=(speed, )).start()
        delay = float(sleep_time)/self.how_many*speed
        time.sleep(delay)

    def go_up(self, speed=0, sleep_time=1):
        DaemonThread(target=self.slow_down, args=(speed, )).start()
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
        def __init__(self, how_many=3, enemy_bullets=None):
            super(EnemySetOne, self).__init__(how_many, enemy_bullets)

        def initialize_set(self):
            for i in range(self.how_many):
                self.enemy_set.append(EnemyOne(self.enemy_bullets))

        def start_movement(self):
            self.go_down(speed=4, sleep_time=3)
            self.go_right(speed=7, sleep_time=5)
            self.go_left(speed=7, sleep_time=2)


class EnemySetTwo(EnemySet):
        def __init__(self, how_many=3, enemy_bullets=None):
            super(EnemySetTwo, self).__init__(how_many, enemy_bullets)

        def initialize_set(self):
            for i in range(self.how_many):
                self.enemy_set.append(EnemyTwo(self.enemy_bullets))

        def start_movement(self):
            self.go_down(speed=4, sleep_time=0)
            self.go_left(speed=3, sleep_time=25)

            self.go_up(speed=4, sleep_time=5)
            self.go_up(speed=4, sleep_time=5)
            self.go_right(speed=3, sleep_time=5)
            self.go_right(speed=3, sleep_time=5)

            self.go_down(speed=3, sleep_time=5)
            self.go_right(speed=3, sleep_time=5)
