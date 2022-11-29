import pygame

class Settings:
    '''A class to store settings'''

    def __init__(self):
        '''Initialize the game's settings'''
        
        # Screen settings
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.bg_color = (255, 255, 255)
        self.ship_speed = 10
        self.bg_image = pygame.image.load('images/background.bmp')


        #bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 500
        self.bullet_height = 30
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        #alien settings
        self.alien_speed = 20
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        self.ship_limit = 2
