import pygame 
from core.settings import Settings
from objects.ship import Ship
from objects.button import Button
from core.gameloop import GameLoop
from core.settings import Settings
from core.game_stats import GameStats
from objects.scoreborad import Scoreboard


def main():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    pygame.display.set_caption('Alien Invasion')

    play_button = Button(settings, screen, "Play")

    stats = GameStats(settings)
    scoreboard = Scoreboard(settings, screen, stats)

    ship = Ship(settings, screen)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()

    bg_color = (230, 230, 230)
    game_loop = GameLoop(settings, screen, ship,aliens, bullets, play_button, scoreboard, stats)

    game_loop.fleetFactory.create_fleet(screen, ship, aliens)

    while True:
        game_loop.check_events()
        
        
        if True:
            ship.update()
            game_loop.update_bullets()
            game_loop.update_aliens()

        game_loop.update_screen()



if __name__ == '__main__':
    main()