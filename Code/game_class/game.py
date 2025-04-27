import pygame
import random
import os
from entity import *
from world import *
from selector import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.current_background = pygame.Surface((1080, 720)).convert_alpha()
        self.next_background = None
        self.background_alpha = 255
        self.transitioning = False
        self.transition_speed = 5

        self.background = pygame.transform.scale(pygame.image.load("Code/textures/Background/plaine.png"), (1080, 720))
        self.current_background.blit(self.background, (0, 0))

        self.world = None
        self.player = Player(1080 * 16, 720, 1, 3)
        x_cam, y_cam = self.player.rect.center
        self.camera = Camera(x_cam, y_cam, 1080, 720)
        self.group = pygame.sprite.Group()

        self.ticks_count = 0
        self.fly = False
        self.seed = None
        self.game_start = False

        self.selector = Selector()

    def create_world(self, seed):
        self.world = World(1080, 2000, seed)
        for row in self.world.terrain:
            for tile in row:
                self.group.add(tile)
        self.game_start = True

    def draw_begin(self):
        self.screen.fill("black")
        self.screen.blit(self.current_background, (0, 0))
        pygame.display.flip()

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if not self.game_start and event.key == pygame.K_SPACE:
                    self.seed = random.randint(0, 0xFFFFFFFF)
                    self.create_world(self.seed)
                    self.game_start = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    if self.fly:
                        self.player.rect.center = self.camera.rect.center
                    self.fly = not self.fly

    def update(self):
        if not self.fly:
            self.player.update(self.group)

        self.camera.update(self.player.rect.center, self.fly)
        self.selector.update(self.group,self.camera,self.world)

        # Transition de background fluide
        biome = self.world.biomes[self.player.rect.x // 32]
        new_bg = pygame.transform.scale(backgrounds[biome], (1080, 720))

        if not self.transitioning and not pygame.Surface.get_buffer(self.current_background).raw == pygame.Surface.get_buffer(new_bg).raw:
            self.next_background = new_bg
            self.transitioning = True
            self.background_alpha = 0

        self.player.update_animation()
       

    def draw(self):
        self.screen.fill("black")

        if self.transitioning and self.next_background:
            temp_old = self.current_background.copy()
            temp_new = self.next_background.copy()

            temp_old.set_alpha(255 - self.background_alpha)
            temp_new.set_alpha(self.background_alpha)

            self.screen.blit(temp_old, (0, 0))
            self.screen.blit(temp_new, (0, 0))

            self.background_alpha += self.transition_speed
            if self.background_alpha >= 255:
                self.background_alpha = 255
                self.current_background = self.next_background
                self.next_background = None
                self.transitioning = False
        else:
            self.screen.blit(self.current_background, (0, 0))

        self.world.draw(self.screen, self.camera,self.group)
        self.player.draw(self.screen, self.camera)
        self.selector.draw(self.screen,self.camera)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            if not self.game_start:
                self.draw_begin()
            else:
                self.update()
                self.draw()
                self.clock.tick(60)


# Chargement des backgrounds par biome
def load_animation_images():
    images = {}
    dossier = 'Code/textures/Background/'
    for nom_fichier in os.listdir(dossier):
        if not nom_fichier.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
            continue

        chemin_complet = os.path.join(dossier, nom_fichier)
        image = pygame.image.load(chemin_complet)
        nom_sans_ext = os.path.splitext(nom_fichier)[0]
        images[nom_sans_ext] = pygame.transform.scale(image, (1080, 720))

    return images


# Initialisation du jeu
pygame.init()
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Terraria")
pygame.display.set_icon(pygame.image.load("Code/textures/icon.png"))

backgrounds = load_animation_images()

game = Game(screen)
game.run()
pygame.quit()