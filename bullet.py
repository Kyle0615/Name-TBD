import pygame
import math
from settings import *

class Bullet():
 def __init__(self, x, y, angle):
     super().__init__()
     self.image = pygame.image.load("bullet.png")
     self.image = pygame.transform.rotozoom(self.image,0, bullet_scale) #Scales the bullet
     self.rect = self.image.get_rect()
     self.rect.center = (x, y)
     self.angle = angle
     self.y = y
     self.x = x
     self.speed = bullet_speed
     self.x_velocity = math.cos(self.angle * (2*math.pi/360)) * self.speed #uses radians
     self.y_velocity = math.sin(self.angle * (2*math.pi/360)) * self.speed


 def bullet_movement(self):
     self.x = self.x + self.x_velocity
     self.y = self.y + self.y_velocity


     self.rect.x = int(self.x)
     self.rect.y = int(self.y)


 def update(self):
     self.bullet_movement()
