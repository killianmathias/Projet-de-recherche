from tiles.tile import Tile
import pygame

class Dirt(Tile):
    def __init__(self, x, y,position):
        super().__init__(x, y)
        self.is_solid =True
        self.position = position
        if (self.position == 'base'):
            self.texture = pygame.transform.scale(pygame.image.load("Code/textures/Tiles/dirt.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE))
        elif (self.position == 'corner-left'):
            self.texture = pygame.transform.scale(pygame.image.load("Code/textures/Tiles/dirt-corner-left.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE))
        elif (self.position == 'corner-right'):
            self.texture = pygame.transform.scale(pygame.image.load("Code/textures/Tiles/dirt-corner-right.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE))
    
    