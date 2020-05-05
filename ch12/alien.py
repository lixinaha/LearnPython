import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    def __init__(self, ai_setting: Settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load("./ch12/images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)        

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_setting.alien_speed_factor * self.ai_setting.aliens_direction)
        self.rect.x = self.x

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
