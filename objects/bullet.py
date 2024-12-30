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
        
        self.y -= self.speed * math.sin(self.angle)
        self.x += self.speed * math.cos(self.angle)

        self.rect.x = int(self.x)
        self.rect.y = self.y 

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def on_hit(self, bullets):
        pass


class SplitterDecorator(Bullet):
    def __init__(self, bullet: Bullet):
        self._bullet = bullet

    def __getattr__(self, name):
        
        return getattr(self._bullet, name)
    
    def __setattr__(self, name: str, value: Any):
        if name == '_bullet':
            super().__setattr__(name, value)
        else:   
            setattr(self._bullet, name, value)
            

            

    def on_hit(self, bullets):
        left_bullet = Bullet(self.settings, self.screen, self.ship, math.radians(180))
        left_bullet.rect = self.rect.copy()

       
        left_bullet.rect.x = self.x
        left_bullet.rect.y = self.y
        left_bullet.x = self.x 
        left_bullet.y = self.y
        

        right_bullet = Bullet(self.settings, self.screen, self.ship, math.radians(0))
        right_bullet.rect = self.rect.copy()
        right_bullet.rect.x = self.x
        right_bullet.rect.y = self.y
        right_bullet.x = self.x 
        right_bullet.y = self.y

        bullets.add(*[left_bullet, right_bullet])

        self._bullet.on_hit(bullets)



class PierceDecorator(Bullet):
    def __init__(self, bullet: Bullet):
        self._bullet = bullet

    def __getattr__(self, name):
        
        return getattr(self._bullet, name)
    
    def __setattr__(self, name: str, value: Any):
        if name == '_bullet':
            super().__setattr__(name, value)
        else:   
            setattr(self._bullet, name, value)

    def on_hit(self, bullets):
        bullet = Bullet(self.settings, self.screen, self.ship, self.angle)
        bullet.rect = self.rect 
        bullet.x = self.x 
        bullet.y = self.y
        
        bullets.add(*[bullet])

        self._bullet.on_hit(bullets)
