import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invation")

    ship = Ship(ai_setting, screen)
    bullets = Group()
    #alien = Alien(ai_setting, screen)
    aliens = Group()
    gf.create_aliens(ai_setting, screen, aliens, ship)

    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting, screen, ship, bullets, aliens)


run_game()
