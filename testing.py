import pygame
import math
from settings import *
class Test:
   def __init__(self, x, y):
       self.x = x
       self.y = y
       super().__init__()
       self.image = pygame.image.load("testing_dot.png") #Loading player
       self.pos = pygame.math.Vector2(player_start_x, player_start_y)

       #Scaling
       self.rescale_image(self.image)
       self.image_size = self.image.get_size()

   def rescale_image(self, image):
       self.image_size = self.image.get_size()
       scale_size = (self.image_size[0] * .4, self.image_size[1] * .4)
       self.image = pygame.transform.scale(self.image, scale_size)
