import time
from level import Level
from sprites.battleship import BattleshipOne
from sprites.asteroids.asteroid import AsteroidAlpha
from sprites.background import Background
from sprites.enemies.enemy import EnemyOne
from sprites.sprite_data import SpriteData


class Level01(Level):

    def __init__(self, score):
        super(Level01, self).__init__(score)
        print "LEVEL 01 STARTED"

    def initialize_background(self):
        background_data = SpriteData(
            image_path='resources/L1_background_800x600.png',
            y_step=1
        )
        self.background.add(Background(background_data))

    def initialize_sprites(self):

        self.battleship = BattleshipOne(self.friend_bullets).battleship
        self.friend_sprites.add(self.battleship)

    def run(self):
        while not (self.game_over and self.load_next_scene):
            time.sleep(2)
            # self.enemy_sprites.add(AsteroidAlpha().asteroid)
            e1 = EnemyOne().enemy

            self.enemy_sprites.add(e1)
            time.sleep(2)
            e1.sprite_data.set_y_step(8)

            time.sleep(1)
            e1.sprite_data.set_x_step(8)
            e1.go_left()

            if self.game_data.score.total == 100:
                self.load_next_scene = True
