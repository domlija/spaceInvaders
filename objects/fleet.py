from typing import Any, Iterable
import pygame
from core.settings import Settings 
from pygame.sprite import AbstractGroup

class Fleet(pygame.sprite.Group):
    def __init__(self, settings: Settings , screen: pygame.surface.Surface, *sprites: Any | AbstractGroup | Iterable) -> None:
        super().__init__(*sprites)
        self.screen = screen
        self.settings = settings

    def check_edges(self):
        for alien in self.sprites():
            if alien.check_edges():
                return True
        
        return False
    
    def check_bottom(self):
        screen_rect = self.screen.get_rect()

        for alien in self.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                return True 

        return False
    
    def change_direction(self):
        print(self.settings.fleet_direction)
        self.settings.fleet_direction *= -1
        print(self.settings.fleet_direction)

        for alien in self.sprites():

            alien.rect.y += self.settings.fleet_drop_speed



        
