## Import data
import pygame
import os
import random
from pygame.locals import *

## Load assets

## Config
# Config value
BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Set window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision Demo")


## Main
# create main rectangle and obstacle rectangle
obstacles = []
for _ in range(16):
    obstacles.append(
        pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
    )

# main flow
running = True
line_start = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

while running:
    # update background
    screen.fill(BG)

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            running = False

    color = GREEN
    position = pygame.mouse.get_pos()

    # draw line
    pygame.draw.line(screen, WHITE, line_start, position, 5)

    for obstacle in obstacles:
        if obstacle.clipline((line_start, position)):
            pygame.draw.rect(screen, RED, obstacle)
        else:
            pygame.draw.rect(screen, GREEN, obstacle)

    # Update the display
    pygame.display.flip()
pygame.quit()
