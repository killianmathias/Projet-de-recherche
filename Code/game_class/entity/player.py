import pygame

GRAVITY = 1.2 # Valeur de gravité
MAX_FALL_SPEED = 10 # Valeur maximum de chute
JUMP_FORCE = 7 # Valeur de saut
GROUND_Y = 500  # À adapter selon ton terrain

class Player(pygame.sprite.Sprite): # Classe du joueur
    def __init__(self, x, y, scale, speed):
        super().__init__() # On appelle le constructeur parent donc de Sprite
        self.image = pygame.image.load('Code/textures/Player/player.png') # On définit l'image de notre joueur
        self.image = pygame.transform.scale(self.image,(int(self.image.get_width() * scale), int(self.image.get_height() * scale))) # On adapte la taille de l'image
        self.rect = self.image.get_rect(x=x,y=y) # On définit le Rect associé au joueur 
        self.speed = speed # On définit une vitesse au joueur
        self.velocity = [0,0] # Un tableau de velocité pour une valeur horizontale et une valeur verticale
        self.in_air = True # Si le joueur est en l'air
        self.jumping =False # Si le joueur est en train de sauter


    
    def apply_gravity(self): # Méthode qui applique la gravité au joueur
        self.velocity[1] += GRAVITY
        if self.velocity[1] > MAX_FALL_SPEED:
            self.velocity[1] = MAX_FALL_SPEED
    
    def jump(self): # Méthode qui permet au joueur de sauter
        self.velocity[1] = -JUMP_FORCE
        self.in_air = True

    def move(self, tiles):# Méthode qui permet au joueur de se déplacer 
        # Si le joueur n'est pas déjà en train de sauter alors on le fait sauter
        if self.jumping: 
            self.jump()
            self.jumping=False
        #Mouvement horizontal
        self.rect.x += self.velocity[0] * self.speed
        for row in tiles:
            for tile in row:
                if tile.is_solid and self.rect.colliderect(tile.rect): # On vérifie les collisions 
                    if self.velocity[0] > 0:  # Va à droite
                        self.rect.right = tile.rect.left
                    elif self.velocity[0] < 0:  # Va à gauche
                        self.rect.left = tile.rect.right

        # Mouvement vertical
        self.rect.y += self.velocity[1] * self.speed
        for row in tiles:
            for tile in row:
                if tile.is_solid and self.rect.colliderect(tile.rect): # On vérifie les collisions
                    if self.velocity[1] > 0:  # Tombe vers le bas
                        self.rect.bottom = tile.rect.top
                        self.in_air = False
                    elif self.velocity[1] < 0:  # Monte
                        self.rect.top = tile.rect.bottom
                    self.velocity[1] = 0


         # On déplace le joueur horizontalement
            
        # Vérifier les collisions verticales
        
        # Limiter le mouvement horizontal
    

        
    def draw(self, screen): # Fonction qui dessine le joueur
        screen.blit(self.image, (self.rect.x, self.rect.y)) # On affiche le joueur au centre de l'écran
        # pygame.draw.rect(screen, (255, 0, 0), 
        #                 pygame.Rect(self.rect.x - camera_x, self.rect.y - camera_y, self.rect.width, self.rect.height), 2)


    