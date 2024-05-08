import pygame
import random
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

display_score = my_font.render(("Score: " + str(score)), True, (255, 0, 0))
display_instructions = my_big_font.render(instructions, True, (255, 0, 0))

first_click = False
run = True

while run:
    if first_click:
        #screen.blit(target.image, target.rect)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.KEYDOWN and first_click == False:
            display_instructions_screen = False
            first_click = True

        if first_click:
            pygame.quit()

        else:
            screen.blit(display_instructions, (172, 200))
            pygame.display.update()

pygame.quit()