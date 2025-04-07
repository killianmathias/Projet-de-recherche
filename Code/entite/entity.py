import pygame

class Entity(pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, height, texture):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        img = pygame.image.load(texture)
        self.image = pygame.transform.scale(img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def move(self, moving_left, moving_right):
        return