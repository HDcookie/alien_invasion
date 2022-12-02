import pygame


class Settings:
    '''A class to store settings'''

    def __init__(self):
        '''Initialize the game's settings'''

        # Screen settings
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.ship_limit = 2

        self.bg_color = (255, 255, 255)
        self.bg_image = pygame.image.load('images/background.bmp')

        # bullet settings
        self.bullet_width = 1000
        self.bullet_height = 30
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.7

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 5
        self.bullet_speed = 3.0
        self.alien_speed = 3

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50
        self.high_score = 0



    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
