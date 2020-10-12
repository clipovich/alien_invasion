class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.bg_color = (199, 193, 245)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 4.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = .5
        self.fleet_drop_speed = 10
        self.alien_hit_limit = 3
        # fleet_direction of 1 represents down; -1 represents up.
        self.fleet_direction = 1
