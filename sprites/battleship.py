from constants import *
from sprite import Sprite
from sprites.bullet import BulletOne
from sprites.sprite_data import SpriteData


class Battleship(Sprite):

    def __init__(self, battleship_data, friend_bullets):
        super(Battleship, self).__init__(battleship_data)

        self.friend_bullets = friend_bullets

    def initialize_sprite(self):
        self.rect.x = WINDOW_WIDTH/2 - self.rect.w/2
        self.rect.y = WINDOW_HEIGHT - self.rect.h*3

    def fire(self):
        self.friend_bullets.add(BulletOne(self).bullet)

    def update(self):
        super(Battleship, self).update()


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
