import pygame, sys

# initiate pygame
pygame.init()
# clock method
clock = pygame.time.Clock()

# Main Window Setup
screen_width = 1200
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height)) # returns display surface object
pygame.display.set_caption('Pong')      # gives window a title

while True:
    # Handles all user inputs
    for event in pygame.event.get():
        # Closes game upon user input (clicks X on top of screen)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # updates window
    pygame.display.flip()
    clock.tick(60) # limits how fast the loop runs (60fps)