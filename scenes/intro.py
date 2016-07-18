from scenes.scene import Scene
from sprites.background import BackgroundOne
from constants import *
from sprites.logo import IntroLogo


class Intro(Scene):

    def __init__(self):
        super(Intro, self).__init__()

    def initialize_background(self):
        self.extra_sprites.add(BackgroundOne())

    def initialize_sprites(self):
        self.extra_sprites.add(IntroLogo())

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
        pass
        # time line is not applicable here
