import pygame
import objects.bullet as bullet
import math


# basically a bullet factory + strategy together
class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def create_bullet():
        raise NotImplementedError()


class ClassicGun(Gun):
    def __init__(self):
        super().__init__()

    def create_bullet(self, settings, screen, ship):
        pass


class DoubleGun(Gun):
    #TODO implement double gun
    pass


class SplitterGun(Gun):
    #TODO implement splitter gun
    pass


class PierceGun(Gun):
    #TODO implemnt Pierecgun
    pass


class SplitterPierceGun(Gun):
    #TODO implemnt splitterPierce gun
    pass
