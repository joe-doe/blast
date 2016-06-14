from scenes.scene import Scene
from sprites.background import Background
import pygame
from constants import *


class Intro(Scene):

    font = None

    def __init__(self):
        super(Intro, self).__init__()

    def initialize_background(self):
        self.all_sprites.add(
            Background(img='resources/L1_background_800x600.png', speed=0)
        )

    def initialize_sprites(self):
        pass

    def draw_extra(self, screen):
        self.font = pygame.font.Font(None, 30)

        high_score_str = "Press 1 to start"

        high_score_text = self.font.render(
            high_score_str,
            True,
            (255, 255, 255))

        pos = ((WINDOW_WIDTH/2)-(high_score_text.get_width()/2), WINDOW_HEIGHT/2)

        screen.blit(high_score_text, pos)

    def update(self):
        self.all_sprites.update()

    def draw(self, screen):
        self.all_sprites.draw(screen)
        self.draw_extra(screen)




