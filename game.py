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

### Game Rectangles ###

# Creates a ball in the center 30px wide and 30 px high
ball = pygame.Rect(screen_width/2 - 15 ,
                   screen_height/2 - 15 ,
                   30, 30) 

# Creates a player in the center right 10px wide and 140 px high
player = pygame.Rect(screen_width - 20, 
                     screen_height/2 - 70, 
                     10, 140)

# Creates an opponent in the center left 10px wide and 140 px high
opponent = pygame.Rect(10, screen_height/2 - 70, 
                       10, 140)


### Establishes Global Colors ###
grey = pygame.Color('grey12')
light_grey = (200, 200, 200)

### Establishes the speed of the ball ###
ball_speed_x = 5
ball_speed_y = 5

while True:
    # Handles all user inputs
    for event in pygame.event.get():
        # Closes game upon user input (clicks X on top of screen)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Animations for ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball play area (ensures the ball doesn't go out of the display)
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    
    # Ball collisions on rectangles
    if ball.collidedict(player) or ball.collidedict(opponent):
        ball_speed_x *= -1

    # Visuals -> Colors in the rectangles and screen
    screen.fill(grey) # The entire screen background
    pygame.draw.rect(screen, light_grey, player) # player
    pygame.draw.rect(screen, light_grey, opponent) # opponent
    pygame.draw.ellipse(screen, light_grey, ball) # ball (circle)

    pygame.draw.aaline(screen, light_grey, 
                       # x coord      y coord            
                       (screen_width/2, 0), (screen_width/2, screen_height)) # draws the center line for the game

    # updates window    
    pygame.display.flip()
    clock.tick(60) # limits on how fast the loop runs (60fps)
