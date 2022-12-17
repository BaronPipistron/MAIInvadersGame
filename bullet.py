import pygame as pg


class Bullet(pg.sprite.Sprite):

    def __init__(self, screen, gun):
        """create a bullet in the position of the gun"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pg.Rect(0, 0, 2, 10)
        self.color = 255, 203, 14
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """moving the bullet up"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """bullet drawing"""
        pg.draw.rect(self.screen, self.color, self.rect)
