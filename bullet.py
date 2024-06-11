import pygame
import math
from settings import *

class Bullet(pygame.sprite.Sprite):
 def __init__(self, x, y, angle):
     super().__init__()
     self.image = pygame.Surface((10,5))
     self.image.fill((255,255,255))
     self.image = pygame.transform.rotozoom(self.image,0, bullet_scale) #Scales the bullet
     self.rect = self.image.get_rect(center=(x,y))
     self.x = x
     self.y = y
     self.angle = angle
     self.speed = bullet_speed
     self.x_velocity = math.cos(self.angle * (2*math.pi/360)) * self.speed #uses radians
     self.y_velocity = math.sin(self.angle * (2*math.pi/360)) * self.speed
     self.bullet_lifetime = bullet_lifetime
     self.spawn_time = pygame.time.get_ticks() #GETS THE TIME THE BULLET WAS CREATED

 def bullet_movement(self):
     self.x = self.x + self.x_velocity
     self.y = self.y + self.y_velocity

     self.rect.x = int(self.x)
     self.rect.y = int(self.y)

     if pygame.time.get_ticks() - self.spawn_time > self.bullet_lifetime:
         self.kill() #removes bullet if on screen more thatn 750 ms

 def update(self):
     self.bullet_movement()
