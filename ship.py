import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect.
        self.image = pygame.image.load('images/ship.bmp')
        # <a href='https://www.freepik.com/photos/independence-day'>Independence day photo created by kjpargeter - www.freepik.com</a>
        self.rect = self.image.get_rect()

        # Start each new ship at the middle left of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's vertical position.
        self.y = float(self.rect.y)

        #Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's y value, not the rect. 
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: 
            self.y += self.settings.ship_speed

        # Update rect object from self.y.
        self.rect.y = self.y
        

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
