import time
from level import Level
from sprites.asteroids.asteroid import AsteroidBeltOne
from sprites.battleship import BattleshipOne
from sprites.background import BackgroundTwo
from sprites.enemies.enemy import EnemySetOne, EnemySetTwo


class Level02(Level):
    def __init__(self, score):
        super(Level02, self).__init__(score)
        print "Level 02 Started"

    def initialize_background(self):
        self.background.add(BackgroundTwo())

    def initialize_sprites(self):
        self.battleship = BattleshipOne(self.friend_bullets)
        self.friend_sprites.add(self.battleship)

    def resurrect_battleship(self):
        time.sleep(.7)

        # grace period upon resurrection
        for i in range(8):
            self.non_interactive_sprites.add(self.battleship)
            time.sleep(.2)
            self.non_interactive_sprites.empty()
            time.sleep(.2)

        # grace period ended
        self.friend_sprites.add(self.battleship)

    def run(self):
        time.sleep(1)

        # enemy set one
        enemy_set_one = EnemySetOne(how_many=4)
        self.enemy_sprites.add(enemy_set_one.get_enemy_set())
        enemy_set_one.start_movement()

        # wait until stage cleared
        while self.enemy_sprites.sprites():
            time.sleep(2)

        # asteroid belt
        asteroid_belt_one = AsteroidBeltOne(how_many=5)
        self.enemy_sprites.add(asteroid_belt_one.get_asteroid_set())

        # just rest for a bit
        time.sleep(3)

        # enemy set two
        enemy_set_two = EnemySetTwo(how_many=4,
                                    enemy_bullets=self.enemy_bullets)
        self.enemy_sprites.add(enemy_set_two.get_enemy_set())
        enemy_set_two.start_movement()

        # wait until stage cleared
        while self.enemy_sprites.sprites():
            time.sleep(2)

        # asteroid belt
        asteroid_belt_one = AsteroidBeltOne(how_many=5)
        self.enemy_sprites.add(asteroid_belt_one.get_asteroid_set())

        # wait until stage cleared
        while self.enemy_sprites.sprites():
            time.sleep(2)

        self.load_next_scene = True

