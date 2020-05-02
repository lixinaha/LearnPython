import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                check_keydown_event(event, ai_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_key_up_event(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw()
    pygame.display.flip()

def check_key_up_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_keydown_event(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:        
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)

def update_bullets(bullets):
    bullets.update()
    for b in bullets.copy():
        if b.rect.bottom <= 0:
            bullets.remove(b)
    # print(str(len(bullets)))

def fire_bullet(ai_setting, screen, ship, bullets):
        if (len(bullets) < ai_setting.bullet_max):
            new_bullet = Bullet(ai_setting, screen, ship)
            bullets.add(new_bullet)