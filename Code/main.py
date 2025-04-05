import pygame
from TileType import TileType
from Tile import Tile
from entite import *

# pygame setup
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Terraria')

clock = pygame.time.Clock()
FPS = 60

player = Player(200, 200, 0.1, 5)

moving_left = False
moving_right = False
running = True
dt = 0


# Charger et redimensionner chaque texture
textures = {
    TileType.DIRT: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/dirt.jpeg"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
}
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
tiles = [] 
for i in range(20):
    tiles.append(Tile(i, 18, TileType.DIRT))
while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                player.jump = True
            if event.key == pygame.K_ESCAPE:
                running = False
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
                
    pygame.display.update()
    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    for row in tiles:
        row.render(screen,textures)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_q]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()