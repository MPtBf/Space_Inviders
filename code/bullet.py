import pygame as pg

from setts import *


class Bullet(pg.sprite.Sprite):
    def __init__(self, sc, image, allSprites, bullets, player_hitbox):
        pg.sprite.Sprite.__init__(self)
        self.allSprites = allSprites
        self.bullets = bullets
        # self.allSprites.add(self)
        self.bullets.append(self)
        self.sc = sc
        self.image = image
        self.rect = self.image.get_rect()
        self.hitbox = self.rect.copy().inflate(-15,0)
        self.rect.midbottom = player_hitbox.midtop

    def update(self):
        self.rect.y -= bullet_speed
        if self.hitbox.bottom < 0:
            self.remove()
        self.hitbox.center = self.rect.center

        self.drawing()

    def drawing(self):
        self.sc.blit(self.image, self.rect)

        if show_hitboxes:
            hitbox_surf = pg.surface.Surface((self.hitbox.width, self.hitbox.height))
            hitbox_surf.fill(RED)
            self.sc.blit(hitbox_surf, self.hitbox)

    def delete(self):
        self.bullets.remove(self)
        self.kill()