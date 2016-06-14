import pygame
import threading

from sprites.explosions.explosion_one import ExplosionOne


class Level(threading.Thread):
    enemy_sprites = None
    enemy_bullets = None

    friend_sprites = None
    friend_bullets = None

    explosions = None
    background = None
    battleship = None

    def __init__(self, game_data):
        super(Level, self).__init__()
        self.setDaemon(True)

        self.game_data = game_data
        self.initialize_level()

    def initialize_level(self):
        self.enemy_sprites = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()

        self.friend_sprites = pygame.sprite.Group()
        self.friend_bullets = pygame.sprite.Group()

        self.explosions = pygame.sprite.Group()
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

        self.explosions.update()

    def draw(self, screen):
        self.background.draw(screen)

        self.enemy_sprites.draw(screen)
        self.enemy_bullets.draw(screen)

        self.friend_sprites.draw(screen)
        self.friend_bullets.draw(screen)

        self.explosions.draw(screen)

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
            if sprite.out_of_bounds is True:
                self.enemy_sprites.remove(sprite)

        for sprite in self.friend_sprites:
            if sprite.out_of_bounds is True:
                self.friend_sprites.remove(sprite)

        # enemy sprite hit battleship
        collided_item = pygame.sprite.spritecollideany(self.battleship,
                                                       self.enemy_sprites)
        if collided_item:
            print "you lost a life"
            self.friend_sprites.remove(self.battleship)
            self.explosions.add(ExplosionOne(collided_item.rect))
            self.game_data.lives.live_subtract()
            self.initialize_level()

        # battleship bullet
        for bullet in self.friend_bullets:
            collided_item = pygame.sprite.spritecollideany(bullet,
                                                           self.enemy_sprites)
            if collided_item:
                self.enemy_sprites.remove(collided_item)
                self.friend_bullets.remove(bullet)
                self.explosions.add(ExplosionOne(collided_item.rect))
                self.game_data.score.modify_score(10)
