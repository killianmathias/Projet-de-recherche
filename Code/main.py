import pygame
from TileType import TileType
from Tile import Tile
from entity import Player  # Assurez-vous d'importer votre classe Player
from World import World

# pygame setup
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Terraria')

clock = pygame.time.Clock()
FPS = 60

# Instancier le joueur (assurez-vous d'avoir une classe Player correcte)
player = Player(200, 200, 0.05, 5)

moving_left = False
moving_right = False
running = True
dt = 0

# Charger et redimensionner chaque texture
textures = {
    TileType.DIRT: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/dirt.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
    TileType.AIR: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/air.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
    TileType.GRASS: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/grass.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
    TileType.COAL: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/coal.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
    TileType.STONE: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/stone.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
    TileType.SAND: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/sand.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
    TileType.WATER: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/water.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
}

# Initialisation du monde
world = World(30, int(screen.get_height()/32), scale=20.0)  # Création du monde avec des dimensions 30x10
background = pygame.image.load("Code/textures/Background/1.png")
background = pygame.transform.scale(background, (1600, SCREEN_HEIGHT))  # Redimensionnement du fond

# Position initiale du joueur
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                player.jump()
            if event.key == pygame.K_ESCAPE:
                running = False
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False

    # Mise à jour du joueur
    player.move(moving_left, moving_right, world.terrain)

    # Affichage
    # Affichage du fond (scrolling basé sur la position du joueur)
    background_scroll = int(player.rect.x / 4)  # Ajuster la vitesse du fond
    screen.blit(background, (-background_scroll, 0))

    # Rendre le monde (terrain) sur l'écran
    world.render(screen, textures)

    # Rendre le joueur sur l'écran
    player.draw(screen)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Gestion du temps pour le FPS
    dt = clock.tick(FPS) / 1000

pygame.quit()