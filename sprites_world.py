import pygame
from settings import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image  = pygame.Surface((w, h))
        self.image.fill(BROWN)
        pygame.draw.rect(self.image, (100, 50, 10), (0, 0, w, 5))
        self.rect   = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Ladder(pygame.sprite.Sprite):
    def __init__(self, x, y, h):
        super().__init__()
        self.image = pygame.Surface((40, h))
        self.image.fill(BROWN)
        self.image.set_colorkey(BROWN)
        pygame.draw.line(self.image, BLACK, (0,0), (0,h), 4)
        pygame.draw.line(self.image, BLACK, (38,0), (38,h), 4)
        for i in range(0, h, 20):
            pygame.draw.line(self.image, BLACK, (0, i), (40, i), 3)
        self.rect           = self.image.get_rect()
        self.rect.midbottom = (x, y + h)

class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image       = pygame.Surface((40, 40))
        self.image.fill((255, 105, 180)) 
        self.rect        = self.image.get_rect()
        self.rect.center = (x, y)

class Barrel(pygame.sprite.Sprite):
    def __init__(self, x, y, min_x, max_x):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED) 
        
        pygame.draw.circle(self.image, (100, 0, 0), (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel_x = 3
        self.min_x = min_x
        self.max_x = max_x

    def update(self):
        self.rect.x += self.vel_x
        if self.rect.right > self.max_x or self.rect.left < self.min_x:
            self.vel_x *= -1