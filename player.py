import pygame
from settings import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.pos = pygame.math.Vector2(player_start_x, player_start_y)
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.speed = player_speed

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .4, self.image_size[1] * .4)
        self.image = pygame.transform.scale(self.image, scale_size)

    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0 #sets up speed and movement of player

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]: #IF W KEY:
            self.velocity_y = -self.speed
        if keys[pygame.K_a]: #IF A KEY:
            self.velocity_x = -self.speed
        if keys[pygame.K_s]: #IF S KEY:
            self.velocity_y = self.speed
        if keys[pygame.K_d]: #IF D KEY:
            self.velocity_x = self.speed

    def move(self): #Moves player
        self.pos  = self.pos + pygame.math.Vector2(self.velocity_x, self.velocity_y)

    def update(self):
        self.user_input() #Updates whenever player moves
        self.move()