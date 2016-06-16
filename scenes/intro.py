from scenes.scene import Scene
from sprites.background import Background
import pygame
from constants import *
from sprites.sprite_data import SpriteData


class Intro(Scene):

    def __init__(self):
        super(Intro, self).__init__()

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
        # time line is not applicable here
        pass

    def draw_extra(self, screen):
        font = pygame.font.Font(None, 30)

        high_score_str = "Press 1 to start"

        high_score_text = font.render(
            high_score_str,
            True,
            (255, 255, 255))

        pos = (
            (WINDOW_WIDTH / 2) - (high_score_text.get_width() / 2),
            WINDOW_HEIGHT / 2
        )

        screen.blit(high_score_text, pos)
