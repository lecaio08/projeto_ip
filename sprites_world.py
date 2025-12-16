import pygame
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
        # cria o quadrado rosa
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 105, 180))
        # posiciona pelo centro pq é mais fácil de alinhar
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# definindo a classe Barrel, que herda a classe Sprite do PyGame. aqui criaremos o objeto dos barris
class Barrel(pygame.sprite.Sprite):
    # constructor da classe, passando as coordenadas e os limites de atuação dos barris
    def __init__(self, x, y, min_x, max_x):
        super().__init__()
        # criando um quadrado vermelho com um circulo no centro
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED) 
        pygame.draw.circle(self.image, (100, 0, 0), (15, 15), 15)
        
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
        
        # bate-volta do brassil
        if self.rect.right > self.max_x or self.rect.left < self.min_x:
            # inverte a direção => multiplicando a velocidade por -1
            self.vel_x *= -1

# O IDEAL É TER APENAS UMA CLASSE POR CÓDIGO, NÃO ESQUEÇA DE VER ISSO! VOCE NAO ESTUDOU MVC A TOA.
