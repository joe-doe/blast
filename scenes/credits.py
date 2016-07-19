import time
from scenes.scene import Scene
from sprites.background import BackgroundOne
from constants import *
import pygame


class Credits(Scene):
    def __init__(self):
        super(Credits, self).__init__()
        print "Credits"

    def initialize_background(self):
        self.extra_sprites.add(BackgroundOne())

    def initialize_sprites(self):
        pass

    def update(self):
        self.extra_sprites.update()

    def draw(self, screen):
        self.extra_sprites.draw(screen)
        self.draw_extra(screen)
        self.print_out(screen=screen,
                       string='Press space to continue',
                       position='bottom-center',
                       color=RED)

    def run(self):
        time.sleep(3)
        self.load_next_scene = True

    def draw_extra(self, screen):

        g_o = pygame.image.load('resources/credits.png').convert_alpha()
        pos = (
                  (WINDOW_WIDTH / 2) - (g_o.get_width() / 2),
                  (WINDOW_HEIGHT / 2) - 50
        )

        screen.blit(g_o, pos)
