import pygame as pg

from setts import *


class Bullet(pg.sprite.Sprite):
    def __init__(self, sc, image, allSprites, bullets, player_hitbox, direction):
        pg.sprite.Sprite.__init__(self)
        self.allSprites = allSprites
        self.bullets = bullets
        self.direction = direction
        # self.allSprites.add(self)
        self.bullets.append(self)
        self.sc = sc
        self.image = image
        self.images = [pg.transform.rotate(self.image, -90*i) for i in range(4)]
        self.rect = self.image.get_rect()
        self.vector = pg.math.Vector2((0,0))
        if self.direction == "up":
            self.vector.xy = (0, -bullet_speed)
            self.image = self.images[0]
            self.hitbox = self.rect.copy().inflate(-20,-5)
            self.rect.midbottom = (player_hitbox.center[0], player_hitbox.midtop[1] + self.rect.height//2)
        elif self.direction == "down":
            self.vector.xy = (0, bullet_speed)
            self.image = self.images[2]
            self.hitbox = self.rect.copy().inflate(-20,-5)
            self.rect.midtop = (player_hitbox.center[0], player_hitbox.midbottom[1] - self.rect.height//2)
        elif self.direction == "right":
            self.vector.xy = (bullet_speed, 0)
            self.image = self.images[1]
            self.hitbox = self.rect.copy().inflate(-5,-20)
            self.rect.midleft = (player_hitbox.midright[0] - self.rect.width//2, player_hitbox.center[1])
        elif self.direction == "left":
            self.vector.xy = (-bullet_speed, 0)
            self.image = self.images[3]
            self.hitbox = self.rect.copy().inflate(-5,-20)
            self.rect.midright = (player_hitbox.midleft[0] + self.rect.width//2, player_hitbox.center[1])

    def update(self):
        self.rect.topleft += self.vector
        if self.hitbox.bottom < 0:
            self.remove()
        elif self.hitbox.top > HEIGHT:
            self.remove()
        elif self.hitbox.right < 0:
            self.remove()
        elif self.hitbox.left > HEIGHT:
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