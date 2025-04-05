import pygame
from TileType import TileType

class Tile():
    TILE_SIZE = 32
    
    def __init__(self,x:int,y:int,type:TileType):
        
        self.rect = pygame.Rect(x,y,self.TILE_SIZE,self.TILE_SIZE)
        self.type = type
        self.is_solid = type != TileType.AIR

    def draw(self, screen, textures, camera_x, camera_y):
        if self.type == TileType.AIR:
            return
        texture = textures[self.type]
        screen.blit(texture, (self.rect.x - camera_x, self.rect.y - camera_y))
        
    