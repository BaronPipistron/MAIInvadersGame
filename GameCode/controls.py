import pygame as pg
import sys
import time
from bullet import Bullet
from alien import Alien


def events(screen, gun, bullets):
    """event processing"""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            """movement to the right"""
            if event.key == pg.K_d or event.key == pg.K_RIGHT:
                gun.move_right = True
            elif event.key == pg.K_a or event.key == pg.K_LEFT:
                gun.move_left = True
            elif event.key == pg.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
                pg.mixer.music.load('Sounds/ShootSound.mp3')
                pg.mixer.music.play()
        elif event.type == pg.KEYUP:
            """movement to the right"""
            if event.key == pg.K_d or event.key == pg.K_RIGHT:
                gun.move_right = False
            elif event.key == pg.K_a or event.key == pg.K_LEFT:
                gun.move_left = False


def screen_update(bg_color, screen, stats, sc, gun, aliens, bullets):
    """screen update"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    aliens.draw(screen)
    pg.display.flip()


def update_bullets(screen, stats, sc, aliens, bullets):
    """updating bullets positions"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pg.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_lives()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)


def gun_kill(stats, screen, sc, gun, aliens, bullets):
    """gun and aliens collision"""
    if stats.guns_loss > 1:
        stats.guns_loss -= 1
        pg.mixer.music.load('Sounds/DeathSound.mp3')
        pg.mixer.music.play()
        sc.image_lives()
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        gun.create_new_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        pg.mixer.music.load('Sounds/GameOverSound.mp3')
        pg.mixer.music.play()
        time.sleep(2)
        sys.exit()


def update_aliens(stats, screen, sc, gun, aliens, bullets):
    """updating aliens positions"""
    aliens.update()
    if pg.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, sc, gun, aliens, bullets)
    aliens_check(stats, screen, sc, gun, aliens, bullets)


def aliens_check(stats, screen, sc, gun, aliens, bullets):
    """checking if the aliens have reached the edge of the screen"""
    for alien in aliens.sprites():
        if alien.rect.bottom >= 700:
            gun_kill(stats, screen, sc, gun, aliens, bullets)
            break


def create_army(screen, aliens):
    """creating an alien army"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((1200 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2 * alien_height) / alien_height)

    for alien_row_number in range(number_alien_y - 5):
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + (alien_height * alien_row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * alien_row_number)
            aliens.add(alien)


def check_high_score(stats, sc):
    """checking new high scores"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('Scores/HighScore.txt', 'w') as fp:
            fp.write(str(stats.high_score))
