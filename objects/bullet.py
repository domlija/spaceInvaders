from typing import Any
import pygame
import math
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship, angle=math.radians(90)):
        """Create a bullet object, at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.settings = ai_settings
        self.ship = ship 
        self.angle = angle

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = self.settings.bullet_color
        self.speed = self.settings.bullet_speed_factor


    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y += self.speed * math.sin(self.angle)
        self.x += self.speed * math.cos(self.angle)

        self.rect.x = int(self.x)
        self.rect.y = self.y 

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
