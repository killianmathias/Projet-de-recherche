import pygame
from TileType import TileType

class Tile(): # Classe Tuile
    TILE_SIZE = 32 # Taille d'une tuile
    
    def __init__(self,x:int,y:int,type:TileType):
        
        self.rect = pygame.Rect(x,y,self.TILE_SIZE,self.TILE_SIZE) # Le rect définit pour la tuile
        self.type = type # Le type de tuile définit par la classe TileType
        self.is_solid = type != TileType.AIR # Si la tuile est solide ou non

    def draw(self, screen, textures, camera_x, camera_y): # Fonction qui dessine une tuile
        if self.type == TileType.AIR: # Si le type de la caméra est de l'air
            return
        texture = textures[self.type] # On récupère la texture associée au type de la tuile 
        screen.blit(texture, (self.rect.x - camera_x, self.rect.y - camera_y)) # On rajoute sur l'écran notre Tuile
        
    