from sprites.bullet import EnemyWeaponOne
from sprites.sprite import Sprite
from sprites.sprite_data import SpriteData
from random import randint
from non_sprite.progress_bar import ProgressBar


class Mothership(Sprite):
    mothership_bullets = None
    weapon = None

    def __init__(self,  mothership_bullets, non_sprites):
        super(Mothership, self).__init__()
        self.mothership_bullets = mothership_bullets
        self.non_sprites = non_sprites

        self.health_progress = ProgressBar(10, self.rect, 15)
        self.non_sprites.append(self.health_progress)

        self.weapon = self.sprite_data.weapon

    def fire(self):
        self.mothership_bullets.add(self.weapon.get_bullets(self))

    def update(self):
        super(Mothership, self).update()

        if self.sprite_data.should_fire:
            if randint(0, 100) < 2:
                self.fire()

        if self.rect.y < 10:
            self.rect.y += self.sprite_data.y_step
        self.rect.x += self.sprite_data.x_step
        self.bounce_x()

        self.health_progress.update_data(self.sprite_data.health)
        self.health_progress.update_position(self.rect)

        if self.sprite_data.health == 0:
            self.non_sprites.remove(self.health_progress)


class MothershipOne(Mothership):
    def feed_data(self):
        self.sprite_data = SpriteData(
            image_path='resources/enemies/mothership_one.png',
            x_step=2,
            y_step=2,
            y_start=-250,
            should_fire=True,
            health=15,
            weapon=EnemyWeaponOne()
        )
