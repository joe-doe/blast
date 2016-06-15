import time
from scenes.scene import Scene
from sprites.background import Background
from constants import *
import pygame


class Credits(Scene):
    def __init__(self):
        super(Credits, self).__init__()
        print "Credits"

    def initialize_background(self):
        self.all_sprites.add(
            Background(img='resources/L1_background_800x600.png', speed=0)
        )

    def initialize_sprites(self):
        pass

    def update(self):
        self.all_sprites.update()

    def draw(self, screen):
        self.all_sprites.draw(screen)
        self.draw_extra(screen)

    def run(self):
        time.sleep(3)
        self.load_next_scene = True

    def draw_extra(self, screen):

        g_o = pygame.image.load('resources/credits.png').convert_alpha()
        pos = ((WINDOW_WIDTH / 2) - (g_o.get_width() / 2), WINDOW_HEIGHT / 2)

        screen.blit(g_o, pos)

        font = pygame.font.Font(None, 30)

        move_on = "Press space to continue"

        move_on_text = font.render(
            move_on,
            True,
            (255, 255, 255))

        pos = ((WINDOW_WIDTH/2)-(move_on_text.get_width()/2), 150)

        screen.blit(move_on_text, pos)
