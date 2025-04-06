import pygame
from entity import Player
from world import *


class Game:
    def __init__(self,screen):
        self.screen = screen # L'écran sur lequel le jeu est affiché
        self.running = True #Si le jeu est en train de tourner
        self.clock = pygame.time.Clock() # Une horloge qui servira à limiter le nombre de frames par seconde
        self.player = Player(500,20,0.05,5) # Le joueur
        self.background =pygame.transform.scale(pygame.image.load("Code/textures/Background/1.png"), (1080*5,720*5)) # L'image de background (qui changera en fonction des biomes)
        self.world = World(1080,720) # Le monde généré avec des tuiles
        self.camera_x = 0 # La position x de la caméra
        self.camera_y = 0 # La position y de la caméra


    def handling_events(self): # Fonction qui gère les évènements

        for event in pygame.event.get(): # Boucle qui parcours les évènements
                if event.type == pygame.QUIT: # Si l'évènement est de quitter la fenêtre
                    self.running= False # On arrête le jeu
        keys = pygame.key.get_pressed() # Ensemble des touches pressées
        if keys[pygame.K_LEFT]: # Si la touche est le bouton gauche
            self.player.velocity[0]=-1 # Le joueur se déplace à gauche
        elif keys[pygame.K_RIGHT]: # Si la touche est le bouton droit
            self.player.velocity[0]=1 # Le joueur se déplace à droite
        else:
            self.player.velocity[0] =0 # Le joueur ne se déplace plus

        if keys[pygame.K_SPACE]: # Si la touche pressée est la touche espace
            self.player.jumping=True # Le joueur saute
            
        elif keys[pygame.K_DOWN]: # Si la touche est le bouton bas
            self.player.velocity[1]=1 # Le joueur descend
        else:
            self.player.velocity[1]=0 # Sinon le joueur ne descend pas  
        
    def update(self): # Fonction qui gère la mise à jour des informations
        self.camera_x = self.player.rect.centerx - self.screen.get_width() // 2 # Coordonnées x de la caméra
        self.camera_y = self.player.rect.centery - self.screen.get_height() // 2 # Coordonnées y de la caméra
        self.player.apply_gravity() # Appel de la fonction qui applique la gravité au joueur
        self.player.move(self.world.terrain) # Déplacement du joueur sur le terrain

    def display(self): # Fonction qui gère l'affichage
        self.screen.fill("black") # Remplir le fond en noir
        background_scroll = int(self.player.rect.x / 4)  # Ajuster la vitesse du fond
        screen.blit(self.background, (-background_scroll, 0))  # optionnel si background scrolling
        self.world.draw(self.screen, self.camera_x, self.camera_y) # Dessiner le monde avec ses tuiles
        self.player.draw(self.screen, self.camera_x, self.camera_y) # Dessiner le joueur
        pygame.display.flip() # Mise à jour des informations sur l'écran

    def run(self): # Fonction principale qui fait tourner le jeu
        while self.running: # Tant que le jeu tourne
            # Appel des trois fonctions précédentes
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60) # Limite les FPS à 60
                

pygame.init() # Initialiser la bibliothèque pygame
screen = pygame.display.set_mode((1080,720)) # Initialiser l'écran
game = Game(screen) # Initialisation d'une instance de la classe Game
game.run() # Mise en route du jeu
pygame.quit() # On libère tout