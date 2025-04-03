import pygame
from entite import *

# pygame setup
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Terraria')

player = Player(200, 200, 0.1)

running = True
while running:
    
    player.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    pygame.display.update()
    

pygame.quit()