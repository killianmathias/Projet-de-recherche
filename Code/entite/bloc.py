import pygame
from .entity import Entity

class Bloc(Entity):
    def __init__(self, x, y, height):
        Entity.__init__(self, x, y, height, height, 'Code/img/bloc.png')
        
    def draw(self, screen):
        super().draw(screen)
        
    def update(self, blocs):
        return