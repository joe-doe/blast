import pygame
import threading


class Level(threading.Thread):
    enemy_sprites = None
    friend_sprites = None
    background = None
    battleship = None

    def __init__(self):
        super(Level, self).__init__()
        self.setDaemon(True)

        self.enemy_sprites = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.friend_sprites = pygame.sprite.Group()
        self.friend_bullets = pygame.sprite.Group()
        self.background = pygame.sprite.Group()

        self.initialize_background()
        self.initialize_sprites()

    def initialize_background(self):
        pass

    def initialize_sprites(self):
        pass

    def update(self):
        self.background.update()
        self.enemy_sprites.update()
        self.enemy_bullets.update()
        self.friend_sprites.update()
        self.friend_bullets.update()

    def draw(self, screen):
        self.background.draw(screen)
        self.enemy_sprites.draw(screen)
        self.enemy_bullets.draw(screen)
        self.friend_sprites.draw(screen)
        self.friend_bullets.draw(screen)

    def get_battleship(self):
        return self.battleship

    def go_left(self):
        self.battleship.go_left()

    def go_right(self):
        self.battleship.go_right()

    def go_up(self):
        self.battleship.go_up()

    def go_down(self):
        self.battleship.go_down()

    def clear_the_dead(self):
        # out of level
        for sprite in self.enemy_sprites:
            if sprite.should_die is True:
                self.enemy_sprites.remove(sprite)

        for sprite in self.friend_sprites:
            if sprite.should_die is True:
                self.friend_sprites.remove(sprite)

        # battleship bullet
        for bullet in self.friend_bullets:
            collision_list = pygame.sprite.spritecollide(bullet,
                                                         self.enemy_sprites,
                                                         False)
            for collided_item in collision_list:
                collided_item.should_explode = True
                self.enemy_sprites.remove(collided_item)
