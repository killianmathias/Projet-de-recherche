import pygame
from .entity import Entity

class Player(Entity):
    
    def __init__(self, x, y, scale, speed, gravity):
        img = pygame.image.load('Code/img/player.png')
        self.width = int(img.get_width() * scale)
        self.height = int(img.get_height() * scale)
        Entity.__init__(self, x, y, self.width, self.height, 'Code/img/player.png')
        self.speed = speed
        self.jump = False
        self.vel_y = 0
        self.in_air = True
        self.gravity = gravity

        
    def draw(self, screen):
        super().draw(screen)
        
    def update(self, blocs):
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
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y
            
            
        self.in_air = True
        for bloc in blocs:
            #check for collision in x direction
            if bloc.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            #check for collision in y direction
            if bloc.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
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
                    
        if self.rect.bottom + dy > 400:
            dy = 400 - self.rect.bottom
            self.in_air = False
            self.vel_y = 0
            

        self.rect.x += dx
        self.rect.y += dy