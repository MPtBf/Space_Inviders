from random import randint, choice

import pygame as pg

from setts import *


class Enemy(pg.sprite.Sprite):
    def __init__(self, sc, image, enemies_list, allSprites):
        pg.sprite.Sprite.__init__(self)
        enemies_list.append(self)
        # allSprites.add(self)
        self.sc = sc
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (randint(0,WIDTH-self.image.get_width()),-randint(0,150) - self.rect.height)
        self.hitbox = self.rect.copy().inflate(-20,-30)
        self.speed = choice((-1,1))*(enemy_speed+randint(-enemy_speed_rand,enemy_speed_rand))

    def update(self):
        self.rect.x += self.speed

        if self.rect.x + self.rect.width > WIDTH:
            self.rect.x = WIDTH - self.rect.width
            self.speed = -self.speed
            self.rect.y += enemy_speed_down + randint(-enemy_speed_down_rand, enemy_speed_down_rand)

        elif self.rect.x < 0:
            self.rect.x = 0
            self.speed = -self.speed
            self.rect.y += enemy_speed_down + randint(-enemy_speed_down_rand, enemy_speed_down_rand)

        if self.rect.top > HEIGHT:
            self.rect.topleft = (randint(0,WIDTH-self.image.get_width()),-randint(0,150) - self.rect.height)

        self.hitbox.center = self.rect.center
        self.drawing()

    def drawing(self):
        self.sc.blit(self.image,self.rect)

        if show_hitboxes:
            hitbox_surf = pg.surface.Surface((self.hitbox.width,self.hitbox.height))
            hitbox_surf.fill(BLUE)
            self.sc.blit(hitbox_surf, self.hitbox)