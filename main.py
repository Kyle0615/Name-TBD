import pygame
import random
import math
from sys import exit
from settings import *
from player import Player
from game_objects import all_sprites_group, bullet_group


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
my_big_font = pygame.font.SysFont('Arial', 40)


#Creates the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("To be determined")
clock = pygame.time.Clock() #CONTROLS FRAME RATE


#Loading Images
p = Player(600, 200)
bg = pygame.image.load("ground.png")

welcome = "Welcome to ______!"
start_game = "Start Game!"
instructions = "Click here for game instructions."

first_click = False
time_left = 10
time_zero = 0
mode = "none"

display_start_game = my_font.render(start_game, True, (255, 0, 0))
display_welcome = my_font.render(welcome, True, (255, 0, 0))
display_instructions = my_big_font.render(instructions, True, (255, 0, 0))
display_time = my_font.render(str(round(time_left, 2)), True, (255, 255, 255))

run = True

while run:
    keys = pygame.key.get_pressed() #GETS ALL THE KEYS THE USER PRESSES
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
            exit()

    screen.blit(bg, (-1000, -1000))
    p.update()
    screen.blit(p.image, p.rect)

    all_sprites_group.update()
    all_sprites_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()
