import pygame as pg
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores

FPS = 120
clock = pg.time.Clock()


def run():

    pg.init()
    screen = pg.display.set_mode((1200, 800))
    pg.display.set_caption("MAI Invaders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens)
    stats = Stats()
    sc = Scores(screen, stats)
    pg.mixer.music.load('Sounds/OpeningSound.mp3')
    pg.mixer.music.play()

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.screen_update(bg_color, screen, stats, sc, gun, aliens, bullets)
            controls.update_bullets(screen, stats, sc, aliens, bullets)
            controls.update_aliens(stats, screen, sc, gun, aliens, bullets)
        clock.tick(FPS)


run()
