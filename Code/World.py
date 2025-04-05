import random
import numpy as np
from TileType import TileType
from tile import Tile
import pygame

@staticmethod
def grille_aleatoire(width,height):
    tiles = []
    for i in range (width):
        tiles.append(abs(int(perlin_noise_octave(i/100,gradients))))
    return tiles

gradients = [random.random() * 2 - 1 for _ in range(1000)]

def fade(t):
    return t ** 3 * (t * (t * 6 - 15) + 10)

def perlin_noise(x, gradients):
    x1 = int(x)
    x2 = x1 + 1
    t = x - x1
    fade_t = fade(t)
    return 20*((1 - fade_t) * gradients[x1 % len(gradients)] + fade_t * gradients[x2 % len(gradients)])


def perlin_noise_octave(x, gradients, octaves=19, persistence=0.5):
    total = 0
    frequency = 1
    amplitude = 1
    max_value = 0  # Utilisé pour normaliser le bruit

    for _ in range(octaves):
        total += perlin_noise(x * frequency, gradients) * amplitude
        max_value += amplitude
        amplitude *= persistence
        frequency *= 2

    return total / max_value  # Normalisation



class World():
    def __init__(self, width, height):
        self.width = width
        self.height = height//32
        self.terrain = self.generate()
        self.textures = {TileType.DIRT: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/dirt.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
    TileType.AIR: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/air.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
    TileType.GRASS: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/grass.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
    TileType.COAL: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/coal.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
    TileType.STONE: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/stone.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
    TileType.SAND: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/sand.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
    TileType.WATER: pygame.transform.scale(pygame.image.load("Code/textures/Tiles/water.png"), (Tile.TILE_SIZE, Tile.TILE_SIZE)),
}
        
    def generate(self):
        grid = grille_aleatoire(self.width, self.height)
        tiles = []
        for i in range(self.width):
            row = []  # Créer une nouvelle ligne pour chaque i
            for j in range(self.height+15):
                if (j<(grid[i]+15)):
                    if (j+1==(grid[i]+15)):
                        row.append(Tile(i*32,(self.height+1-j)*32,TileType.GRASS))
                    else:
                        row.append(Tile(i*32, (self.height+1-j)*32, TileType.DIRT))
                else:
                    row.append(Tile(i*32,(self.height-j)*32,TileType.AIR))  # Ajouter un nouvel objet Tile dans la ligne
            tiles.append(row)  # Ajouter la ligne à tiles
        return tiles

        

    
    def draw(self, screen, camera_x, camera_y):
        for x in range(self.width):
            for y in range(self.height):
                tile = self.terrain[x][y]
                tile.draw(screen, self.textures, camera_x, camera_y)
