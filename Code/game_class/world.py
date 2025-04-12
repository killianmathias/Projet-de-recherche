import random
import numpy as np
import pygame
from tiles.tile import Tile
from tiles.stone import Stone

from tiles.dirt import Dirt
from tiles.air import Air
from tiles.grass import Grass

@staticmethod 
def grille_aleatoire(width,height): # Méthode statique qui gènère une grille avec le bruit de Perlin
    tiles = [] # tableau de hauteurs
    for i in range (width): # On parcours le nombre de blocs de large que l'on veut générer
        tiles.append(abs(int(perlin_noise_octave(i/100,gradients)))) # On ajoute au tableau de hauteurs la hauteur générée par Perlin
    return tiles # On retourne le tableau

gradients = [random.random() * 2 - 1 for _ in range(1000)] # Tableau de gradients entre -1 et 1

def fade(t): # Fonction de fade qui adoucit le bruit de Perlin pour avoir des écarts de valeur de 1 maximum
    return t ** 3 * (t * (t * 6 - 15) + 10) # Formule mathématique de fade

def perlin_noise(x, gradients): # Fonction du bruit de Perlin
    x1 = int(x) # On récupère la valeur entière de x
    x2 = x1 + 1 # On récupère une deuxième valeur qui est la valeur entière de x +1
    t = x - x1 # On créé t qui est la différence entre les deux valeurs précédente
    fade_t = fade(t) # On applique la fonction de fade
    return 20*((1 - fade_t) * gradients[x1 % len(gradients)] + fade_t * gradients[x2 % len(gradients)]) # Formule de bruit de Perlin


def perlin_noise_octave(x, gradients, octaves=19, persistence=0.5):
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
    def __init__(self, width, height):
        self.width = width # Nombre de tuiles de large
        self.height = height//32 # Nombre de tuiles de hauteur / Taille d'une tuile
        self.terrain = self.generate() # Le terrain généré
        
 # Ensemble des textures de chaque tuile
        
    def generate(self): # Fonction qui génère le terrain
        grid = grille_aleatoire(self.width, self.height) # On génère notre tableau de hauteur 
        tiles = [] # Initialisation de notre grille de tuiles
        for i in range(self.width): # On parcours la largeur
            row = []  # Créer une nouvelle ligne pour chaque i
            for j in range(self.height+15): # On parcours la hauteur et on rajoute 15 de hauteur afin qu'il y ait au minimum 15 blocs sous le joueur
                if (j<(grid[i]+15)): # Si la valeur de j est inférieure à la valeur générée par Perlin 
                    if (j+1==(grid[i]+15)): # Si la prochaine valeur est la valeur générée par Perlin +15 alors on affiche de l'herbe
                        row.append(Grass(i*32,(self.height+1-j)*32));
                    else:
                        row.append(Dirt(i*32, (self.height+1-j)*32)) # Sinon on affiche de la terre
                else:
                    row.append(Air(i*32,(self.height-j)*32))  # Sinon on affiche de l'air
            tiles.append(row)  # Ajouter la ligne à tiles 
        return tiles # On retourne notre grille de tuiles

        

    
    def draw(self, screen): # Fonction qui affiche la grille de tuiles
        for x in range(self.width):
            for y in range(self.height+15):
                tile = self.terrain[x][y] # On récupère la tuile à la position [x][y]
                tile.draw(screen) # On appelle la fonction draw de chaque tuile
