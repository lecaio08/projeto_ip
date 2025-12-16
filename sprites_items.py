import pygame
from settings import *

# definindo a classe Item, que herda a classe Sprite do PyGame, aqui definiremos a lógica dos itens a serem pegos
class Item(pygame.sprite.Sprite):
    
    # definindo a constructor da classe, ao criar um item, passamos suas coordenadas e seeu tipo
    def __init__(self, x, y, type):
        # inicializa o Sprite base do Pygame
        super().__init__()
        self.type = type # tipo do item
        # criando o item visualmente, um pequeno quadrado 25x25
        self.image = pygame.Surface((25, 25))
        
        if type == 'apple':    
            self.image.fill(RED)   # se for maçã, pinta de vermelho
        elif type == 'hammer': 
            self.image.fill(GRAY)  # se for martelo, pinta de cinza
        elif type == 'coin':   
            self.image.fill(GOLD)  # se for moeda, pinta de dourado
        # o rect nos possibilita modificar facilmente os atributos do item criado, ref.: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect
        self.rect = self.image.get_rect()
        # centralizando o item na coordenada
        self.rect.center = (x, y)
