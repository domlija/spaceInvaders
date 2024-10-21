import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        pass

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        pass

    def update(self):
        """Move the alien right or left."""
        pass

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
