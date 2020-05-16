import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_state import GameState
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invation")
    play_button = Button(ai_setting, screen, "Play")

    ship = Ship(ai_setting, screen)
    bullets = Group()
    #alien = Alien(ai_setting, screen)
    aliens = Group()
    gf.create_aliens(ai_setting, screen, aliens, ship)

    state = GameState(ai_setting)
    board = Scoreboard(ai_setting, screen, state)

    while True:
        gf.check_events(ai_setting, screen, ship, bullets, state, play_button, aliens)
        if state.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, screen, ship, ai_setting, board, state)
            gf.update_aliens(aliens, ai_setting, ship, state, screen, bullets)
        else:
            aliens.empty()
            gf.create_aliens(ai_setting, screen, aliens, ship)    
        gf.update_screen(ai_setting, screen, ship, bullets, aliens, state, play_button, board)

run_game()
