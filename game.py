import pygame, sys

# initiate pygame
pygame.init()
# clock method
clock = pygame.time.Clock()

# Main Window Setup
screen_width = 1200
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

while True:
    # Closes game upon user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # updates window
    pygame.display.flip()
    clock.tick(60)