import pygame
import math
from settings import *
class Player:
    #THIS IS NEW3
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()
        self.image = pygame.image.load("player.png")  # Loading player
        self.base_player_image = self.image
        self.pos = pygame.math.Vector2(player_start_x, player_start_y)

        self.speed = player_speed
        self.rect = self.image.get_rect(center=(x, y)) #FINDS CENTER OF THE RECTANGLE
        self.image_size = self.image.get_size()
        self.base_player_image_size = self.base_player_image.get_size()
        self.rescale_image(self.image_size)

        self.shoot = False
        self.shoot_cooldown = 0

    def rescale_image(self, image):
        self.image_size = (int(self.image_size[0] * .5), int(self.image_size[1] * .5))
        self.base_player_image = pygame.transform.scale(self.base_player_image, self.image_size)
        self.hitbox_rect = self.image.get_rect(center=self.rect.center)

    def rotate_player(self):
        self.mouse_coords = pygame.mouse.get_pos()  # Gets mouse coordinates.
        self.x_change_mouse_player_distance = (self.mouse_coords[0] - self.rect.centerx) #Moves player according to
        self.y_change_mouse_player_distance = (self.mouse_coords[1] - self.rect.centery) #where the previous rectangle was
        self.angle = math.degrees(math.atan2(self.y_change_mouse_player_distance, self.x_change_mouse_player_distance))
        self.image = pygame.transform.rotate(self.base_player_image, -self.angle)
        self.rect = self.hitbox_rect.copy()

    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0  # sets up speed and movement of player

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:  # IF W KEY:
            self.velocity_y = -self.speed
        if keys[pygame.K_a]:  # IF A KEY:
            self.velocity_x = -self.speed
        if keys[pygame.K_s]:  # IF S KEY:
            self.velocity_y = self.speed
        if keys[pygame.K_d]:  # IF D KEY:
            self.velocity_x = self.speed

        if self.velocity_x != 0 and self.velocity_y != 0:  # CHECKS IF PLAYER IS GOING DIAGONALLY
            # When player moves diagonally it speeds up and instead of a velocity of 8 it has velocity of 8root2
            self.velocity_x = self.velocity_x / math.sqrt(2)  # Divide x movement and y movement by root 2 so speed is 8
            self.velocity_y = self.velocity_y / math.sqrt(2)

        if pygame.mouse.get_pressed() == (1,0, 0) or keys[pygame.K_SPACE]:
        #CHECKS IF USER LEFT CLICKS ON MOUSE OR CLICKS SPACE BAR
            self.shoot = True
            self.is_shooting()
        else:
            self.shoot = False

    def is_shooting(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = shoot_cooldown

    def move(self):  # Moves player
        self.pos = self.pos + pygame.math.Vector2(self.velocity_x, self.velocity_y)
        self.hitbox_rect.center = self.pos

    def update(self):
        if self.image_size[0] < 300:
            self.image_size = self.base_player_image_size
        self.user_input()  # Updates whenever player moves
        self.move()
        self.rotate_player()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown = self.shoot_cooldown - 1

