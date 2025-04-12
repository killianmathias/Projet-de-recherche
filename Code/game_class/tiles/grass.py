import pygame
from tiles.tile import Tile

class Grass(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_solid = True
        self.texture = pygame.transform.scale(pygame.image.load("Code/textures/Tiles/grass.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE))