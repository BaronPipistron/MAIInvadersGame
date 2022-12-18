import pygame as pg
from pygame.sprite import Sprite


class Gun(Sprite):

    def __init__(self, screen):
        """gun initialization"""
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pg.image.load('Images/GunToGame.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def output(self):
        """gun drawing"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """gun position update"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.move_left and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_new_gun(self):
        """creates a new gun"""
        self.center = self.screen_rect.centerx
