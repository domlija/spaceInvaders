import pygame
import core.settings
from objects.alien import Alien

# A classic example of factory. We encapsulate object creation duty in one class.
# By doing so, we can freely modify object creation without touching gameloop code


class FleetFactory:
    def __init__(self, settings: core.settings.Settings):
        self.settings = settings

    def get_number_aliens_x(self, alien_width):
        #TODO calculate number of aliens per row
        pass

    def get_number_rows(self, ship_height, alien_height):
        #TODO calc free rows
        pass

    def create_alien(self, screen, aliens, col, row):
        #TODO: create aliens
        pass

    def create_fleet(self, screen, ship, aliens):
        #TODO add fleet creation
        pass