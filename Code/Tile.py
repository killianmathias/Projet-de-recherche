import pygame
from TileType import TileType

class Tile():
    TILE_SIZE = 32
    
    def __init__(self,x:int,y:int,type:TileType):
        self.x = x
        self.y = y
        self.type = type
        self.is_solid = type != TileType.AIR

    def render(self,screen,textures):
        if self.type == TileType.AIR:
            return
        texture = textures[self.type]
        screen.blit(texture, (self.x * self.TILE_SIZE, self.y * self.TILE_SIZE))
    