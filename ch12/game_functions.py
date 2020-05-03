import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                
            sys.exit(0)            
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_event(event, ship)

def update_screen(ai_settings, screen, ship, bullets, aliens):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw()
    aliens.draw(screen)
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
    elif event.key == pygame.K_q:
        sys.exit(0)

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

def create_aliens(ai_setting, screen, aliens, ship):
    alien = Alien(ai_setting, screen)    
    count_x = get_count_x(ai_setting, alien.rect.width)
    row_numbers = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)
    for row_number in range(row_numbers):
        for alien_number in range(count_x):
            create_alien(ai_setting, screen, aliens, alien_number, row_number)

def get_count_x(ai_setting, alien_width):
    available_space_x = ai_setting.screen_width - 2* alien_width
    count_x = int(available_space_x/(2*alien_width))
    return count_x

def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    alien = Alien(ai_setting, screen)    
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number    
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_setting, ship_height, alien_height):
    available_space_y = (ai_setting.screen_height - 3*alien_height - ship_height)
    number_rows = int(available_space_y/(2*alien_height))    
    return number_rows

def update_aliens(aliens, ai_setting):
    check_aliens_edge(ai_setting, aliens)
    aliens.update()

def check_aliens_edge(ai_setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_aliens_direction(ai_setting, aliens)
            break
    
def change_aliens_direction(ai_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.aliens_drop_speed
        
    ai_setting.aliens_direction *= -1