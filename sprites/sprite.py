import pygame


class Sprite(pygame.sprite.Sprite):
    image = None
    rect = None
    sprite_data = None

    def __init__(self, sprite_data):
        super(Sprite, self).__init__()

        self.image = pygame.image.load(sprite_data.image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.sprite_data = sprite_data

        self.initialize_sprite()

    def initialize_sprite(self):
        self.rect.x = 0
        self.rect.y = 0

    def go_left(self):
        pass

    def go_right(self):
        pass

    def go_up(self):
        pass

    def go_down(self):
        pass
