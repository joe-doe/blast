from scenes.scene import Scene
from sprites.background import Background
from sprites.sprite_data import SpriteData
from constants import *
from sprites.logo import IntroLogo


class Intro(Scene):

    def __init__(self):
        super(Intro, self).__init__()

    def initialize_background(self):
        background_data = SpriteData(
            image_path='resources/L1_background_800x600.png',
            y_step=1
        )
        self.extra_sprites.add(Background(background_data))
        self.extra_sprites.add(IntroLogo().logo)

    def initialize_sprites(self):
        pass

    def update(self):
        self.extra_sprites.update()

    def draw(self, screen):
        self.extra_sprites.draw(screen)
        self.print_out(screen=screen,
                       string='Press 1 to start',
                       position='bottom-center',
                       size=50,
                       color=RED)

    def run(self):
        # time line is not applicable here
        pass
