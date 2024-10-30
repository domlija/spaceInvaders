import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = ai_settings

        self.image = pygame.image.load('assets/alien.png')
        self.rect = self.image.get_rect()

        #self.rect.x = self.rect.width
        #self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        if self.rect.left < 0 or self.rect.right > self.settings.screen_width:
            return True
        
        return False

    def update(self):
        """Move the alien right or left."""
        pass

    def blitme(self):
        """Draw the alien at its current location."""
        print(self.rect)
        self.screen.blit(self.image, self.rect)
