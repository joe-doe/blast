import thread
import time
import pygame
from scenes.scene import Scene
from sprites.explosions.explosion import ExplosionOne
from sprites.battleship import Battleship


class Level(Scene):
    enemy_sprites = None
    enemy_bullets = None

    friend_sprites = None
    friend_bullets = None

    explosions = None
    battleship = None

    non_interactive_sprites = None
    non_sprites = None

    game_over = False

    def __init__(self, game_data):
        super(Level, self).__init__()

        self.game_data = game_data

    def update(self):
        self.background.update()

        self.enemy_sprites.update()
        self.enemy_bullets.update()

        self.friend_sprites.update()
        self.friend_bullets.update()

        self.non_interactive_sprites.update()
        # [non_sprite.update() for non_sprite in self.non_sprites]

        self.explosions.update()

    def draw(self, screen):
        self.background.draw(screen)

        self.enemy_sprites.draw(screen)
        self.enemy_bullets.draw(screen)

        self.friend_sprites.draw(screen)
        self.friend_bullets.draw(screen)

        self.non_interactive_sprites.draw(screen)
        [non_sprite.draw(screen) for non_sprite in self.non_sprites]

        self.explosions.draw(screen)

    def initialize_scene(self):
        self.enemy_sprites = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()

        self.friend_sprites = pygame.sprite.Group()
        self.friend_bullets = pygame.sprite.Group()

        self.non_interactive_sprites = pygame.sprite.Group()
        self.non_sprites = []

        self.explosions = pygame.sprite.Group()
        self.background = pygame.sprite.Group()

        super(Level, self).initialize_scene()

    def initialize_sprites(self):
        pass

    def resurrect_battleship(self):
        pass

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
        battleship = None
        for sprite in self.friend_sprites.sprites():
            if isinstance(sprite, Battleship):
                battleship = sprite

        # out of level
        for sprite in self.enemy_sprites:
            if sprite.sprite_data.out_of_bounds is True:
                self.enemy_sprites.remove(sprite)

        for sprite in self.friend_sprites:
            if sprite.sprite_data.out_of_bounds is True:
                self.friend_sprites.remove(sprite)

        if battleship:
            # enemy sprite hit battleship
            collided_sprite = pygame.sprite.spritecollideany(battleship,
                                                             self.enemy_sprites)
            if collided_sprite:
                self.lost_a_life()
                self.enemy_sprites.remove(collided_sprite)
                self.explosions.add(ExplosionOne(collided_sprite).explosion)

            # enemy bullet hit battleship
            collided_bullet = pygame.sprite.spritecollideany(battleship,
                                                             self.enemy_bullets)
            if collided_bullet:
                self.lost_a_life()
                self.enemy_bullets.remove(collided_bullet)
                self.explosions.add(ExplosionOne(collided_bullet).explosion)

            # battleship bullet
            for bullet in self.friend_bullets:
                collided_item = pygame.sprite.spritecollideany(bullet,
                                                               self.enemy_sprites)
                if collided_item:
                    self.friend_bullets.remove(bullet)
                    self.explosions.add(ExplosionOne(collided_item).explosion)
                    collided_item.sprite_data.health -= 1

                    if collided_item.sprite_data.health == 0:
                        collided_item.update()
                        self.enemy_sprites.remove(collided_item)
                        self.game_data.score.modify_score(10)

    def lost_a_life(self):
        print "you lost a life"
        self.friend_sprites.empty()
        self.game_data.lives.live_subtract()

        if self.game_data.lives.get_lives() < 0:
            self.game_over = True
        else:
            thread.start_new_thread(self.resurrect_battleship)

    def wait_until_no_enemies_on_stage(self, interval=2):
        while self.enemy_sprites.sprites():
            time.sleep(interval)
