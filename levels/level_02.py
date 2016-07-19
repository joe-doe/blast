import time
from level import Level
from sprites.asteroids.asteroid import AsteroidBeltOne
from sprites.battleship import BattleshipOne
from sprites.background import BackgroundTwo
from sprites.enemies.enemy import EnemySetOne, EnemySetTwo
from sprites.enemies.mothership import MothershipTwo
from sprites.power_ups import (
    UpgradeBattleshipWeapon,
    ShieldsOn
)
from sprites.label import (
    LevelLabel,
    LevelCompleted
)


class Level02(Level):
    def __init__(self, score):
        super(Level02, self).__init__(score)
        print "Level 02 Started"

    def initialize_background(self):
        self.background.add(BackgroundTwo())

    def initialize_sprites(self):
        self.battleship = BattleshipOne(
            self.friend_bullets,
            self.non_interactive_sprites
        )
        self.friend_sprites.add(self.battleship)

    def run(self):
        start = time.time()
        time.sleep(1)

        cp1 = time.time() - start
        print "passed: {}".format(cp1)
        # level label
        label = LevelLabel(2)
        self.non_interactive_sprites.add(label)
        time.sleep(2)
        self.non_interactive_sprites.remove(label)

        cp1 = time.time() - start
        print "passed: {}".format(cp1)
        # enemy set one
        enemy_set_one = EnemySetOne(how_many=4)
        self.enemy_sprites.add(enemy_set_one.get_enemy_set())
        enemy_set_one.start_movement()

        cp1 = time.time() - start
        print "passed: {}".format(cp1)
        # shields upgrade
        self.interactive_sprites.add(ShieldsOn())

        # wait until stage cleared
        self.wait_until_no_enemies_on_stage()

        cp1 = time.time() - start
        print "passed: {}".format(cp1)
        # asteroid belt
        asteroid_belt_one = AsteroidBeltOne(how_many=5)
        self.enemy_sprites.add(asteroid_belt_one.get_asteroid_set())

        cp1 = time.time() - start
        print "passed: {}".format(cp1)
        # just rest for a bit
        # time.sleep(1)

        # enemy set two
        enemy_set_two = EnemySetTwo(how_many=4,
                                    enemy_bullets=self.enemy_bullets)
        self.enemy_sprites.add(enemy_set_two.get_enemy_set())
        enemy_set_two.start_movement()

        cp1 = time.time() - start
        print "passed: {}".format(cp1)
        # wait until stage cleared
        self.wait_until_no_enemies_on_stage()

        # shields upgrade
        self.interactive_sprites.add(ShieldsOn())

        cp1 = time.time() - start
        print "passed: {}".format(cp1)
        # asteroid belt
        asteroid_belt_one = AsteroidBeltOne(how_many=5)
        self.enemy_sprites.add(asteroid_belt_one.get_asteroid_set())

        # wait until stage cleared
        self.wait_until_no_enemies_on_stage()

        cp1 = time.time() - start
        print "passed: {}".format(cp1)
        # mothership
        mothership_two = MothershipTwo(self.enemy_bullets, self.non_sprites)
        self.enemy_sprites.add(mothership_two)

        # wait until stage cleared
        self.wait_until_no_enemies_on_stage()

        # level completed
        label = LevelCompleted()
        self.non_interactive_sprites.add(label)
        time.sleep(2)
        self.non_interactive_sprites.remove(label)

        self.load_next_scene = True

