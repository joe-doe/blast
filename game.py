import sys
import pygame
from pygame.locals import *
from constants import *
from levels.level_01 import Level01
from levels.level import Level
from game_data import (
    GameData
)
from scenes.intro import Intro

class Game(object):
    clock = None
    screen = None
    level = None
    level_number = 0
    levels = None

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Blast !")

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH,
                                               WINDOW_HEIGHT), 0, 32)

        self.game_data = GameData(self.screen)

        self.scene = Intro()
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
                # if keys[pygame.K_LCTRL]:
                #     self.fire()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if isinstance(self.scene, Level):
                        if event.key == K_LCTRL:
                            self.scene.battleship.fire()
                    if not isinstance(self.scene, Level):
                        if event.key == K_1:
                            self.scene = Level01(self.game_data)
                            self.scene.start()

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)

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


