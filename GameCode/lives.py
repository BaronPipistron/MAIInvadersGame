import pygame as pg
from pygame.sprite import Sprite


class Lives(Sprite):

    def __init__(self, screen):
        """lives initialization"""
        super(Lives, self).__init__()
        self.screen = screen
        self.image = pg.image.load('Images/Live.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def output(self):
        """gun drawing"""
        self.screen.blit(self.image, self.rect)
