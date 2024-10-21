import pygame
from pygame.sprite import Sprite
import objects.gun as gun


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        #TODO: implelemnt init
        pass

    def center_ship(self):
        """Center the ship on the screen."""
        pass

    def update(self):
        pass

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
