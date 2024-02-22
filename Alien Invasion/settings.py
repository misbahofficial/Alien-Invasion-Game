class Settings:
    # a class to store all settings for Alien Invasion game

    def __init__(self):
        # initialize the game's settings

        # screen settings
        self.screen_width = 1200
        self.screen_height = 675
        self.bg_color = (51, 153, 255)

        # ship settings
        self.ship_speed_factor = 3.5

        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
