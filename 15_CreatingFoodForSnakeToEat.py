import pygame
import random

pygame.init()

# COLORS 
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# GAME WINDOWS HERE 
screenWidth = 900
screenHeight = 600
gameWindow = pygame.display.set_mode((screenWidth, screenHeight))

# GAME TITLE HERE 
pygame.display.set_caption("Snake Game - Manisha")
pygame.display.update()

# GAME SPECIFIC VARIABLES
exit_game = False
game_over = False

snake_size = 10

snake_x = 40
snake_y = 50

velocity_x = 0 
velocity_y = 0

food_x =  random.randint(0, screenWidth)
food_y =  random.randint(0, screenHeight)

fps = 30

clock  = pygame.time.Clock()

# CREATING GAME LOOP 
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0
            
            if event.key == pygame.K_LEFT:
                velocity_x = -10
                velocity_y = 0

            if event.key == pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0

            if event.key == pygame.K_UP:
                velocity_y = -10
                velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y


    gameWindow.fill(white)
    # creating food rectangle 
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size]) # CREATING RECTANGLE TO SNAKE HEAD 
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size+4, snake_size+4])
    # UPDATING DISPLAY 
    pygame.display.update()       
    clock.tick(fps) 

pygame.quit()
quit()