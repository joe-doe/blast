import time
from level import Level
from sprites.battleship import Battleship
from sprites.asteroids.asteroid_alpha import AsteroidAlpha
from sprites.background import Background


class Level01(Level):
    def __init__(self, score):
        super(Level01, self).__init__(score)
        print "LEVEL 01 STARTED"

    def initialize_background(self):
        self.background.add(
            Background(img='resources/L1_background_800x600.png', speed=1)
        )

    def initialize_sprites(self):
        self.battleship = Battleship(self.friend_bullets)
        self.friend_sprites.add(self.battleship)

    def run(self):
        while self.friend_sprites.has(self.battleship):
            time.sleep(2)
            self.enemy_sprites.add(AsteroidAlpha())
