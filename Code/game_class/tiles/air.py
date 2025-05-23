import pygame
from .tile import Tile

class Air(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_solid = False
        self.texture = pygame.transform.scale(pygame.image.load("Code/textures/Tiles/air.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE))
        
    def draw(self, screen, camera):
        return