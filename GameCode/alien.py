import pygame as pg


class Alien(pg.sprite.Sprite):
    """one alien class"""

    def __init__(self, screen):
        """initialize and spare initial position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pg.image.load('Images/AlienToGame.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """alien drawing"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """alien position update"""
        self.y += 0.1
        self.rect.y = self.y
