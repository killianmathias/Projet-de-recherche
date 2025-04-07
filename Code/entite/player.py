import pygame
from .entity import Entity

GRAVITY = 0.7

class Player(Entity):
    
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, 'Code/img/player.png')
        self.speed = speed
        self.jump = False
        self.vel_y = 0
        self.in_air = True
        
    def draw(self, screen):
        super().draw(screen)
        
    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        
        if moving_left:
            dx = -self.speed
        if moving_right:
            dx = self.speed
            
        if self.jump == True:
            self.vel_y = -11
            self.jump = False
            self.in_air = True
            
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y
            
            
        if self.rect.bottom + dy > 500:
            dy = 500 - self.rect.bottom
            self.in_air = False
            
        self.rect.x += dx
        self.rect.y += dy