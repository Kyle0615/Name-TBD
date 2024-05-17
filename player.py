import pygame
import math
from settings import *
class Player:
   def __init__(self, x, y):
       self.x = x
       print(x)
       self.y = y
       print(y)
       super().__init__()
       self.image = pygame.image.load("player.png") #Loading player
       self.pos = pygame.math.Vector2(player_start_x, player_start_y)

       #Scaling
       self.rescale_image(self.image)
       self.image_size = self.image.get_size()
       self.speed = player_speed

   def rescale_image(self, image):
       self.image_size = self.image.get_size()
       scale_size = (self.image_size[0] * .4, self.image_size[1] * .4)
       self.image = pygame.transform.scale(self.image, scale_size)

       self.hitbox_rect = pygame.Rect((self.x, self.y), (self.image_size[0], self.image_size[1]))
       print(self.hitbox_rect)
       self.center = ((self.x + self.y / 2), (self.image_size[0] + self.image_size[1] / 2))
       print(self.center)
       self.rect = self.hitbox_rect.copy()

   def rotate_player(self):
       self.mouse_coords = pygame.mouse.get_pos() #Gets mouse coordinates.
       self.x_change_mouse_player_distance = (self.mouse_coords[0] - self.hitbox_rect)
       self.y_change_mouse_player_distance = (self.mouse_coords[1] - self.hitbox_rect)
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

       if self.velocity_x != 0 and self.velocity_y != 0: #CHECKS IF PLAYER IS GOING DIAGONALLY
           #When player moves diagonally it speeds up and instead of a velocity of 8 it has velocity of 8root2
           self.velocity_x = self.velocity_x / math.sqrt(2) #Divide x movement and y movement by root 2 so speed is 8
           self.velocity_y = self.velocity_y / math.sqrt(2)

   def move(self): #Moves player
       self.pos = self.pos + pygame.math.Vector2(self.velocity_x, self.velocity_y)

   def update(self):
       self.user_input() #Updates whenever player moves
       self.move()

