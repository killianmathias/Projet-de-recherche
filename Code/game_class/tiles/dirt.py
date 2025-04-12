from tiles.tile import Tile
import pygame

class Dirt(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_solid =True
        self.texture = pygame.transform.scale(pygame.image.load("Code/textures/Tiles/dirt.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE))
    
    