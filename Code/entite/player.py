import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Code/img/player.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)