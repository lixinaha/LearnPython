import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from button import Button
from ship import Ship

def check_events(ai_settings, screen, ship, bullets, state, play_button, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            check_play_button(state, play_button, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship)

def check_play_button(state, play_button, mouse_x, mouse_y, aliens, bullets, ai_setting, screen, ship):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not state.game_active:
        ai_setting.init_dynamic_setting()
        pygame.mouse.set_visible(False)
        state.reset()
        state.game_active = True
        aliens.empty()
        bullets.empty()
        create_aliens(ai_setting, screen, aliens, ship)
        ship.center_ship()


def update_screen(ai_settings, screen, ship: Ship, bullets, aliens, state, play_button: Button):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw()
    aliens.draw(screen)
    if not state.game_active:
        play_button.draw_button()
    
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


def update_bullets(bullets, aliens, screen, ship, ai_setting):
    bullets.update()
    for b in bullets.copy():
        if b.rect.bottom <= 0:
            bullets.remove(b)
    # print(str(len(bullets)))
    check_bullet_alien_collisions(ai_setting, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_setting, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()
        create_aliens(ai_setting, screen, aliens, ship)


def fire_bullet(ai_setting, screen, ship, bullets):
    if (len(bullets) < ai_setting.bullet_max):
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def create_aliens(ai_setting, screen, aliens, ship):
    alien = Alien(ai_setting, screen)
    count_x = get_count_x(ai_setting, alien.rect.width)
    row_numbers = get_number_rows(
        ai_setting, ship.rect.height, alien.rect.height)
    for row_number in range(row_numbers):
        for alien_number in range(count_x):
            create_alien(ai_setting, screen, aliens, alien_number, row_number)


def get_count_x(ai_setting, alien_width):
    available_space_x = ai_setting.screen_width - 2 * alien_width
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
    available_space_y = (ai_setting.screen_height -
                         3*alien_height - ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows


def update_aliens(aliens, ai_setting, ship, state, screen, bullets):
    check_aliens_edge(ai_setting, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, state, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_setting, state, screen, ship, aliens, bullets)


def check_aliens_edge(ai_setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_aliens_direction(ai_setting, aliens)
            break


def change_aliens_direction(ai_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.aliens_drop_speed
    ai_setting.aliens_direction *= -1


def ship_hit(ai_setting, state, screen, ship, aliens, bullets):
    if state.ship_left > 0:
        state.ship_left -= 1
        aliens.empty()
        bullets.empty()
        create_aliens(ai_setting, screen, aliens, ship)
        ship.center_ship()
        sleep(1)
    else:
        state.game_active = False
        pygame.mouse.set_visible(True)
        print("game over!")

def check_aliens_bottom(ai_setting, state, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, state, screen, ship, aliens, bullets)
            break
