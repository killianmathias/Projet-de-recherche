import pygame

class Entity(pygame.sprite.Sprite):
    
    def __init__(self, x, y, scale, texture):
        super()
        self.x = x
        self.y = y
        img = pygame.image.load(texture)
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_width() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def move(self):
        return