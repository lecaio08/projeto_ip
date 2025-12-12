import pygame
import os

# carregar a fonte
BASE_DIR   = os.path.dirname(__file__)         # load do diretório do projeto
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')  
FONTS_DIR  = os.path.join(ASSETS_DIR, 'fonts') # carrega o subdiretorio assets/fonts
FONT_NAME  = "font.ttf" 

# setando algumas variáveis que serão usadas em vários trechos do código, pra evitar ficar repetindo toda hora
WIDTH, HEIGHT     = 1080, 720
FPS               = 60
TITLE             = "Donkey Kong: Prototipo do Projeto"
GAME_DURATION     = 60
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
PLAYER_ACC        = 0.5
PLAYER_FRICTION   = -0.12
PLAYER_GRAVITY    = 0.8
PLAYER_JUMP_POWER = -15
CLIMB_SPEED       = 4
