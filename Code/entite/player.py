import pygame

GRAVITY = 0.7

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y, scale, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.jump = False
        self.vel_y = 0
        self.in_air = True
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Code/img/player.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
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