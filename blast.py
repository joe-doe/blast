import pygame
import sys

from pygame.locals import *
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
        pygame.display.set_caption("Asteroids !")

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH,
                                               WINDOW_HEIGHT), 0, 32)
        self.level = Level01()
        self.level.start()
        self.start_main_loop()

    def start_main_loop(self):
        while True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.level.go_left()
            if keys[pygame.K_RIGHT]:
                self.level.go_right()
            if keys[pygame.K_DOWN]:
                self.level.go_down()
            if keys[pygame.K_UP]:
                self.level.go_up()
            if keys[pygame.K_LCTRL]:
                self.level.fire()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        print "UP"
                    elif event.key == K_DOWN:
                        print "DOWN"
                    elif event.key == K_LCTRL:
                        print "CONTROL"

                if event.type == MOUSEBUTTONDOWN:
                    print "MOUSE DOWN"

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)

            # update level
            self.level.update()

            # clear up the dead
            self.level.clear_the_dead()

            # blit everything
            self.level.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)


