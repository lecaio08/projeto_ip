import pygame
import os
from PIL import Image
from settings import *

# definindo a classe Platform, que herda a classe Sprite do PyGame. aqui criaremos o objeto da plataforma (é um jogo de plataforma ne)
class Platform(pygame.sprite.Sprite):
    # definindo a constructor da classe, passando as coordenadas das plataformas e as dimensões
    def __init__(self, x, y, w, h):
        super().__init__()
        # como ainda não temos a arte do mapa, em vez de carregar uma imagem, criamos uma superfície vazia com a largura (w) e altura (h) que pedimos.
        self.image = pygame.Surface((w, h))
        self.image.fill(BROWN) # pinta tudo de marrom
        # criando o rect: (surface, cor, (x, y, largura, altura))
        pygame.draw.rect(self.image, (100, 50, 10), (0, 0, w, 5))
        # propriedades do rect
        self.rect   = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# definindo a classe Ladder, que herda a classe Sprite do PyGame. aqui criaremos o objeto da escada
class Ladder(pygame.sprite.Sprite):
    # definindo a constructor da classe, passando as coordenadas das escadas e a altura
    def __init__(self, x, y, h):
        super().__init__()
        # criando uma superficie estreita e com a altura determinada
        self.image = pygame.Surface((40, h))
        self.image.fill(BROWN)
        # com essa função, basicamente dizemos que tudo o que for marrom e estiver apoiado sob a ponte, deve ficar invisivel
        self.image.set_colorkey(BROWN)
        # desenha as hastes da escada
        pygame.draw.line(self.image, BLACK, (0,0), (0,h), 4)   # haste esquerda
        pygame.draw.line(self.image, BLACK, (38,0), (38,h), 4) # haste direita
        
        # percorre a escada inteira e cada 20 pixels desenha 1 degrau
        for i in range(0, h, 20):
            pygame.draw.line(self.image, BLACK, (0, i), (40, i), 3) 
        # posiciona a base da escada na coordenada pedida
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y + h)

# definindo a classe Ladder, que herda a classe Sprite do PyGame. aqui criaremos o objeto da peaches (no caso, um simples quadrado rosa que ao ser alcançado acaba o jogo)
class Goal(pygame.sprite.Sprite):
    # constructor da classe, passando somente as coordeenadas
    def __init__(self, x, y):
        super().__init__()
        

        self.frames          = []
        self.current_frame   = 0
        self.animation_speed = 0.15 # velocidade da troca de frame
        
        path_goal = os.path.join(ASSETS_DIR, "gifs/byte.gif")
        
        try:
            gif = Image.open(path_goal)
            for i in range(gif.n_frames):
                gif.seek(i)
                frame = gif.convert("RGBA")
                raw = frame.tobytes("raw", "RGBA")
                surface = pygame.image.fromstring(raw, gif.size, "RGBA")
                surface = pygame.transform.scale(surface, (50, 50))
                self.frames.append(surface)
            self.image = self.frames[0]
        except Exception as e:
            self.image = pygame.Surface((40, 40))
            self.image.fill((255, 105, 180))
            print(f"Erro ao carregar o GIF do Goal: {e}")

        # posiciona pelo centro pq é mais fácil de alinhar
        self.rect        = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        if len(self.frames) > 1:
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
            self.image = self.frames[int(self.current_frame)]

# definindo a classe Barrel, que herda a classe Sprite do PyGame. aqui criaremos o objeto dos barris
class Barrel(pygame.sprite.Sprite):
    # constructor da classe, passando as coordenadas e os limites de atuação dos barris
    def __init__(self, x, y, min_x, max_x):
        super().__init__()
        
        self.frames          = []
        self.current_frame   = 0
        self.animation_speed = 0.2 # Velocidade da rotação/animação do barril
        
        path_barrel = os.path.join(ASSETS_DIR, "gifs/Serra_circular.gif")
        
        try:
            gif = Image.open(path_barrel)
            for i in range(gif.n_frames):
                gif.seek(i)
                frame = gif.convert("RGBA")
                raw = frame.tobytes("raw", "RGBA")
                surface = pygame.image.fromstring(raw, gif.size, "RGBA")
                surface = pygame.transform.scale(surface, (30, 30))
                self.frames.append(surface)
            self.image = self.frames[0]
        except Exception as e:
            # criando um quadrado vermelho com um circulo no centro (prototipo)
            self.image = pygame.Surface((30, 30))
            self.image.fill(RED) 
            pygame.draw.circle(self.image, (100, 0, 0), (15, 15), 15)
            print(f"Erro ao carregar o GIF do Barrel: {e}")
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        # movimento do barril
        self.vel_x = 3      # velocidade horizontal (3 pixels/frame)
        self.min_x = min_x  # limite esquerdo de rolamento
        self.max_x = max_x  # limite direito de rolamento

    # funçãoo pra atualizar a posição do barril a cada frame
    def update(self):
        # x = xo + vt
        self.rect.x += self.vel_x
        
        # bate-volta
        if self.rect.right > self.max_x or self.rect.left < self.min_x:
            # inverte a direção => multiplicando a velocidade por -1
            self.vel_x *= -1

        if self.frames:
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
            self.image = self.frames[int(self.current_frame)]
            
            # espelha o GIF se o barril estiver indo para a esquerda para parecer que está rolando
            if self.vel_x < 0:
                self.image = pygame.transform.flip(self.image, True, False)

