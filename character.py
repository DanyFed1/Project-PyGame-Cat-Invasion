import pygame
import os

class Girl:
    """A class to maange player controlled character - girl"""
    
    def __init__(self, ai_game):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        """Initialize the character and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings 
        
        #Load the girl image and get its rect
        image_path = os.path.join(self.base_dir, 'assets/Game images/rcIaniCpy5NCWgUYcK2r-1-sb7rx-_1_.bmp')
        self.image = pygame.image.load(image_path)
        # Resize the image
        self.image = pygame.transform.scale(self.image, (80, 80))  # Set new dimensions (width, height)
        self.rect = self.image.get_rect() #pygame treats objects as rectangles which 
        #simplifies the collision registration
        
        #Start each new girl at the bottom center of the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #Store a float for the girl's exact horizontal position.
        self.x = float(self.rect.x)
        
        #Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ship's position based on the movement flag."""
        #Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right: #Makes sure not to go outside screen
            self.x += self.settings.girl_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.girl_speed
        
        #Update rect object from self.x
        self.rect.x = self.x
        
    def blitme(self):
        """Draw the girl at its current location."""
        self.screen.blit(self.image, self.rect)
        
    def center_character(self):
        """Position character at the center of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
    def resize(self, width, height):
        """Resize the image. for the screen dimensions"""
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom