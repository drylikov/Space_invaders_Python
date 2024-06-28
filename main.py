from tkinter import S
import pygame
from ship import Ship
import control
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("space invaders")
    bg_color = (14, 21, 37)
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    control.generate_aliens(screen, aliens)

    while True:
        control.events(screen, ship, bullets)
        ship.ship_position()
        control.screen_update(bg_color, screen, ship, aliens, bullets)
        control.bullets_manage(bullets)
        control.update_aliens(aliens)


run()