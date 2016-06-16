from constants import *
from sprite import Sprite
from sprites.bullet import Bullet
from sprites.sprite_data import SpriteData, AnimatedSpriteData


class Battleship(Sprite):

    def __init__(self, battleship_data, friend_bullets):
        super(Battleship, self).__init__(battleship_data)

        self.friend_bullets = friend_bullets

    def initialize_sprite(self):
        self.rect.x = WINDOW_WIDTH/2 - self.rect.w/2
        self.rect.y = WINDOW_HEIGHT - self.rect.h*3

    def update(self):
        pass

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


class BattleshipOne(object):
    battleship = None

    def __init__(self, friend_bullets):
        super(BattleshipOne, self).__init__()

        battleship_data = SpriteData(
            image_path='resources/spaceship/spaceship_1.png',
            x_step=6,
            y_step=6
        )

        self.battleship = Battleship(battleship_data, friend_bullets)
