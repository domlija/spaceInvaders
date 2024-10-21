from typing import Any
import pygame
import math
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship, angle=math.radians(90)):
        """Create a bullet object, at the ship's current position."""
        pass

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        pass

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def on_hit(self, bullets):
        pass


class SplitterDecorator(Bullet):
    #TODO: implement splitter decorator
    pass


class PierceDecorator(Bullet):
    #TODO: implement splitter decorator
    pass
