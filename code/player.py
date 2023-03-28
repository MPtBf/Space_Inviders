import pygame as pg

from setts import *


class Player(pg.sprite.Sprite):
    def __init__(self, sc, image, allSprites):
        pg.sprite.Sprite.__init__(self)
        allSprites.add(self)
        self.sc = sc
        self.image = image
        start_pos = (HALF_WIDTH-self.image.get_width()//2,HEIGHT-50-self.image.get_height())
        self.rect = self.image.get_rect()
        self.rect.topleft = start_pos
        self.hitbox = self.rect.copy().inflate(-20,-20)

    def update(self):
        # движение
        keys = pg.key.get_pressed()
        if keys[pg.K_LCTRL]:
            player_speed = 10
        else:
            player_speed = 5
        if keys[pg.K_d]:
            self.rect.x += player_speed
        if keys[pg.K_a]:
            self.rect.x -= player_speed

        # отладка
        if v_moving:
            if keys[pg.K_w]:
                self.rect.y -= player_speed
            if keys[pg.K_s]:
                self.rect.y += player_speed

        # столкновение игрока с границами экрана
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width

        # if keys[pg.K_LSHIFT]:
        #     FPS = 10
        # else:
        #     FPS = 60
        # линк хитбокса и рисование на экран
        self.hitbox.center = self.rect.center

        self.drawing()

    def drawing(self):
        self.sc.blit(self.image, self.rect)

        if show_hitboxes:
            hitbox_surf = pg.surface.Surface((self.hitbox.width, self.hitbox.height))
            hitbox_surf.fill(GREEN)
            self.sc.blit(hitbox_surf, (self.hitbox))
