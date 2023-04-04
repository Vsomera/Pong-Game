import pygame
import sys
import random

# initiate pygame
pygame.init()
# clock method
clock = pygame.time.Clock()

# Main Window Setup
screen_width = 1200
screen_height = 960

# returns display surface object
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')      # gives window a title

### Establishes Global Colors ###
grey = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Points class
class Points:
    # Keeps track of points for opponent and player
    player_points = 0
    opponent_points = 0

    def add_player_point(self):
        # Adds 1 point to player when called
        Points.player_points += 1

    def add_opponent_point(self):
        # Adds 1 point to opponent when called
        Points.opponent_points += 1
    
# Animations class
class Animations:
    def __init__(self, screen_width, screen_height):
        # Creates ball, player and opponent rectangles
        self.ball = pygame.Rect(screen_width/2 - 15,
                                screen_height/2 - 15,
                                30, 30)
        self.player = pygame.Rect(screen_width - 20,
                                screen_height/2 - 70,
                                10, 140)
        self.opponent = pygame.Rect(10, screen_height/2 - 70,
                                    10, 140)

        # Sets default speed for ball, player and opponent
        self.ball_speed_x = 7 * random.choice((1, -1))
        self.ball_speed_y = 7 * random.choice((1, -1))
        self.ball_speed_y = 7
        self.player_speed = 0
        self.opponent_speed = 7

    # Ball animation
    def ball_animation(self):
        # Set speed of ball (to be used in while loop)
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        # Ball play area (ensures the ball doesn't go out of the display)
        if self.ball.top <= 0 or self.ball.bottom >= screen_height:
            self.ball_speed_y *= -1

        # Adds points to points class and resets ball
        if self.ball.left <= 0:
            # adds one point to player
            Points.add_player_point(self)
            self.ball_restart()
        
        if self.ball.right >= screen_width:
            # adds one point to opponent
            Points.add_opponent_point(self)
            self.ball_restart()

        # Ball collisions on rectangles
        if self.ball.colliderect(self.player) or self.ball.colliderect(self.opponent):
            self.ball_speed_x *= -1

    # Player paddle animations
    def player_animation(self):
        # Moves player paddle
        self.player.y += self.player_speed

        # Ensures player paddle doesn't leave the frame
        if self.player.top <= 0:
            self.player.top = 0
        if self.player.bottom >= screen_height:
            self.player.bottom = screen_height

    # Opponent paddle animation
    def opponent_animation(self):
        # Moves player paddle based on ball position
        if self.opponent.top < self.ball.y:
            self.opponent.top += self.opponent_speed
        if self.opponent.bottom > self.ball.y:
            self.opponent.bottom -= self.opponent_speed

        # Ensures opponent paddle doesn't leave the frame
        if self.opponent.top <= 0:
            self.opponent.top = 0
        if self.opponent.bottom >= screen_height:
            self.opponent.bottom = screen_height

    # Resets ball every time the ball hits frame
    def ball_restart(self):
        # Centers ball
        self.ball.center = (screen_width/2, screen_height/2)

        # Sends ball to move in random direction
        self.ball_speed_y *= random.choice((1, -1))
        self.ball_speed_x *= random.choice((1, -1))

# Starts game
class Game:
    def __init__(self, Animations, screen_width, screen_height):
        # Declares Animations class and resets ball position
        self.Animations = Animations(screen_width, screen_height)
        self.Animations.ball_restart()

    def run(self):
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
                        self.Animations.player_speed += 7
                    # Move player paddle up if the up arrow is pressed
                    if event.key == pygame.K_UP:
                        self.Animations.player_speed -= 7
                # Detects when
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.Animations.player_speed -= 7
                    if event.key == pygame.K_UP:
                        self.Animations.player_speed += 7

            self.Animations.ball_animation()
            self.Animations.player_animation()
            self.Animations.opponent_animation()
            
            # Retrieves points from Points class
            player = Points.player_points
            opponent = Points.opponent_points

            ### Displays points for game ###
            # Font for text
            font = pygame.font.Font('freesansbold.ttf', 32) 

            # Text that is displayed
            text = font.render(f'{opponent}       {player}', 
                               True, light_grey, grey) # colors in the text

           # creates surface object for text
            textRect = text.get_rect()

            # centers the text on display
            textRect.center = (screen_width // 2, 
                               screen_height // 2)


            # Visuals -> Colors in the rectangles and screen
            screen.fill(grey)  # The entire screen background

            screen.blit(text, textRect) # Displays points for each player

            pygame.draw.rect(screen, light_grey,
                            self.Animations.player)  # player
            pygame.draw.rect(screen, light_grey,
                            self.Animations.opponent)  # opponent
            pygame.draw.ellipse(screen, light_grey,
                                self.Animations.ball)  # ball (circle)

            pygame.draw.aaline(screen, light_grey,
                               # x coord      y coord
                               (screen_width/2, 0), (screen_width/2, screen_height))  # draws the center line for the game

            # updates window
            pygame.display.flip()
            clock.tick(60)  # limits on how fast the loop runs (60fps)


if __name__ == '__main__':
    game = Game(Animations, screen_width, screen_height)
    game.run()
