import pygame

class Camera (pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        
        
    def update(self, position_player):
        self.rect.center = position_player
        
        