import threading
import pygame


class Scene(threading.Thread):
    background = None
    all_sprites = None

    def __init__(self):
        super(Scene, self).__init__()

        self.setDaemon(True)

        self.all_sprites = pygame.sprite.Group()

        self.initialize_scene()

    def initialize_background(self):
        pass

    def initialize_sprites(self):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

    def initialize_scene(self):
        self.initialize_background()
        self.initialize_sprites()
