import pygame
import entity.animation

GRAVITY = 0.7 # Valeur de gravité
MAX_FALL_SPEED = 10 # Valeur maximum de chute
JUMP_FORCE = 7 # Valeur de saut
GROUND_Y = 500  # À adapter selon ton terrain

# Hauteur 50 largeur 53
class Player(entity.animation.AnimateSprite): # Classe du joueur
    def __init__(self, x, y, scale, speed):
        super().__init__('player',scale) # On appelle le constructeur parent donc de Sprite
        self.rect = self.image.get_rect(x=x,y=y) # On définit le Rect associé au joueur 
        self.speed = speed # On définit une vitesse au joueur
        self.vel_y = 0
        self.velocity = [0,0]
        self.in_air = True # Si le joueur est en l'air
        self.jumping =False # Si le joueur est en train de sauter
        self.facing_right = True # Si le joueur fait face à la droite
        self.can_jump = True 
        self.gravity =GRAVITY
        self.animation=False

    def update_animation(self):
        self.animate() 

    def update(self, tiles):# Méthode qui permet au joueur de se déplacer 
        dx = 0
        dy = 0
        
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.in_air == False:
            self.velocity[1] = -11
            self.in_air = True
        if key[pygame.K_q]:
            dx -= self.speed
        if key[pygame.K_d]:
            dx += self.speed
            
        self.velocity[1] += self.gravity
        if self.velocity[1] > 30:
            self.velocity[1] = 30
        dy += self.velocity[1]
            
            
        self.in_air = True
        for bloc in tiles:
            if bloc.can_touch and bloc.is_solid:
                #check for collision in x direction
                if bloc.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    if dx < 0:
                        self.rect.left = bloc.rect.right
                    if dx > 0:
                        self.rect.right = bloc.rect.left  
                    dx = 0
                #check for collision in y direction
                if bloc.rect.colliderect(self.rect.x, self.rect.y + dy + 1, self.width, self.height):
                    #check if below the ground i.e. jumping
                    if self.velocity[1] < 0:
                        dy = bloc.rect.bottom - self.rect.top
                        self.velocity[1] = 0
                    #check if above the ground i.e. falling
                    elif self.velocity[1] >= 0:
                        dy = 0
                        self.rect.bottom = bloc.rect.top
                        self.velocity[1] = 0
                        self.in_air = False
                

        self.rect.x += dx
        self.rect.y += dy

        if dx != 0:
            self.facing_right = dx > 0
            if not self.animation:
                self.start_animation()
        
    def draw(self, screen, camera): # Fonction qui dessine le joueur
        x_player , y_player = self.rect.topleft
        x_cam, y_cam = camera.rect.topleft
        print_pos = (x_player - x_cam + int((screen.get_width() - camera.rect.width)/2), y_player - y_cam + int((screen.get_height() - camera.rect.height)/2))
        print(print_pos)
        screen.blit(self.image, print_pos) # On affiche le joueur au centre de l'écran
        # rectangle = pygame.rect.Rect(camera.rect.width/2-25,camera.rect.height/2-25,50,50)
        # pygame.draw.rect(screen,(255,0,0),rectangle)
        