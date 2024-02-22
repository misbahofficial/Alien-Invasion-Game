import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)

    # make an alien object
    alien = Alien(ai_settings, screen)

    # make a group to store bullets in
    bullets = Group()
    # make a group of aliens
    aliens = Group()

    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the game
    while True:
        # watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        # update the ship based on key events
        ship.update()
        gf.update_bullets(bullets)
        # gf.update_aliens(ai_settings, aliens)
        # redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


# run the game
if __name__ == "__main__":
    run_game()
