import pygame
from entite import *

class Game():
    
    def __init__(self):
        
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Terraria')
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.Player = Player(200, 200, 0.1, 5)
        
        
    def run(self):
        
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
                    
            pygame.display.update()