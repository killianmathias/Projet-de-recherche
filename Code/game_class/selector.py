import pygame
import math
from tiles import * 

class Selector(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mouse = pygame.mouse
        self.tile = None
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.collide_rect = pygame.Rect(0, 0, 32, 32)  # Met un Rect visible par défaut (32x32px par exemple)
        self.delete = False
        self.image = pygame.image.load("Code/textures/selector/selector.png")
    
    def handling_events(self, events):
        mouse_x, mouse_y = self.mouse.get_pos()
        self.rect.topleft = (mouse_x, mouse_y)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1 = clic gauche
                print("clic gauche activé")
                self.delete=True
                

    def update(self, group, camera,world):
        events = pygame.event.get()
        self.handling_events(events)

        # Mettre à jour la position de la souris (correctement)
        mouse_x, mouse_y = self.mouse.get_pos()
        self.rect.topleft = (mouse_x + camera.rect.x - 16, mouse_y + camera.rect.y - 16)
           

        # Cherche un bloc sous la souris
        self.tile = None
        for bloc in group:
            # if bloc.can_touch and bloc.is_solid:
                if bloc.rect.colliderect(self.rect):
                    self.tile = bloc
                      # dès qu'on trouve, on arrête
                      
        if self.tile is not None:
            self.rect.topleft = self.tile.rect.topleft
            
        if self.tile and self.delete:
            x_tile = self.tile.rect.x // 32
            y_tile = self.tile.rect.y // 32
            
            self.tile.kill()  # Enlève l'ancienne tuile du groupe

            new_tile = Air(self.tile.rect.x, self.tile.rect.y)  # Air aux mêmes coordonnées
            world.terrain[x_tile][y_tile] = new_tile  # IMPORTANT : remplace dans le terrain
            group.add(new_tile)  # Ajoute dans le groupe

            self.delete = False

    # Pas besoin de toucher à self.rect ici : il reste la position souris
    def draw(self, screen, camera):
        if self.rect:
            x_selector, y_selector = self.rect.topleft
            x_cam, y_cam = camera.rect.topleft
            print_pos = (
                x_selector - x_cam + (screen.get_width() - camera.rect.width) // 2,
                y_selector - y_cam + (screen.get_height() - camera.rect.height) // 2
            )
            screen.blit(self.image, print_pos)