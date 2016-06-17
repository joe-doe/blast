import time
from level import Level
from sprites.asteroids.asteroid import AsteroidBeltOne
from sprites.battleship import BattleshipOne
from sprites.background import Background
from sprites.enemies.enemy import EnemySetOne, EnemySetTwo
from sprites.sprite_data import SpriteData


class Level01(Level):

    def __init__(self, score):
        super(Level01, self).__init__(score)
        print "Level 01 Started"

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
        time.sleep(1)

        # asteroid belt
        asteroid_belt_one = AsteroidBeltOne(how_many=5)
        self.enemy_sprites.add(asteroid_belt_one.get_asteroid_set())

        # wait until stage cleared
        while self.enemy_sprites.sprites():
            time.sleep(2)

        # enemy set one
        enemy_set_one = EnemySetOne(how_many=4,
                                    start_here=100,
                                    enemy_bullets=self.enemy_bullets)
        self.enemy_sprites.add(enemy_set_one.get_enemy_set())
        enemy_set_one.start_movement()

        # wait until stage cleared
        while self.enemy_sprites.sprites():
            time.sleep(2)

        # enemy set two
        enemy_set_two = EnemySetTwo(how_many=4,
                                    start_here=500,
                                    enemy_bullets=self.enemy_bullets)
        self.enemy_sprites.add(enemy_set_two.get_enemy_set())
        enemy_set_two.start_movement()

        # wait until stage cleared
        while self.enemy_sprites.sprites():
            time.sleep(2)

        # asteroid belt
        asteroid_belt_one = AsteroidBeltOne(how_many=10)
        self.enemy_sprites.add(asteroid_belt_one.get_asteroid_set())

        # wait until stage cleared
        while self.enemy_sprites.sprites():
            time.sleep(2)

        self.load_next_scene = True
