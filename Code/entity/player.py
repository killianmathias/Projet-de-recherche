import pygame

GRAVITY = 0.75
MAX_FALL_SPEED = 10
JUMP_FORCE = 11
GROUND_Y = 500  # À adapter selon ton terrain

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        super().__init__()

        self.image = pygame.image.load('Code/textures/Player/player.png')
        self.image = pygame.transform.scale(
            self.image,
            (int(self.image.get_width() * scale), int(self.image.get_height() * scale))
        )
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = speed
        self.vel_y = 0
        self.in_air = True

    def jump(self):
        if not self.in_air:
            self.vel_y = -JUMP_FORCE
            self.in_air = True

    def apply_gravity(self):
        self.vel_y += GRAVITY
        if self.vel_y > MAX_FALL_SPEED:
            self.vel_y = MAX_FALL_SPEED

    def move(self, moving_left, moving_right, terrain):
        dx = 0
        dy = 0

        # Mouvement horizontal
        if moving_left:
            dx = -self.speed
        if moving_right:
            dx = self.speed


        # Gravité
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y


        # --- COLLISIONS VERTICALES ---

        for tiles in terrain:
            for tile in tiles :
                if not tile.is_solid:
                    continue

                tile_rect = pygame.Rect(
                    tile.x * tile.TILE_SIZE,
                    tile.y * tile.TILE_SIZE + tile.TILE_SIZE/4,
                    tile.TILE_SIZE,
                    tile.TILE_SIZE
                )

                # Collision horizontale
                if tile_rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                    dx = 0

                # Collision verticale
                if tile_rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                    dy = 0
                    self.in_air =False

        # Mise à jour position
        self.rect.x += dx
        self.rect.y += dy
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)


    