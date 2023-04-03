import pygame, sys, random

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
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

# Ball animations
def ball_animation():
    # Set speed of ball as global variables (to be used in while loop)
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball play area (ensures the ball doesn't go out of the display)
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    
    # Ball collisions on rectangles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

# Player paddle animations
def player_animation():
    # Moves player paddle 
    player.y += player_speed

    # Ensures player paddle doesn't leave the frame
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

# Opponent paddle animation
def opponent_animation():
    # Moves player paddle based on ball position
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    # Ensures opponent paddle doesn't leave the frame
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

# Resets ball every time the ball hits frame
def ball_restart():
    global ball_speed_x, ball_speed_y

    # Centers ball
    ball.center = (screen_width/2, screen_height/2)

    # Sends ball to move in random direction
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

while True:
    # Handles all user inputs
    for event in pygame.event.get():
        # Closes game upon user input (clicks X on top of screen)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Detects when a key is pushed down
        if event.type == pygame.KEYDOWN:
            # Move player paddle down if the down arrow is pressed
            if event.key == pygame.K_DOWN:
                player_speed +=7
            # Move player paddle up if the up arrow is pressed
            if event.key == pygame.K_UP:
                player_speed -=7
        # Detects when a key is released
        if event.type == pygame.KEYUP:
            # Stops movement of paddle
            if event.key == pygame.K_DOWN:
                player_speed -=7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()

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
