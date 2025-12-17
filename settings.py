import pygame
import os

# carregar a fonte
BASE_DIR   = os.path.dirname(__file__)         # Load do diretório do projeto
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')  
FONTS_DIR  = os.path.join(ASSETS_DIR, 'fonts') # Carrega o subdiretorio assets/fonts
FONT_NAME  = "font.ttf" 

# Configurando algumas variáveis que serão usadas em vários trechos do código, pra evitar ficar repetindo toda hora

# Resolução e reprodução de vídeo 
WIDTH, HEIGHT     = 1080, 720
FPS               = 60

# Características do jogo
TITLE             = "Donkey Kong: Prototipo do Projeto"
GAME_DURATION     = 60

# Coloração
WHITE             = (255, 255, 255) # código RGB
BLACK             = (0, 0, 0)
RED               = (220, 20, 60)
GOLD              = (255, 215, 0)
GRAY              = (128, 128, 128)
BROWN             = (139, 69, 19)
PLAYER_COLOR      = (50, 205, 50)
YELLOW            = (255, 255, 0)
GREEN             = (0, 255, 0)
BGCOLOR           = (20, 30, 50)

# Física do jogo 
PLAYER_ACC        = 0.5     # Movimentação do jogador 
PLAYER_FRICTION   = -0.12   # Atrito de desaceleração do jogador
PLAYER_GRAVITY    = 0.8     # Aceleração da gravidade
PLAYER_JUMP_POWER = -13     # Altura do salto 
CLIMB_SPEED       = 4       # Velocidade de escalada
