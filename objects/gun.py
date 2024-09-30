import pygame
import objects.bullet as bullet
import math


# basically a bullet factory + strategy together
class Gun(pygame.sprite.Sprite):
    def __init__(self ):
        super().__init__()

    
    def create_bullet():
        raise NotImplementedError()
    

class ClassicGun(Gun):
    def __init__(self):
        super().__init__()

    def create_bullet(self, settings, screen, ship):
        return [bullet.Bullet(settings, screen, ship)]
    
class DoubleGun(Gun):
    def __init__(self):
        super().__init__()

    def create_bullet(self, settings, screen, ship):
        return [bullet.Bullet(settings, screen, ship, math.radians(110)),
                bullet.Bullet(settings, screen, ship, math.radians(70))]
    
class SplitterGun(Gun):
    def create_bullet(self, settings, screen, ship):
        new_bullet = bullet.Bullet(settings, screen, ship)
        new_bullet = bullet.SplitterDecorator(new_bullet)
        return [new_bullet]
    
class PierceGun(Gun):
    def create_bullet(self, settings, screen, ship):
        new_bullet = bullet.Bullet(settings, screen, ship)
        new_bullet = bullet.PierceDecorator(new_bullet)
        return [new_bullet]
    
class SplitterPierceGun(Gun):
    def create_bullet(self, settings, screen, ship):
        new_bullet = bullet.Bullet(settings, screen, ship)
        new_bullet = bullet.PierceDecorator(new_bullet)
        new_bullet = bullet.SplitterDecorator(new_bullet)
        return [new_bullet]
        