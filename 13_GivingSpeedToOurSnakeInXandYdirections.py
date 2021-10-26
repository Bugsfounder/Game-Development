import pygame

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
snake_x = 45
snake_y = 55
snake_size = 10
velocity_x = 4 
velocity_y = 4 
fps = 30

clock  = pygame.time.Clock()

# CREATING GAME LOOP 
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10
            
            if event.key == pygame.K_LEFT:
                snake_x = snake_x - 10

            if event.key == pygame.K_DOWN:
                snake_y = snake_y + 10

            if event.key == pygame.K_UP:
                snake_y = snake_y - 10
    snake_x += velocity_x
    snake_y += velocity_y


    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size]) # CREATING RECTANGLE TO SNAKE HEAD 
    pygame.display.update()       
    clock.tick(fps) 

pygame.quit()
quit()