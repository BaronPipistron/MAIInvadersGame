import pygame.font
from lives import Lives
from pygame.sprite import Group


class Scores:
    """output game information"""
    def __init__(self, screen, stats):
        """scoring initialization"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_lives()

    def image_score(self):
        """converts score text to graphics"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        """converts high score to graphics"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_lives(self):
        """number of lives"""
        self.lives = Group()
        for live_number in range(self.stats.guns_loss):
            live = Lives(self.screen)
            live.rect.x = 15 + live_number * live.rect.width
            live.rect.y = 20
            self.lives.add(live)

    def show_score(self):
        """score drawing"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.lives.draw(self.screen)
