import random
import numpy as np
from TileType import TileType
from Tile import Tile
from pygame import *  # Pour générer le bruit de Perlin
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

# noise_values = []
# # Exemple d'utilisation
# for x in range(1000):
#     noise_values.append(int(perlin_noise_octave(x/100, gradients)))


class World():
    def __init__(self, width, height, scale=10.0):
        self.width = width
        self.height = height
        self.scale = scale
        self.terrain = self.generate()
        
    def generate(self):
        grid = grille_aleatoire(self.width, self.height)
        tiles = []
        for i in range(self.width):
            row = []  # Créer une nouvelle ligne pour chaque i
            for j in range(self.height):
                if (j<grid[i]):
                    if (j+1==grid[i]):
                        row.append(Tile(i,self.height-j,TileType.GRASS))
                    else:
                        row.append(Tile(i, self.height-j, TileType.DIRT))
                else:
                    row.append(Tile(i,self.height-j,TileType.AIR))  # Ajouter un nouvel objet Tile dans la ligne
            tiles.append(row)  # Ajouter la ligne à tiles
        return tiles

        

    
    def render(self, screen, textures):
        # Affichage du terrain
        for x in range(self.width):
            for y in range(self.height):
                tile = self.terrain[x][y]
                tile.render(screen, textures)
