import pygame
from tiles.tile import Tile

class Grass(Tile):
    def __init__(self, x, y, position):
        super().__init__(x, y)
        self.is_solid = True
        self.position = position
        if (self.position == 'base'):
            self.texture = pygame.transform.scale(pygame.image.load("Code/textures/Tiles/grass.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE))
        elif (self.position == 'left'):
            self.texture = pygame.transform.scale(pygame.image.load("Code/textures/Tiles/grass-left.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE))
        elif (self.position == 'right'):
            self.texture = pygame.transform.scale(pygame.image.load("Code/textures/Tiles/grass-right.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE))
        elif (self.position == 'corner-left'):
            self.texture = pygame.transform.scale(pygame.image.load("Code/textures/Tiles/grass-corner-left.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE))
        elif (self.position == 'corner-right'):
            self.texture = pygame.transform.scale(pygame.image.load("Code/textures/Tiles/grass-corner-right.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE))

        