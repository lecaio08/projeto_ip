import pygame           # biblioteca principal do pygame
import os               # manipulação de caminhos e arquivos do sistema
from settings import *  # configuracoes globais

class UI:

    def __init__(self, screen): # inicializa a tela 
        self.screen    = screen  # referência a tela principal
        self.font_path = os.path.join(FONTS_DIR, FONT_NAME)
        try: # vê se é possível utilizar uma fonte
            pygame.font.Font(self.font_path, 20)
        except: # se não conseguir, usa outra
            self.font_path = pygame.font.match_font('arial')

    def draw_text(self, text, size, color, x, y, align='center'): # desenha o texto na tela
        try: # tenta criar fonte personalizada
            font = pygame.font.Font(self.font_path, size)
        except: # se não conseguir, usa uma já existente 
            font = pygame.font.SysFont('arial', size)
            
        surface = font.render(str(text), True, color) # renderiza o texto
        rect    = surface.get_rect()                  # cria o retângulo do texto  
        
        if align == 'center':  rect.midtop    = (x, y) # centraliza e alinha à direita e à esquerda 
        elif align == 'right': rect.topright  = (x, y)
        elif align == 'left':  rect.topleft   = (x, y)
            
        self.screen.blit(surface, rect) # desenha o texto na tela

    def draw_hud(self, player, coins, start_time):
        
        elapsed     = (pygame.time.get_ticks() - start_time) / 1000 # tepo decorrido e restante
        remaining   = max(0.0, GAME_DURATION - elapsed)
        color_time  = RED if remaining < 10 else WHITE # define a cor do texto do tempo em relação ao tempo faltante
        self.draw_text(f"Tempo: {remaining:.1f}", 20, color_time, 20, 10, align='left') # alinha o tempo restante e a quantidade de vidas
        self.draw_text(f"Vidas: {player.lives}", 24, WHITE, WIDTH/2, 10, align='center')
        right_x     = WIDTH - 20        
        color_apple = GREEN if player.apples > 0 else WHITE # define a cor de um dos colecionáveis
        self.draw_text(f"Maçã: {player.apples}/3", 18, color_apple, right_x, 10, align='right')
        
        if player.lives < 3 and player.apples > 0: # se puder curar
             self.draw_text("[A] Curar!", 14, GREEN, right_x, 28, align='right')
        
        martelo_status = 1 if player.has_hammer else 0 # estado do martelo
        color_hammer   = YELLOW if player.has_hammer else WHITE
        self.draw_text(f"Martelo: {martelo_status}/1", 18, color_hammer, right_x, 45, align='right')
        self.draw_text(f"Moedas: {coins}", 18, GOLD, right_x, 70, align='right') # moedas coletadas

    def screen_start(self): # desenha a tela inicial do jogo
        self.screen.fill(BLACK) # limpa a tela
        self.draw_text("Donkey Kong", 48, YELLOW, WIDTH/2, HEIGHT/4) # título
        self.draw_text("Aperte [ENTER] para jogar! | [O]: Opções", 22, WHITE, WIDTH/2, HEIGHT/2)
        pygame.display.flip() # atualiza
        return self._wait_key(['RETURN', 'o']) # aguarda a entrada do jogador

    def screen_settings(self): # exibe a tela de configurações do jogo
        self.screen.fill(BLACK) # limpa a tela
        self.draw_text("Configurações & Ajuda", 40, YELLOW, WIDTH/2, 50) # escreve no topo "Configurações & Ajuda"
        
        instrucoes = [ # lista de instruções com as strings que serão utlizadas no texto
            "--- CONTROLES ---",
            "Mover: Setas Direcionais",
            "Pular: [BARRA DE ESPAÇO]",
            "Subir/Descer: Setas Cima/Baixo",
            "[ESC]: Pausar o jogo",
            "",
            "--- ITENS ---",
            "Maçã: Pressione [A] para curar",
            "Martelo: Quebra Barris",
            "Moeda: Pontuação Extra"
        ]
        
        for i, linha in enumerate(instrucoes):
            self.draw_text(linha, 20, WHITE, WIDTH/2, 130 + (i * 35)) # esse cálculo oferece a altura, separando cada linha por 35 pixels de forma uniforme
            
        self.draw_text("Pressione [ESC] ou [ENTER] para voltar", 18, GRAY, WIDTH/2, HEIGHT - 50) # instruções sobre os comandos de saída
        pygame.display.flip()
        self._wait_key(['RETURN', 'ESCAPE']) # esperando o 'RETURN' (Enter) ou 'ESCAPE' (Esc) 
        return 'MENU' # indica que o loop principal vai voltar para a tela de menu do jogo

    def screen_pause(self): # exibe a tela de 'pause' do jogo
        overlay = pygame.Surface((WIDTH, HEIGHT)) # cria uma nova camada do tamanho da tela
        overlay.set_alpha(150) # define o grau de transparência, sendo 0 invisível e 255 completamente visível, o 150 deixa o fundo do jogo transparente, porém um pouco escuro
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0,0)) # desenha a transparência setada por cima do jogo "freezado"
        self.draw_text("Pausado", 48, YELLOW, WIDTH/2, HEIGHT/3) # exibe o texto "Pausado"
        self.draw_text("[C] Continuar", 25, WHITE, WIDTH/2, HEIGHT/2) # exibe o texto "[C] Continuar"
        self.draw_text("[S] Sair", 25, RED, WIDTH/2, HEIGHT/2 + 50) # exibe o texto "[S] Sair"
        pygame.display.flip()
        waiting = True
        while waiting: # loop esperando as teclas
            for event in pygame.event.get():
                if event.type == pygame.QUIT: return 'QUIT'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c: return 'CONTINUE'  # se apertar "C" o jogo retoma
                    if event.key == pygame.K_s: return 'MENU' # se apertar "S" o jogo para e vai para o menu
                    
    def screen_gameover(self, won, coins, start_time): # exibe a tela de game over
        self.screen.fill(BLACK)
        title = "Você venceu!" if won else "GAME OVER!" # condicionais para qual título mostrar
        color = GREEN if won else RED
        
        remaining = max(0, GAME_DURATION - ((pygame.time.get_ticks() - start_time) / 1000)) # calcula quanto tempo sobrou
        score_base = int(remaining * 1000) # a pontuação será o tempo sobrado multiplicado por 1000
        bonus_moedas = 1 + (coins * 0.05) # bônus por moeda coletada, a qual cada moeda aumenta a pontuação em 5%
        
        if not won:
            final_score = int(coins * 100) # se perdeu, o score será a quantidade das moedas vezes 100
        else:
            final_score = int(score_base * bonus_moedas) # se ganhou, o score será o score base do tempo e multiplica pelo bônus das moedas
            
        self.draw_text(title, 48, color, WIDTH/2, HEIGHT/4) # exibe a tela (se ganhou ou perdeu)
        self.draw_text(f"Pontuação Final: {final_score}", 36, YELLOW, WIDTH/2, HEIGHT/2) # exibe a pontuação final
        self.draw_text("Enter para Menu", 18, WHITE, WIDTH/2, HEIGHT*3/4) # exibe a tecla para voltar ao menu
        pygame.display.flip()
        self._wait_key(['RETURN']) # aguarda o jogador apertar ENTER

    def _wait_key(self, keys): # função de espera
        waiting = True
        while waiting: # entra no loop até achar alguma ação
            for event in pygame.event.get():
                if event.type == pygame.QUIT: return 'QUIT' # verifica se o jogador "quitou" do jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and 'RETURN' in keys: return 'GAME' # verifica se o jogador quer entrar no jogo
                    if event.key == pygame.K_o and 'o' in keys: return 'SETTINGS' # verifica se o jogador quer entrar no menu de configurações
                    if event.key == pygame.K_ESCAPE and 'ESCAPE' in keys: return 'ESCAPE' # verifica se o jogador que está no menu de configurações quer voltar pro menu principal
        return None
