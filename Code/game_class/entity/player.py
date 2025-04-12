import pygame
import entity.animation

GRAVITY = 1.2 # Valeur de gravité
MAX_FALL_SPEED = 10 # Valeur maximum de chute
JUMP_FORCE = 7 # Valeur de saut
GROUND_Y = 500  # À adapter selon ton terrain

# Hauteur 50 largeur 53
class Player(entity.animation.AnimateSprite): # Classe du joueur
    def __init__(self, x, y, scale, speed):
        super().__init__('player') # On appelle le constructeur parent donc de Sprite # On adapte la taille de l'image
        self.rect = self.image.get_rect(x=x,y=y) # On définit le Rect associé au joueur 
        self.speed = speed # On définit une vitesse au joueur
        self.velocity = [0,0] # Un tableau de velocité pour une valeur horizontale et une valeur verticale
        self.in_air = True # Si le joueur est en l'air
        self.jumping =False # Si le joueur est en train de sauter
        self.facing_right = True # Si le joueur fait face à la droite
        self.can_jump = True # Si le joueur peut sauter


    def update_animation(self):
        self.animate()  # Ne redémarre pas tout le temps, on laisse animate() gérer la suite
    def apply_gravity(self): # Méthode qui applique la gravité au joueur
        self.velocity[1] += GRAVITY
        if self.velocity[1] > MAX_FALL_SPEED:
            self.velocity[1] = MAX_FALL_SPEED
    
    def jump(self): # Méthode qui permet au joueur de sauter
        if not self.in_air and self.can_jump:  # On ne peut sauter que si on est au sol
            self.velocity[1] = -JUMP_FORCE
            self.in_air = True
            self.can_jump = False  # On ne peut pas sauter tant qu'on n'est pas au sol
    def move(self, tiles):
    # Déplacer horizontalement
        self.rect.x += self.velocity[0] * self.speed
        for row in tiles:
            for tile in row:
                if tile.is_solid and self.rect.colliderect(tile.rect): # On vérifie les collisions horizontales
                    if self.velocity[0] > 0:  # Si on va à droite
                        self.rect.right = tile.rect.left
                    elif self.velocity[0] < 0:  # Si on va à gauche
                        self.rect.left = tile.rect.right
                    self.velocity[0] = 0  # Annule la vitesse horizontale après la collision

        # Déplacer verticalement
        self.rect.y += self.velocity[1] * self.speed
        for row in tiles:
            for tile in row:
                if tile.is_solid and self.rect.colliderect(tile.rect): # On vérifie les collisions verticales
                    if self.velocity[1] > 0:  # Si on tombe
                        self.rect.bottom = tile.rect.top  # On se place juste au-dessus du bloc
                        self.in_air = False  # Le joueur touche le sol
                    elif self.velocity[1] < 0:  # Si on monte (saut)
                        self.rect.top = tile.rect.bottom  # On se place juste en dessous du bloc
                    self.velocity[1] = 0  # Annule la vitesse verticale après la collision

        # Gérer l'animation
        if self.velocity[0] != 0:
            self.facing_right = self.velocity[0] > 0
            if not self.animation:
                self.start_animation()
    

        
    def draw(self, screen): # Fonction qui dessine le joueur
        screen.blit(self.image, (self.rect.x, self.rect.y)) # On affiche le joueur au centre de l'écran
        # pygame.draw.rect(screen, (255, 0, 0), 
        #                 pygame.Rect(self.rect.x - camera_x, self.rect.y - camera_y, self.rect.width, self.rect.height), 2)


    