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
        stats: GameStats
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
                self.check_play_button(x,y)

    def check_play_button(self, x, y):
        clicked = self.play_button.rect.collidepoint(x, y)
        if clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            pygame.mouse.set_visible(False)

            self.stats.reset_stats()
            self.stats.game_active = True

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
        self.aliens.draw(self.screen)

        #TODO add scoreboard
        self.scoreboard.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()


        pygame.display.flip()

    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            #new_bullet = Bullet(self.settings, self.screen, self.ship)
            new_bullets = self.ship.gun.create_bullet(self.settings, self.screen, self.ship)
            self.bullets.add(*new_bullets)

    def update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        
        self.check_bullet_alien_collision()

    def check_highscore(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.scoreboard.prep_high_score()

    def check_bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        #TODO increase score

        if collisions:
            for bullet, aliens in collisions.items():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.scoreboard.prep_score()
                
                bullet.on_hit(self.bullets)
            self.check_highscore()



        if len(self.aliens) == 0:
            self.bullets.empty()
            self.settings.increase_speed()

            #TODO update scoreboard
            self.stats.level += 1
            self.scoreboard.prep_level()
            
            self.fleetFactory.create_fleet(self.screen, self.ship, self.aliens)

    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def ship_hit(self):
        #TODO add health check
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.scoreboard.prep_ships()
        else:
            self.stats.game_active = False 
            pygame.mouse.set_visible(True)
        
        self.aliens.empty()
        self.bullets.empty()

        self.fleetFactory.create_fleet(self.screen, self.ship, self.aliens)
        self.ship.center_ship()

        sleep(0.5)

    def check_fleet_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break 

    def update_aliens(self):
        self.check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()

        self.check_fleet_bottom()



