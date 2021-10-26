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

snake_size = 30

snake_x = 45
snake_y = 55

velocity_x = 0 
velocity_y = 0
init_velocity = 5

food_x =  random.randint(20, screenWidth/2)
food_y =  random.randint(20, screenHeight/2)

score = 0

fps = 60

clock  = pygame.time.Clock()

font = pygame.font.SysFont(None, 15)

def text_score(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

# CREATING GAME LOOP 
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0
            
            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0

            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y

    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        score += 1*10 
        print(f"Score: {score}")
        food_x =  random.randint(20, screenWidth/2)
        food_y =  random.randint(20, screenHeight/2)
         

    gameWindow.fill(white)
    text_score(f"Score: {score}", red, 5, 5)

    # creating food rectangle 
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size]) # CREATING RECTANGLE TO SNAKE HEAD 
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size+4, snake_size+4])
    # UPDATING DISPLAY 
    pygame.display.update()       
    clock.tick(fps) 

pygame.quit()
quit()