import pygame
from pygame.sprite import Sprite
import objects.gun as gun
import core.settings as settingsType


class Ship(Sprite):
    def __init__(self, ai_settings: settingsType, screen):
        """Initialize the ship, and set its starting position."""
        super().__init__()
        self.screen = screen
        
        self.settings = ai_settings

        self.image = pygame.image.load('assets/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom 

        self.center = float(self.rect.centerx)

        self.moving_left = False
        self.moving_right = False 

        self.gun = gun.ClassicGun()    

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.width:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center
 

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
