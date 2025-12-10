import pygame 
from settings import *

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.type        = type
        self.image       = pygame.Surface((25, 25))
        if type == 'apple':    self.image.fill(RED)
        elif type == 'hammer': self.image.fill(GRAY)
        elif type == 'coin':   self.image.fill(GOLD)
        self.rect        = self.image.get_rect()
        self.rect.center = (x, y)