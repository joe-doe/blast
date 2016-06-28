import sys
import pygame
from pygame.locals import *
from constants import *
from levels.level_01 import Level01
from levels.level_02 import Level02
from levels.level import Level
from game_data import (
    GameData
)
from scenes.credits import Credits
from scenes.intro import Intro
from scenes.game_over import GameOver


class Game(object):
    clock = None
    screen = None
    level = None
    level_current = 0
    levels = None

    def __init__(self):
        self.levels = [Level01, Level02]

        pygame.init()
        pygame.display.set_caption("Blast !")

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH,
                                               WINDOW_HEIGHT), 0, 32)

        self.game_data = GameData(self.screen)

        self.scene = Intro()
        self.scene.start()

        self.start_main_loop()

    def start_main_loop(self):
        while True:

            keys = pygame.key.get_pressed()
            if isinstance(self.scene, Level):
                if keys[pygame.K_LEFT]:
                    self.scene.battleship.go_left()
                if keys[pygame.K_RIGHT]:
                    self.scene.battleship.go_right()
                if keys[pygame.K_DOWN]:
                    self.scene.battleship.go_down()
                if keys[pygame.K_UP]:
                    self.scene.battleship.go_up()
                # autofire
                # if keys[pygame.K_LCTRL]:
                #     self.fire()

            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.scene.battleship.get_straight(True)
                    if event.key == K_RIGHT:
                        self.scene.battleship.get_straight(False)
                if event.type == KEYDOWN:
                    if isinstance(self.scene, Level):
                        if event.key == K_LCTRL:
                            self.scene.battleship.fire()
                    if isinstance(self.scene, Intro):
                        if event.key == K_1:
                            self.game_data = GameData(self.screen)

                            self.level_current = 0
                            self.scene = self.levels[self.level_current](self.game_data)
                            self.scene.start()
                    if isinstance(self.scene, Credits):
                        if event.key == K_SPACE:
                            self.level_current = 0
                            self.scene = Intro()
                            self.scene.start()

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)

            # check level status
            if isinstance(self.scene, Level):
                if self.scene.game_over:
                    self.level_current = 0
                    self.scene = GameOver()
                    self.scene.start()
                if self.scene.load_next_scene:
                    self.level_current += 1
                    try:
                        self.scene = self.levels[self.level_current](self.game_data)
                        self.scene.start()
                    except IndexError:
                        # show credits
                        self.level_current = 0
                        self.scene = Credits()
                        self.scene.start()

            if isinstance(self.scene, GameOver):
                if self.scene.load_next_scene:
                    self.level_current = 0
                    self.scene = Intro()
                    self.scene.start()

            if isinstance(self.scene, Intro):
                if self.scene.load_next_scene:
                    self.level_current = 0
                    self.game_data = GameData(self.screen)
                    self.scene = self.levels[self.level_current](self.game_data)
                    self.scene.start()

            # update level
            self.scene.update()

            # clear up the dead
            if isinstance(self.scene, Level):
                self.scene.clear_the_dead()

            # blit everything
            self.scene.draw(self.screen)

            # update score
            self.game_data.update()

            pygame.display.flip()
            self.clock.tick(FPS)


