import pygame
import core.settings
from objects.alien import Alien
from objects.fleet import Fleet

# A classic example of factory. We encapsulate object creation duty in one class.
# By doing so, we can freely modify object creation without touching gameloop code


class FleetFactory:
    def __init__(self, settings: core.settings.Settings):
        self.settings = settings

    def get_number_aliens_x(self, alien_width):
        #TODO calculate number of aliens per row
        free_space = self.settings.screen_width - 2 * alien_width
        number_aliens = free_space // (alien_width * 2)

        return number_aliens

    def get_number_rows(self, ship_height, alien_height):
        #TODO calc free rows
        free_space = self.settings.screen_height - 3 * alien_height - ship_height
        
        number_rows = free_space // (alien_height * 2)
        

        return number_rows

    def create_alien(self, screen, aliens, col, row):
        alien = Alien(self.settings, screen)

        alien.x = alien.rect.width + 2 * alien.rect.width * col 
        alien.rect.x = alien.x 

        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row

        aliens.add(alien)
        

    def create_fleet(self, screen, ship, aliens: Fleet):
        alien = Alien(self.settings, screen)

        cols = self.get_number_aliens_x(alien.rect.width)
        rows = self.get_number_rows(ship.rect.height, alien.rect.height)

        for row in range(rows):
            for col in range(cols):
               self.create_alien(screen, aliens, col, row)
                

