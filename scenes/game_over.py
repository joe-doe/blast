import time
from scenes.scene import Scene
from sprites.background import Background
from constants import *
import pygame

from sprites.sprite_data import SpriteData


class GameOver(Scene):
    def __init__(self):
        super(GameOver, self).__init__()
        print "GAME OVER"

    def initialize_background(self):
        background_data = SpriteData(
            image_path='resources/L1_background_800x600.png',
            y_step=1
        )
        self.extra_sprites.add(Background(background_data))

    def initialize_sprites(self):
        pass

    def update(self):
        self.extra_sprites.update()

    def draw(self, screen):
        self.extra_sprites.draw(screen)
        self.draw_extra(screen)

    def run(self):
        time.sleep(3)
        self.load_next_scene = True

    def draw_extra(self, screen):
        g_o = pygame.image.load('resources/g_o.png').convert_alpha()
        pos = ((WINDOW_WIDTH / 2) - (g_o.get_width() / 2), WINDOW_HEIGHT / 2)

        screen.blit(g_o, pos)
