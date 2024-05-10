import pygame
import random
import time
from targetcircle import Targetcircle

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
my_big_font = pygame.font.SysFont('Arial', 40)
#pygame.display.set_caption("")

size = (800, 600)
screen = pygame.display.set_mode(size)
score = 0

instructions = "Welcome to ______!"
target = Targetcircle(100, 100)
first_click = False
start_time = time.time()
time_left = 10
time_zero = 0

display_score = my_font.render(("Score: " + str(score)), True, (255, 0, 0))
display_instructions = my_big_font.render(instructions, True, (255, 0, 0))
display_time = my_font.render(str(round(time_left, 2)), True, (255, 255, 255))

first_click = False
run = True

while run:
    if first_click:
        screen.fill(255,255,255)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.KEYDOWN and first_click == False:
            current_time = time.time()
            display_instructions_screen = False
            first_click = True

        if first_click:
            screen.blit(display_score, (0,50))
            if time_left > 0 and first_click:
                start_time = time.time()
                time_left = 10 - (start_time - current_time)
                display_time = my_font.render(str(round(time_left, 2)), True, (255, 255, 255)

            if time_left <= 0:
                display_time = my_font.render(str(time_zero), True, (255, 255, 255))


        else:
            screen.blit(display_instructions, (172, 200))
            pygame.display.update()

pygame.quit()