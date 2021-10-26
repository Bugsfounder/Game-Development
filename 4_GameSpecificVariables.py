import pygame

pygame.init()

# CREATING WINDOW OF GAME 
gameWindow = pygame.display.set_mode((1200, 500))

# SETTING TITLE OF THE GAME CAPTION
pygame.display.set_caption("My First Game")

# GAME SPECIFIC VARIABLES 
exit_game = False
game_over = False