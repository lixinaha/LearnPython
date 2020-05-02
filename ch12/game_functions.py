import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                check_keydown_event(event, ship)
            elif event.type == pygame.KEYUP:
                check_key_up_event(event, ship)

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()

def check_key_up_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_keydown_event(event, ship):
    if event.key == pygame.K_RIGHT:
        # ship.rect.centerx += 1
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True