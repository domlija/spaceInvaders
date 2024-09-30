from typing import Any
import pygame
import math
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship, angle=math.radians(90)):
        """Create a bullet object, at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        self.settings = ai_settings
        self.ship = ship

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.angle = angle

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor * math.sin(self.angle)
        self.x += self.speed_factor * math.cos(self.angle)

        if math.cos(self.angle) < 0:
            print(self.x, self.y)

        # Update the rect position.
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def on_hit(self, bullets):
        pass


class SplitterDecorator(Bullet):

    def __init__(self, bullet: Bullet):
        self._bullet = bullet

    def __getattr__(self, name):
        """
        If an attribute is not found on the decorator, it delegates the lookup to the wrapped bullet.
        """
        return getattr(self._bullet, name)

    def __setattr__(self, name, value):
        # Delegate attribute setting to the wrapped bullet
        if name == "_bullet":
            # Allow setting the wrapped bullet itself
            super().__setattr__(name, value)
        else:
            setattr(self._bullet, name, value)

    def on_hit(self, bullets):
        left_bullet = Bullet(self.settings, self.screen, self.ship, math.radians(0))
        left_bullet.rect = self.rect.copy()
        left_bullet.y = self.y
        left_bullet.x = self.x

        right_bullet = Bullet(self.settings, self.screen, self.ship, math.radians(180))
        right_bullet.rect = self.rect.copy()
        right_bullet.y = self.y
        right_bullet.x = self.x

        bullets.add(*[left_bullet, right_bullet])

        self._bullet.on_hit(bullets)


class PierceDecorator(Bullet):
    def __init__(self, bullet: Bullet):
        self._bullet = bullet

        print(self.y)

    def __getattr__(self, name):
        """
        If an attribute is not found on the decorator, it delegates the lookup to the wrapped bullet.
        """
        return getattr(self._bullet, name)

    def __setattr__(self, name, value):
        # Delegate attribute setting to the wrapped bullet
        if name == "_bullet":
            # Allow setting the wrapped bullet itself
            super().__setattr__(name, value)
        else:
            setattr(self._bullet, name, value)

    def on_hit(self, bullets):
        new_bullet = Bullet(self.settings, self.screen, self.ship, self.angle)
        new_bullet.rect = self.rect.copy()
        new_bullet.y = self.y
        new_bullet.x = self.x

        bullets.add(new_bullet)

        self._bullet.on_hit(bullets)
