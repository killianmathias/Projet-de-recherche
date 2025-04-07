import pygame
from entite import *

class Game():
    
    def __init__(self):
        
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Terraria')
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.player = Player(200, -2000, 0.1, 5, 0.7)

        bloc = Bloc(600, 375, 50)
        self.blocs = pygame.sprite.Group()
        self.blocs.add(bloc)
        
        
    def run(self):
        
        while self.running:

            self.clock.tick(60)

            self.screen.fill((255,255,0))
            
            self.player.draw(self.screen)
            self.blocs.draw(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:

                        self.player.moving_left = True
                    if event.key == pygame.K_d:
                        self.player.moving_right = True
                    if event.key == pygame.K_SPACE :
                        self.player.jump = True
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        self.player.moving_left = False
                    if event.key == pygame.K_d:
                        self.player.moving_right = False


            self.player.update(self.blocs)

            pygame.display.update()