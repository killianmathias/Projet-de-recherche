import pygame

GRAVITY = 1.2
MAX_FALL_SPEED = 10
JUMP_FORCE = 7
GROUND_Y = 500  # À adapter selon ton terrain

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        super().__init__()
        self.image = pygame.image.load('Code/textures/Player/player.png')
        self.image = pygame.transform.scale(self.image,(int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect(x=x,y=y)
        self.speed = speed
        self.velocity = [0,0]
        self.in_air = True
        self.jumping =False


    
    def apply_gravity(self):
        self.velocity[1] += GRAVITY
        if self.velocity[1] > MAX_FALL_SPEED:
            self.velocity[1] = MAX_FALL_SPEED
    
    def jump(self):
        if not self.in_air:
            self.velocity[1] = -JUMP_FORCE
            self.apply_gravity()
            self.in_air = True

    def move(self, tiles):
    # Mouvement horizontal
        if self.jumping:
            self.jump()
            self.jumping=False
        self.rect.x += self.velocity[0] * self.speed
        for row in tiles:
            for tile in row:
                if tile.is_solid and self.rect.colliderect(tile.rect):
                    if self.velocity[0] > 0:  # Va à droite
                        self.rect.right = tile.rect.left
                    elif self.velocity[0] < 0:  # Va à gauche
                        self.rect.left = tile.rect.right

        # Mouvement vertical
        
        self.rect.y += self.velocity[1] * self.speed
        for row in tiles:
            for tile in row:
                if tile.is_solid and self.rect.colliderect(tile.rect):
                    if self.velocity[1] > 0:  # Tombe vers le bas
                        self.rect.bottom = tile.rect.top
                        self.in_air = False
                    elif self.velocity[1] < 0:  # Monte
                        self.rect.top = tile.rect.bottom
                    self.velocity[1] = 0


        
    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))
        pygame.draw.rect(screen, (255, 0, 0), 
                        pygame.Rect(self.rect.x - camera_x, self.rect.y - camera_y, self.rect.width, self.rect.height), 2)


    