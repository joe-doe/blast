import time
from level import Level
from sprites.battleship import Battleship 
from sprites.asteroid import Asteroid
from sprites.bullet import Bullet
from background import Background


class Level01(Level):
    battleship = None

    def __init__(self):
        super(Level01, self).__init__()
        print "LEVEL 01 STARTED"

    def initialize_background(self):
        image = 'recources/background_800x600.png'
        speed = 1
        self.background.add(Background(image, speed))

    def initialize_sprites(self):
        self.battleship = Battleship()
        self.friend_sprites.add(self.battleship)

    def fire(self):
        battleship_rect = self.friend_sprites.spritedict.get(self.battleship)
        battleship_rect.y -= 50
        self.friend_sprites.add(Bullet(battleship_rect))

    def run(self):
        while True:
            self.enemy_sprites.add(Asteroid())
            time.sleep(3)
            self.enemy_sprites.add(Asteroid())
            time.sleep(2)
            self.enemy_sprites.add(Asteroid())
            time.sleep(4)
            self.enemy_sprites.add(Asteroid())
