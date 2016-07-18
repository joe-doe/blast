import time
from level import Level
from sprites.asteroids.asteroid import AsteroidBeltOne
from sprites.battleship import BattleshipOne
from sprites.background import BackgroundOne
from sprites.enemies.enemy import EnemySetOne, EnemySetTwo
from sprites.enemies.mothership import MothershipOne


class Level01(Level):

    def __init__(self, score):
        super(Level01, self).__init__(score)
        print "Level 01 Started"

    def initialize_background(self):
        self.background.add(BackgroundOne())

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

        # asteroid belt
        asteroid_belt_one = AsteroidBeltOne(how_many=15)
        self.enemy_sprites.add(asteroid_belt_one.get_asteroid_set())

        # wait until stage cleared
        self.wait_until_no_enemies_on_stage()

        # enemy set one
        enemy_set_one = EnemySetOne(how_many=10,
                                    enemy_bullets=self.enemy_bullets)
        self.enemy_sprites.add(enemy_set_one.get_enemy_set())
        enemy_set_one.start_movement()

        # wait until stage cleared
        self.wait_until_no_enemies_on_stage()

        # enemy set two
        enemy_set_two = EnemySetTwo(how_many=14,
                                    enemy_bullets=self.enemy_bullets)
        self.enemy_sprites.add(enemy_set_two.get_enemy_set())
        enemy_set_two.start_movement()

        # wait until stage cleared
        self.wait_until_no_enemies_on_stage()

        # asteroid belt
        asteroid_belt_one = AsteroidBeltOne(how_many=10)
        self.enemy_sprites.add(asteroid_belt_one.get_asteroid_set())

        # wait until stage cleared
        self.wait_until_no_enemies_on_stage()

        # mothership
        mothership_one = MothershipOne(self.enemy_bullets, self.non_sprites)
        self.enemy_sprites.add(mothership_one.mothership)

        # wait until stage cleared
        self.wait_until_no_enemies_on_stage()

        self.load_next_scene = True
