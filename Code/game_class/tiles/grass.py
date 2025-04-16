import pygame
import os
from tiles.tile import Tile

class Grass(Tile):
    def __init__(self, x, y, position):
        super().__init__(x, y)
        self.is_solid = True
        self.position = position
        self.texture = textures[position]
        


#Charger les images d'un sprite
def load_animation_images():
    images = {}

    dossier = 'Code/textures/tiles/grass/'
    for nom_fichier in os.listdir(dossier):
        chemin_complet = os.path.join(dossier, nom_fichier)
        # Chargement de l'image
        image = pygame.image.load(chemin_complet)

        # Suppression de l'extension
        nom_sans_ext = os.path.splitext(nom_fichier)[0]  # 'grass-corner-left'

        # Extraction de la position : on prend tout après le premier tiret
        parties = nom_sans_ext.split('-')
        if len(parties) >= 2:
            position = '-'.join(parties[1:])  # 'corner-left'
            images[position] = image
        else:
            print(f"Nom de fichier inattendu : {nom_fichier}")

    return images

textures = load_animation_images()