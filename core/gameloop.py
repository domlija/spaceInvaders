from time import sleep
from typing import List
import pygame
from objects.ship import Ship
from objects.alien import Alien
from objects.bullet import Bullet
from objects.button import Button
import objects.gun as gun
from objects.scoreborad import Scoreboard
from core.game_stats import GameStats
import sys
import core.settings
from core.fleetFactory import FleetFactory


class GameLoop:
    def __init__(
        self,
        settings: core.settings.Settings,
        screen,
        ship: Ship,
        aliens: pygame.sprite.Group,
        bullets: pygame.sprite.Group,
        play_button: Button,
        scoreboard: Scoreboard,
        stats: GameStats,
    ):

        self.settings = settings
        self.screen = screen
        self.ship = ship
        self.aliens = aliens
        self.bullets = bullets
        self.fleetFactory = FleetFactory(settings)
        self.play_button = play_button
        self.scoreboard = scoreboard
        self.stats = stats

    def check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_1:
            self.ship.gun = gun.ClassicGun()
        elif event.key == pygame.K_2:
            self.ship.gun = gun.DoubleGun()
        elif event.key == pygame.K_3:
            self.ship.gun = gun.SplitterGun()
        elif event.key == pygame.K_4:
            self.ship.gun = gun.PierceGun()
        elif event.key == pygame.K_5:
            self.ship.gun = gun.SplitterPierceGun()

    def check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.check_play_button(x, y)

    def check_play_button(self, x, y):
        clicked = self.play_button.rect.collidepoint(x, y)
        if clicked :
            self.settings.initialize_dynamic_settings()
            pygame.mouse.set_visible(False)

            self.stats.reset_stats()

            #TODO: set game_stats.is_active to true
            self.stats.game_active =True

            

            self.scoreboard.prep_high_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_score()
            self.scoreboard.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self.fleetFactory.create_fleet(self.screen, self.ship, self.aliens)
            self.ship.center_ship()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets:
            bullet.draw_bullet()
        self.ship.blitme()

        #TODO add alien drawing
        

        # TODO add scoreboard
        self.scoreboard.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            # new_bullet = Bullet(self.settings, self.screen, self.ship)
            new_bullets = self.ship.gun.create_bullet(
                self.settings, self.screen, self.ship
            )
            print(new_bullets)
            self.bullets.add(*new_bullets)

    def update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if (
                bullet.rect.bottom <= 0
                or bullet.rect.left < 0
                or bullet.rect.right > self.settings.screen_width
            ):
                self.bullets.remove(bullet)

        self.check_bullet_alien_collision()

    def check_highscore(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score

            #TODO: draw new high score
            

            # We can think of scoreboard.prep_high_score as a crude listener mechanism.
            # In general case we would iterate over some collection of high score listeners 
            # and call their prep_high_score methods. In case the scoreboard has no direct reference 
            # to stats we could pass it as an argument.

    def check_bullet_alien_collision(self):
        #TODO: check if bullet hit any alien
        pass

    def check_fleet_edges(self):
        #TODO: check if the fleet touched an edge
        pass

    def change_fleet_direction(self):
        #TODO: implement changing fleet direction
        pass

    def ship_hit(self):

        if self.stats.ships_left > 0:
            #TODO: update ships_left stats
            pass

            #TODO update new ships(lives) on screen
            
            # Again the same crude listener pattern. In this case
            # we notify the ships (in-game lives) listener.
            
        else:
            #TODO end the game and show mouse
            pass

        self.aliens.empty()
        self.bullets.empty()

        #TODO: create new fleet

        self.ship.center_ship()

        sleep(0.5)

    def check_fleet_bottom(self):
        #TODO: add logic to check if fleet came to the bottom
        pass

    def update_aliens(self):
        #TODO: add logic to update fleet movement


        # This is a basic composite example. Even though we didn't implement
        # pygame.sprite.Group it functions as a basic composite pattern
        # Instead of knowing how each alien (but in more general case each sprite subclass) updates
        # It calls update method of each individual sprite subclass. In more rigid languages
        # group and sprite should implement the same interface (in this case Updatable)
        # but that is not necessary when working with dynamic languages.

        pass

        
