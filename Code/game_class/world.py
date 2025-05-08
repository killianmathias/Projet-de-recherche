import random
import numpy as np
import pygame
from tiles import *

@staticmethod 
def grille_aleatoire(width,height,gradients,multiplicateur): # Méthode statique qui gènère une grille avec le bruit de Perlin
    tiles = [] # tableau de hauteurs
    for i in range (width): # On parcours le nombre de blocs de large que l'on veut générer
        tiles.append(abs(int(height*0.7)+int(perlin_noise_octave(i/multiplicateur,gradients, height)))) # On ajoute au tableau de hauteurs la hauteur générée par Perlin
    return tiles # On retourne le tableau


def grille_perlin(width,height,gradients,multiplicateur):
    tiles = [] # tableau de hauteurs
    for i in range (width): # On parcours le nombre de blocs de large que l'on veut générer
        tiles.append((abs(int(height*0.7)+int(perlin_noise_octave(i/multiplicateur,gradients, height)))-35)/22) # On ajoute au tableau de hauteurs la hauteur générée par Perlin
    return tiles # On retourne le tableau

def fade(t): # Fonction de fade qui adoucit le bruit de Perlin pour avoir des écarts de valeur de 1 maximum
    return t ** 3 * (t * (t * 6 - 15) + 10) # Formule mathématique de fade

def perlin_noise(x, gradients): # Fonction du bruit de Perlin
    x1 = int(x) # On récupère la valeur entière de x
    x2 = x1 + 1 # On récupère une deuxième valeur qui est la valeur entière de x +1
    t = x - x1 # On créé t qui est la différence entre les deux valeurs précédente
    fade_t = fade(t) # On applique la fonction de fade
    return 20*((1 - fade_t) * gradients[x1 % len(gradients)] + fade_t * gradients[x2 % len(gradients)]) # Formule de bruit de Perlin


def perlin_noise_octave(x, gradients,octaves=19, persistence=0.5):
    total = 0 # Future somme des valeurs obtenues par le bruit de Perlin
    frequency = 1 # Fréquence 
    amplitude = 1 # Amplitude du bruit qui augmentera de tour en tour
    max_value = 0  # Utilisé pour normaliser le bruit

    for _ in range(octaves): # Nombre de fois que l'on appelle la fonction de perlin
        total += perlin_noise(x * frequency, gradients) * amplitude # On ajoute le résultat obtenu à la somme
        max_value += amplitude # On rajoute au nombre de valeur calculée l'amplitude
        amplitude *= persistence # On multiplie l'amplitude par la persistence
        frequency *= 2 # On multiplie la fréquence par 2

    return total / max_value  # Normalisation 



class World():
    def __init__(self, width, height, seed):
        self.width = width # Nombre de tuiles de large
        self.height = height//32 # Nombre de tuiles de hauteur / Taille d'une tuile
        random.seed(seed)
        self.gradients = [random.random() * 2 - 1 for _ in range(width)]
        self.temp_gradients = [random.random() * 2 - 1 for _ in range(width)] # Tableau de gradients entre -1 et 1
        self.humidity_gradients = [random.random() * 2 - 1 for _ in range(width)]
        self.heights =[]
        self.biomes = []
        self.terrain = self.generate() # Le terrain généré
        
        
 # Ensemble des textures de chaque tuile
        
    def generate(self): # Fonction qui génère le terrain
        grid = grille_aleatoire(self.width, self.height, self.gradients,100) # On génère notre tableau de hauteur 
        self.heights = grid
        temperature = grille_perlin(self.width, self.height, self.temp_gradients,300)
        humidity = grille_perlin(self.width, self.height, self.humidity_gradients,300)

        for i in range(self.width):
            t = temperature[i]
            h = humidity[i]
            terrain_height = grid[i]
            normalized_height = terrain_height / self.height
            biome = self.get_biome_from(t, h, normalized_height)
            self.biomes.append(biome) 
        tiles = [] # Initialisation de notre grille de tuiles
        for i in range(self.width): # On parcours la largeur
            row = []  # Créer une nouvelle ligne pour chaque i
            for j in range(self.height): # On parcours la hauteur et on rajoute 15 de hauteur afin qu'il y ait au minimum 15 blocs sous le joueur

                if (j<(grid[i])):
                    if(self.biomes[i]=="desert"):
                        if (j+1==(grid[i])): # Si la prochaine valeur est la valeur générée par Perlin +15 alors on affiche de l'herbe
                            if (i>0 and grid[i-1]<grid[i] and i< len(grid) -1 and grid[i+1]<grid[i]):
                                row.append(Sand(i*32,(self.height+1-j)*32,'top-left-right'))
                            elif (i>0 and grid[i-1]<grid[i]):
                                row.append(Sand(i*32,(self.height+1-j)*32,'corner-left'))
                            elif (i< len(grid) -1 and grid[i+1]<grid[i]):
                                row.append(Sand(i*32,(self.height+1-j)*32,'corner-right'))
                            else:
                                row.append(Sand(i*32,(self.height+1-j)*32,'top'))
                        else:
                            row.append(Sand(i*32,(self.height+1-j)*32,'base')) # Si la valeur de j est inférieure à la valeur générée par Perlin
                    else:
                        if (j+1==(grid[i])): # Si la prochaine valeur est la valeur générée par Perlin +15 alors on affiche de l'herbe
                            if (i>0 and grid[i-1]<grid[i] and i< len(grid) -1 and grid[i+1]<grid[i]):
                                row.append(Grass(i*32,(self.height+1-j)*32,'top-left-right',self.biomes[i]))
                            elif (i>0 and grid[i-1]<grid[i]):
                                row.append(Grass(i*32,(self.height+1-j)*32,'corner-left',self.biomes[i]))
                            elif (i< len(grid) -1 and grid[i+1]<grid[i]):
                                row.append(Grass(i*32,(self.height+1-j)*32,'corner-right',self.biomes[i]))
                            else:
                                row.append(Grass(i*32,(self.height+1-j)*32,'base',self.biomes[i]))
                        else:
                            if ((j+2)==(grid[i])):
                                if (i>0 and grid[i-1]<grid[i]):
                                    row.append(Dirt(i*32,(self.height+1-j)*32,'corner-left', self.biomes[i]))
                                elif (i< len(grid)-1 and grid[i+1]<grid[i]):
                                    row.append(Dirt(i*32,(self.height+1-j)*32,'corner-right', self.biomes[i]))
                                else:
                                    row.append(Dirt(i*32,(self.height+1-j)*32,'base', self.biomes[i]))
                            else:
                                row.append(Dirt(i*32,(self.height+1-j)*32,'base', self.biomes[i]))
                else:
                    row.append(Air(i*32,(self.height-j)*32))  # Sinon on affiche de l'air
            tiles.append(row)  # Ajouter la ligne à tiles

        
        return tiles # On retourne notre grille de tuiles

    def get_biome_from(self, temp, humidity, height):
        if height > 0.85:
            return "toundra"
        elif temp > 0.7:
            if humidity > 0.5:
                return "jungle"
            else:
                return "desert"
        elif temp > 0.4:
            return "plaine"
        else:
            if humidity > 0.5:
                return "taiga"
            else:
                return "toundra"
            
    
    def draw(self, screen, camera,group): # Fonction qui affiche la grille de tuiles
        for tile in group: # On récupère la tuile à la position [x][y]
                tile.can_touch = False
                if camera.rect.colliderect(tile.rect):
                    tile.draw(screen, camera) # On appelle la fonction draw de chaque tuile
