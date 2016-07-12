import pygame
from non_sprite import NonSprite


class ProgressBar(NonSprite):
    percentage = 0
    unit_width = None
    position = None
    height = None

    def __init__(self, unit_width, position, height):
        super(ProgressBar, self).__init__()
        self.unit_width = unit_width
        self.position = position
        self.height = height

        self.rect_data = pygame.Rect(
            position.left,
            position.top,
            unit_width * self.percentage,
            height
        )

    def draw(self, screen):
        self.rect_data.width = self.unit_width * self.percentage
        pygame.draw.rect(screen, (128, 128, 128), self.rect_data)

    def update_data(self, new_percentage):
        self.percentage = new_percentage

    def update_position(self, position):
        self.rect_data.left = position.left
        self.rect_data.top = position.top+20
