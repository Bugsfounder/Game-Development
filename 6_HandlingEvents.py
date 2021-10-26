import pygame
from pygame.constants import K_RIGHT, KEYDOWN

# INITIALIZING PYGAME 
pygame.init()

# CREATING DISPLAY OF THE GAME 
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("Handling Events in Pygame")

# SPECIFIC VARIABLES 
quit_game = False
game_over = False


# CREATING GAME LOOP 
while not quit_game:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            quit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print('You Have Clicked Right Arrow Kye')


pygame.quit()
quit()

