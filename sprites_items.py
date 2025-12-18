import pygame
import os
from PIL import Image
from settings import *

# definindo a classe Item, que herda a classe Sprite do PyGame, aqui definiremos a lógica dos itens a serem pegos
class Item(pygame.sprite.Sprite):
    
    # definindo a constructor da classe, ao criar um item, passamos suas coordenadas e seu tipo
    def __init__(self, x, y, type):
        # inicializa o Sprite base do Pygame
        super().__init__()
        self.type            = type
        self.frames          = []
        self.current_frame   = 0
        self.animation_speed = 0.15 

        # dicionário pra definir o tamanho do gif de cada coletável
        sizes = {
            'apple': (40, 40),
            'hammer': (40, 40), 
            'coin': (30, 30)
        }
        
        # default: 25x25
        self.size = sizes.get(type, (25, 25))

        # dicionario pro nome dos arquivos
        filenames = {
            'apple': "apple.png",
            'hammer': "martelo.png",
            'coin': "Moeda_IP.gif"
        }
        filename = filenames.get(type)
        
        # carrega o gif usando pillow
        path = os.path.join(ASSETS_DIR, "gifs", filename)
        try:
            gif = Image.open(path)
            for frame_index in range(gif.n_frames):
                gif.seek(frame_index)
                frame_rgba = gif.convert("RGBA")
                str_frame = frame_rgba.tobytes("raw", "RGBA")
                # converte para superfície do Pygame e aplica o tamanho personalizado
                surface = pygame.image.fromstring(str_frame, gif.size, "RGBA")
                surface = pygame.transform.scale(surface, self.size)
                self.frames.append(surface)
            
            self.image = self.frames[0]
        except Exception as e:
            # fallback em caso de erro no carregamento
            self.image = pygame.Surface(self.size)
            color = RED if type == 'apple' else GOLD if type == 'coin' else GRAY
            self.image.fill(color)
            print(f"Erro ao carregar {filename}: {e}")

        # o rect nos possibilita modificar facilmente os atributos do item criado
        self.rect = self.image.get_rect()
        # centralizando o item na coordenada
        self.rect.center = (x, y)

    def update(self):
        # se houver mais de um frame, anima o item
        if len(self.frames) > 1:
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
            self.image = self.frames[int(self.current_frame)]
