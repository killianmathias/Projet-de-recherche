import pygame

class Camera (pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        self.speed = 15
        
        
    def update(self, position_player, fly):
        if not fly:
            self.rect.center = position_player
        
        else:

            dx = 0
            dy = 0
            
            key = pygame.key.get_pressed()
            if key[pygame.K_q]:
                dx -= self.speed
            if key[pygame.K_d]:
                dx += self.speed
            if key[pygame.K_s]:
                dy += self.speed
            if key[pygame.K_z]:
                dy -= self.speed
        
            self.rect.x += dx
            self.rect.y += dy
        
    def draw(self, screen):
        # x = int((screen.get_width() - self.rect.width)/2)
        # y = int((screen.get_height() - self.rect.height)/2)
        # rect = pygame.Rect(x, y, self.rect.width, self.rect.height)
        # pygame.draw.rect(screen, (255, 0, 0), rect, 2)
        return