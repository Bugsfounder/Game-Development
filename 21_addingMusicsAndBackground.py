import pygame
import random
import os
from pygame.constants import K_RETURN

pygame.mixer.init()

pygame.init()



# COLORS 
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# GAME WINDOWS HERE 
screenWidth = 900
screenHeight = 600
gameWindow = pygame.display.set_mode((screenWidth, screenHeight))

# BACKGROUND IMAGE
bgImage = pygame.image.load('bg.jpg')
bgImage = pygame.transform.scale(bgImage, (screenWidth, screenHeight)).convert_alpha()

# GAME TITLE HERE 
pygame.display.set_caption("Snake Game - Manisha")
pygame.display.update()

clock  = pygame.time.Clock()

font = pygame.font.SysFont(None, 50)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y  in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((65,23,98))
        text_screen("Welcome to Snakes", white, 300, 250)
        text_screen("Press Space Bar to Play", white, 270, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameLoop()
            
        pygame.display.update()
        clock.tick(60)

# CREATING GAME LOOP 
def gameLoop():
    
    # CHECK IF HIGHSCORE FILE IS EXISTS
    if not os.path.exists('highscore.txt'):
        with open('highscore.txt', 'w') as f:
            f.write("0")

    with open('highscore.txt', 'r') as f:
        hiscore = f.read()
    
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

    snk_list = []
    snk_length = 1

    while not exit_game:

        if game_over:
         
            with open('highscore.txt', 'w') as f:
               f.write(str(hiscore))

            gameWindow.fill(white)
            text_screen("Game Over. Press Enter to Continue", red, 150, 240)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        welcome()

            
        else:

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

                    
                    if event.key == pygame.K_q:
                        score += 10 

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x-food_x)<30 and abs(snake_y-food_y)<30:
                score += 10 
                food_x =  random.randint(20, screenWidth/2)
                food_y =  random.randint(20, screenHeight/2)
                snk_length += 5
                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgImage, (0,0))
            text_screen(f"Score: {score} | Hiscore: {hiscore}", red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size+4, snake_size+4])
            

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()



            if snake_x<0 or snake_x>screenWidth or snake_y<0 or snake_y>screenHeight:
                game_over = True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()
                print("Game Over")

            # creating food rectangle 
            plot_snake(gameWindow, black, snk_list, snake_size) # CREATING RECTANGLE TO SNAKE HEAD 

        pygame.display.update() # UPDATING DISPLAY
        clock.tick(fps) 

    pygame.quit()
    quit()

welcome()