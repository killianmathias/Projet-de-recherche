import pygame
from entity import *
from world import *


class Game:
    def __init__(self,screen):
        self.screen = screen # L'écran sur lequel le jeu est affiché
        self.running = True #Si le jeu est en train de tourner
        self.clock = pygame.time.Clock() # Une horloge qui servira à limiter le nombre de frames par seconde
         # Le joueur
        self.background =pygame.transform.scale(pygame.image.load("Code/textures/Background/1.png"), (1080*5,720*5)) # L'image de background (qui changera en fonction des biomes)
        self.world = World(1080,720) # Le monde généré avec des tuiles
        self.player = Player(0, 0 ,1,5)
        x_cam, y_cam = self.player.rect.center
        self.camera = Camera(x_cam, y_cam, 1080, 720)
        self.group = pygame.sprite.Group()
        self.ticks_count=0
        
        self.fly = False
        for row in self.world.terrain:
            for tile in row:
                self.group.add(tile)
        


    def handling_events(self): # Fonction qui gère les évènements

        for event in pygame.event.get(): # Boucle qui parcours les évènements
            if event.type == pygame.QUIT: # Si l'évènement est de quitter la fenêtre
                self.running= False # On arrête le jeu
                
            if event.type == pygame.KEYDOWN: # vérifie pression de touche 
                if event.key == pygame.K_ESCAPE: # Si échappe alors quitte le jeu
                    self.running = False
                    
            if event.type == pygame.KEYUP: # vérifie arrêt pression de touche 
                if event.key == pygame.K_p: # Si p alors fly ou non
                    if self.fly:
                        self.player.rect.center = self.camera.rect.center
                    self.fly = not self.fly

        
    def update(self): # Fonction qui gère la mise à jour des informations
        if not self.fly:
            self.player.update(self.group) # Déplacement du joueur sur le terrain
        self.camera.update(self.player.rect.center, self.fly)
        self.player.update_animation()

    def draw(self): # Fonction qui gère l'affichage
        self.screen.fill("black") # Remplir le fond en noir
        screen.blit(self.background,(0,0)) # Background
        self.world.draw(self.screen, self.camera) # Dessiner le monde avec ses tuiles
        self.player.draw(self.screen, self.camera) # Dessiner le joueur
        pygame.display.flip() # Mise à jour des informations sur l'écran

    def run(self): # Fonction principale qui fait tourner le jeu
        while self.running: # Tant que le jeu tourne
            # Appel des trois fonctions précédentes
            self.handling_events()
            self.update()
            self.draw()
            self.clock.tick(60) # Limite les FPS à 60
                

pygame.init() # Initialiser la bibliothèque pygame
screen = pygame.display.set_mode((1080,720))# Initialiser l'écran
pygame.display.set_caption("Terraria") 
pygame.display.set_icon(pygame.image.load("Code/textures/icon.png")) # On met une icône
game = Game(screen) # Initialisation d'une instance de la classe Game
game.run() # Mise en route du jeu
pygame.quit() # On libère tout