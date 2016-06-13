import time
from level import Level
from sprites.battleship import Battleship
from sprites.asteroids.asteroid_alpha import AsteroidAlpha
from sprites.bullet import Bullet
from sprites.background import Background


class Level01(Level):
    def __init__(self):
        super(Level01, self).__init__()
        print "LEVEL 01 STARTED"

    def initialize_background(self):
        image = 'resources/L1_background_800x600.png'
        speed = 1
        self.background.add(Background(image, speed))

    def initialize_sprites(self):
        self.battleship = Battleship()
        self.friend_sprites.add(self.battleship)

    def fire(self):
        battleship_rect = self.friend_sprites.spritedict.get(self.battleship)
        battleship_rect.y -= 50
        self.friend_bullets.add(Bullet(battleship_rect))

    def run(self):
        self.enemy_sprites.add(AsteroidAlpha())

        # while True:
        #     time.sleep(1)
        #     self.enemy_sprites.add(AsteroidAlpha())
