import pygame
from entity import Player
from world import *

class Game:
    def __init__(self,screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(500,20,0.05,5)
        self.background =pygame.transform.scale(pygame.image.load("Code/textures/Background/1.png"), (10800,7200))
        self.world = World(1080,720)
        self.camera_x = 0
        self.camera_y = 0


    def handling_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running= False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.velocity[0]=-1
        elif keys[pygame.K_RIGHT]:
            self.player.velocity[0]=1
        else:
            self.player.velocity[0] =0

        if keys[pygame.K_SPACE]:
            self.player.jumping=True
            
        elif keys[pygame.K_DOWN]:
            self.player.velocity[1]=1
        else:
            self.player.velocity[1]=0

                
        
    def update(self):
        self.camera_x = self.player.rect.centerx - self.screen.get_width() // 2
        self.camera_y = self.player.rect.centery - self.screen.get_height() // 2
        self.player.apply_gravity()
        self.player.move(self.world.terrain)
    def display(self):

        self.screen.fill("black")
        background_scroll = int(self.player.rect.x / 4)  # Ajuster la vitesse du fond
        screen.blit(self.background, (-background_scroll, 0))  # optionnel si background scrolling

        self.world.draw(self.screen, self.camera_x, self.camera_y)
        self.player.draw(self.screen, self.camera_x, self.camera_y)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)
                

pygame.init()
screen = pygame.display.set_mode((1080,720))
game = Game(screen)
game.run()
pygame.quit()