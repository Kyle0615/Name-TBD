import pygame
import random
import math
from sys import exit
from settings import *
from player import Player

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
bg = pygame.transform.scale(pygame.image.load("backround.png"), (width, height)) #Scales the backround up to our window
p = Player(player_start_x, player_start_y)

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

first_click = False
run = True

while run:
    keys = pygame.key.get_pressed() #GETS ALL THE KEYS THE USER PRESSES
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
            exit()

        if event.type == pygame.KEYDOWN and first_click == False:
            display_instructions_screen = False

        screen.blit(bg, (0,0))
        #screen.blit(display_welcome, (172, 200))
        #screen.blit(display_start_game, (172, 230))
        #screen.blit(display_instructions, (172, 250))
        screen.blit(p.image, p.pos)
        p.update()

        pygame.display.update()
        clock.tick(FPS)

pygame.quit()