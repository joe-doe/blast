import pygame
from constants import *
from levels.level_01 import Level01


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
        self.level = Level01()
        self.level.start()
        self.start_main_loop()

    def start_main_loop(self):
        while True:
            # update level
            self.level.update()

            # clear up the dead
            self.level.clear_the_dead()

            # blit everything
            self.level.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)


