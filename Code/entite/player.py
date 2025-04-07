import pygame
from .entity import Entity

class Player(Entity):
    
    def __init__(self, x, y, scale, speed, gravity):
        img = pygame.image.load('Code/img/player.png')
        Entity.__init__(self, x, y, int(img.get_width() * scale), int(img.get_height() * scale), 'Code/img/player.png')
        self.speed = speed
        self.jump = False
        self.vel_y = 0
        self.in_air = True
        self.gravity = gravity
        self.moving_left = False
        self.moving_right = False

        
    def draw(self, screen):
        super().draw(screen)
        
    def update(self, blocs):
        dx = 0
        dy = 0
        
        if self.moving_left:
            dx = -self.speed
        if self.moving_right:
            dx = self.speed
                
        if self.jump == True:
            self.vel_y = -11
            self.jump = False
            self.in_air = True
            
        if self.in_air:
            self.vel_y += self.gravity
            if self.vel_y > 10:
                self.vel_y = 10
        dy += self.vel_y
            
        if self.rect.bottom + dy > 400:
            dy = 400 - self.rect.bottom
            self.in_air = False
            self.vel_y = 0

        for bloc in blocs:
            if self.rect.colliderect(bloc.rect):
                print('colision')

        self.rect.x += dx
        self.rect.y += dy