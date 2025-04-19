import pygame

class Tile(pygame.sprite.Sprite): # Classe Tuile
    TILE_SIZE = 32 # Taille d'une tuile
    
    def __init__(self,x:int,y:int):
        super().__init__() # On appelle le constructeur de la classe Sprite
        self.rect = pygame.Rect(x,y,self.TILE_SIZE,self.TILE_SIZE) # Le rect définit pour la tuile
        self.type = type # Le type de tuile définit par la classe TileType
        self.is_solid = False
        self.texture = None
        self.can_touch = True

    def draw(self, screen, camera): # Fonction qui dessine une tuile
         # On récupère la texture associée au type de la tuile 
        x_tile , y_tile = self.rect.topleft
        x_cam, y_cam = camera.rect.topleft
        print_pos = (x_tile - x_cam + int((screen.get_width() - camera.rect.width)/2), y_tile  - y_cam + int((screen.get_height() - camera.rect.height)/2))
        screen.blit(self.texture, print_pos)
         # On rajoute sur l'écran notre Tuile
        self.can_touch = True
        
    