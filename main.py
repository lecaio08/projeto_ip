import pygame
import sys
# importando a classe principal Game, onde fora implementada a lógica do jogo
from game import Game

# instanciando a classe Game
g = Game()

# chamando a propriedade running da nossa classe pra rodar o loop do jogo
while g.running:
    # verificamos a propridade state da nossa classe pra fazer funcionar a máquina de estados
    if g.state == 'MENU':
        # chama o menu e espera ação do jogador
        action = g.ui.screen_start()
        
        if action == 'QUIT': 
            g.running = False
        elif action == 'GAME': 
            g.new_game()      # chamando a função new_game(), pra começar o jogo de fato
        elif action == 'SETTINGS': 
            g.state = 'SETTINGS'
            
    elif g.state == 'SETTINGS':
        # tela de configurações, quando o jogador sai dessa tela, volta automaticamente p/ menu
        g.ui.screen_settings()
        g.state = 'MENU' 

    elif g.state == 'PAUSE':
        # chama a tela de pause e espera ação do jogador
        action = g.ui.screen_pause()
        
        if action == 'QUIT':
            g.running = False
        elif action == 'MENU':
            g.state = 'MENU'
        elif action == 'CONTINUE':
            g.run() # chamando a função run() ao invés da new_game() por motivos óbvios

    elif g.state == 'GAMEOVER':
        # chama a tela final passando os dados da partida: moedas, tempo e se venceu ou não
        g.ui.screen_gameover(g.won, g.coins, g.start_time)
        g.state = 'MENU'

# fim do loop: mata o processo com o sys.exit()
pygame.quit()
sys.exit()

