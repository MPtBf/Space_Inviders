import pygame as pg

from setts import *


class Player(pg.sprite.Sprite):
    def __init__(self, sc, image, allSprites, direction):
        pg.sprite.Sprite.__init__(self)
        allSprites.add(self)
        self.sc = sc
        self.image = image
        self.images = [pg.transform.rotate(self.image, -90*i) for i in range(4)]
        start_pos = (HALF_WIDTH-self.image.get_width()//2,HEIGHT-50-self.image.get_height())
        self.rect = self.image.get_rect()
        self.rect.topleft = start_pos
        self.hitbox = self.rect.copy().inflate(-20,-20)
        self.speed = player_speed
        self.direction = direction
        self.vector = pg.math.Vector2((0,0))

    def update(self):
        # движение
        keys = pg.key.get_pressed()
        if keys[pg.K_LCTRL]:
            self.speed = player_speed * 2
        else:
            self.speed = player_speed
        if keys[pg.K_d]:
            self.direction = "right"
            self.vector.x = self.speed
            self.image = self.images[1]
        if keys[pg.K_a]:
            self.direction = "left"
            self.vector.x = -self.speed
            self.image = self.images[3]
        self.rect.topleft += self.vector
        self.vector.xy = (0,0)
        if keys[pg.K_w]:
            self.direction = "up"
            self.vector.y = -self.speed
            self.image = self.images[0]
        if keys[pg.K_s]:
            self.direction = "down"
            self.vector.y = self.speed
            self.image = self.images[2]

        if keys[pg.K_RIGHT]:
            self.direction = "right"
            self.image = self.images[1]
        if keys[pg.K_LEFT]:
            self.direction = "left"
            self.image = self.images[3]
        if keys[pg.K_UP]:
            self.direction = "up"
            self.image = self.images[0]
        if keys[pg.K_DOWN]:
            self.direction = "down"
            self.image = self.images[2]



        # столкновение игрока с границами экрана
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width

        # линк хитбокса и рисование на экран
        self.hitbox.center = self.rect.center

        self.drawing()

    def drawing(self):
        self.sc.blit(self.image, self.rect)

        if show_hitboxes:
            hitbox_surf = pg.surface.Surface((self.hitbox.width, self.hitbox.height))
            hitbox_surf.fill(GREEN)
            self.sc.blit(hitbox_surf, (self.hitbox))
