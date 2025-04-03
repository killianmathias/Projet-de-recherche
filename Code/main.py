import pygame
from entite import *

# pygame setup
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Terraria')

clock = pygame.time.Clock()
FPS = 60

player = Player(200, 200, 0.1, 5)

moving_left = False
moving_right = False
running = True
while running:
    
    clock.tick(FPS)
    
    screen.fill("purple")
    player.draw(screen)
    
    player.move(moving_left, moving_right)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                player.jump = True
            if event.key == pygame.K_ESCAPE:
                running = False
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
                
    pygame.display.update()
    

pygame.quit()