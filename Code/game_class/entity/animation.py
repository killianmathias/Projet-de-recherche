import pygame
import random

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self,sprite_name):
        super().__init__()
        self.image = pygame.image.load(f"Code/textures/{sprite_name}/{sprite_name}0.png")
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False
        self.counter = 0

    def start_animation(self):
        self.animation = True


    def animate(self):
        
        if self.animation:
            self.counter+=1
            if (self.counter == 2):
                self.current_image += 1
                self.counter = 0
            

            if self.current_image >= len(self.images):
                self.animation = False
                self.current_image = 0
                

            image = self.images[self.current_image]
            if hasattr(self, 'facing_right') and self.facing_right:
                image = pygame.transform.flip(image, True, False)
            self.image = image
        


#Charger les images d'un sprite
def load_animation_images(sprite_name):
    images = []
    path = f"Code/textures/{sprite_name}/{sprite_name}"
    for num in range(0,16):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images

#Définir un dictionnaire qui va contenir les images chargées de chaque sprite
animations = {
    'player': load_animation_images('player')
}