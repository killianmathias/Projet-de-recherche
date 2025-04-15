import pygame

GRAVITY = 0.7 # Valeur de gravité
MAX_FALL_SPEED = 10 # Valeur maximum de chute
JUMP_FORCE = 7 # Valeur de saut
GROUND_Y = 500  # À adapter selon ton terrain

class Player(pygame.sprite.Sprite): # Classe du joueur
    def __init__(self, x, y, scale, speed):
        super().__init__() # On appelle le constructeur parent donc de Sprite
        img = pygame.image.load('Code/textures/Player/player.png') # On définit l'image de notre joueur
        self.width = int(img.get_width() * scale)
        self.height = int(img.get_height() * scale)
        self.image = pygame.transform.scale(img, (self.width, self.height)) # On adapte la taille de l'image
        self.rect = self.image.get_rect(x=x,y=y) # On définit le Rect associé au joueur 
        self.speed = speed # On définit une vitesse au joueur
        self.vel_y = 0
        self.in_air = True # Si le joueur est en l'air
        self.jumping =False # Si le joueur est en train de sauter
        self.gravity = GRAVITY


    def update(self, tiles):# Méthode qui permet au joueur de se déplacer 
        dx = 0
        dy = 0
        
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.in_air == False:
            self.vel_y = -11
            self.in_air = True
        if key[pygame.K_q]:
            dx -= self.speed
        if key[pygame.K_d]:
            dx += self.speed
            
        self.vel_y += self.gravity
        if self.vel_y > 30:
            self.vel_y = 30
        dy += self.vel_y
            
            
        self.in_air = True
        for bloc in tiles:
            #check for collision in x direction
            if bloc.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height) and bloc.is_solid:
                if dx < 0:
                    self.rect.left = bloc.rect.right
                if dx > 0:
                    self.rect.right = bloc.rect.left  
                dx = 0
            #check for collision in y direction
            if bloc.rect.colliderect(self.rect.x, self.rect.y + dy + 1, self.width, self.height) and bloc.is_solid:
                #check if below the ground i.e. jumping
                if self.vel_y < 0:
                    dy = bloc.rect.bottom - self.rect.top
                    self.vel_y = 0
                #check if above the ground i.e. falling
                elif self.vel_y >= 0:
                    dy = 0
                    self.rect.bottom = bloc.rect.top
                    self.vel_y = 0
                    self.in_air = False
                

        self.rect.x += dx
        self.rect.y += dy
    

        
    def draw(self, screen, camera): # Fonction qui dessine le joueur
        x_player , y_player = self.rect.topleft
        x_cam, y_cam = camera.rect.topleft
        screen.blit(self.image, (x_player - x_cam, y_player - y_cam)) # On affiche le joueur au centre de l'écran
        # pygame.draw.rect(screen, (255, 0, 0), 
        #                 pygame.Rect(self.rect.x - camera_x, self.rect.y - camera_y, self.rect.width, self.rect.height), 2)

