from re import A
import pygame
import sys
from bullet import Bullet
from alien import Alien

def events(screen, ship, bullets):
    # Handling Game Events

    # close game window
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # ship move
            elif event.type == pygame.KEYDOWN:
                # movement to the right
                if event.key == pygame.K_d:
                    ship.mright = True
                # movement to the left
                elif event.key == pygame.K_a:
                    ship.mleft = True
                # fire 
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, ship)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                # movement to the right
                if event.key == pygame.K_d:
                    ship.mright = False
                # movement to the left
                elif event.key == pygame.K_a:
                    ship.mleft = False

def screen_update(bg_color, screen, ship, aliens, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.bullet_render()
    ship.render()
    aliens.draw(screen)
    pygame.display.flip()

def bullets_manage(bullets):
    # delete old bullets and manage all bullets
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_aliens(aliens):
    # update alien's position
    aliens.update()

def generate_aliens(screen, aliens):
    # generate aliens
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2 * alien_height) / alien_height)

    for row_number in range(number_alien_y - 1):
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + (alien_height * row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * row_number)
            aliens.add(alien)