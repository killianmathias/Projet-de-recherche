import pygame
import os
from .tile import Tile

class Dirt(Tile):
    def __init__(self, x, y,position,biome):
        super().__init__(x, y)
        self.is_solid =True
        self.position = position
        self.texture = textures[biome][position]
    


def load_animation_images():
    base_folder = 'Code/textures/tiles/dirt'
    biome_textures = {}

    for biome in os.listdir(base_folder):
        biome_path = os.path.join(base_folder, biome)
        if not os.path.isdir(biome_path):
            continue  # Ignore les fichiers

        biome_textures[biome] = {}

        for filename in os.listdir(biome_path):
            file_path = os.path.join(biome_path, filename)

            if not filename.endswith(('.png', '.jpg', '.bmp')):
                continue  # Ignore les fichiers non image

            try:
                image = pygame.image.load(file_path)
            except pygame.error as e:
                print(f"Erreur de chargement de l'image {file_path}: {e}")
                continue

            # Enlève l'extension
            name_without_ext = os.path.splitext(filename)[0]
            parts = name_without_ext.split('-')

            if len(parts) >= 2:
                position = '-'.join(parts[1:])
                biome_textures[biome][position] = image
            else:
                print(f"Nom de fichier inattendu : {filename}")

    return biome_textures

textures = load_animation_images()