import pygame            # biblioteca principal do pygame
import os                # manipulação de caminhos e arquivos do sistema
from PIL import Image    # biblioteca para manipulação de imagens e extração de frames de GIF
from settings import *   # configuracoes globais

class UI:

    def __init__(self, screen): # inicializa a tela 
        self.screen    = screen  # referência a tela principal
        self.font_path = os.path.join(FONTS_DIR, FONT_NAME)
        try: # tenta pegar a fonte de assets/fonts/font.ttf
            pygame.font.Font(self.font_path, 20)
        except: # se não conseguir, usa arial
            self.font_path = pygame.font.match_font('arial')

        # carregar o gif do menu
        self.menu_frames        = []
        self.current_menu_frame = 0
        path_menu               = os.path.join(ASSETS_DIR, "gifs/googfy-ah-menu-pixilart.gif") 
        try:
            gif = Image.open(path_menu)
            for frame_index in range(gif.n_frames):
                gif.seek(frame_index)
                frame_rgba = gif.convert("RGBA")
                str_frame = frame_rgba.tobytes("raw", "RGBA")
                surface = pygame.image.fromstring(str_frame, gif.size, "RGBA")
                surface = pygame.transform.scale(surface, (WIDTH, HEIGHT))
                self.menu_frames.append(surface)
        except:
            pass

        # carregar o gif de pause
        self.pause_frames        = []
        self.current_pause_frame = 0
        path_pause               = os.path.join(ASSETS_DIR, "gifs/pause.gif") # Certifique-se que o nome do arquivo está correto
        try:
            gif_p = Image.open(path_pause)
            for frame_index in range(gif_p.n_frames):
                gif_p.seek(frame_index)
                frame_rgba = gif_p.convert("RGBA")
                str_frame = frame_rgba.tobytes("raw", "RGBA")
                surface = pygame.image.fromstring(str_frame, gif_p.size, "RGBA")
                surface = pygame.transform.scale(surface, (WIDTH, HEIGHT))
                self.pause_frames.append(surface)
        except:
            pass

    # função pra escrever na tela
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
        waiting = True
        clock = pygame.time.Clock()
        
        while waiting:
            clock.tick(20) # Define a velocidade de animação do menu
            
            if self.menu_frames:
                self.current_menu_frame = (self.current_menu_frame + 1) % len(self.menu_frames)
                self.screen.blit(self.menu_frames[self.current_menu_frame], (0, 0))
            else:
                self.screen.fill(BLACK) 
                
            pygame.display.flip() 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'QUIT'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: return 'GAME'
                    if event.key == pygame.K_o: return 'SETTINGS'
        return None

    def screen_settings(self): # exibe a tela de configurações do jogo
        self.screen.fill(BLACK) # limpa a tela
        self.draw_text("Configurações & Ajuda", 40, YELLOW, WIDTH/2, 50) # escreve no topo "Configurações & Ajuda"
        
        instrucoes = [ # lista de instruções com as strings que serão utlizadas no texto
            "--- CONTROLES ---",
            "Mover: Setas Direcionais",
            "Pular: [BARRA DE ESPAÇO]",
            "Subir/Descer: Setas Cima/Baixo",
            "[P]: Pausar o jogo",
            "",
            "--- ITENS ---",
            "Maçã: Pressione [A] para curar",
            "Martelo: Quebra Barris",
            "Moeda: Pontuação Extra"
        ]
        
        for i, linha in enumerate(instrucoes):
            self.draw_text(linha, 20, WHITE, WIDTH/2, 130 + (i * 35)) 
            
        self.draw_text("Pressione [ESC] ou [ENTER] para voltar", 18, GRAY, WIDTH/2, HEIGHT - 50) 
        pygame.display.flip()
        self._wait_key(['RETURN', 'ESCAPE']) 
        return 'MENU' 

    def screen_pause(self): # exibe a tela de 'pause' do jogo
        waiting = True
        clock = pygame.time.Clock()
        
        while waiting:
            clock.tick(20) # Velocidade da animação de pause
            
            if self.pause_frames:
                # Desenha o GIF animado de pause
                self.current_pause_frame = (self.current_pause_frame + 1) % len(self.pause_frames)
                self.screen.blit(self.pause_frames[self.current_pause_frame], (0, 0))
            else:
                # Se não houver GIF, usa o overlay transparente padrão
                overlay = pygame.Surface((WIDTH, HEIGHT))
                overlay.set_alpha(150)
                overlay.fill(BLACK)
                self.screen.blit(overlay, (0,0))
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: return 'QUIT'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c: return 'CONTINUE'  
                    if event.key == pygame.K_s: return 'MENU' 
                    
    def screen_gameover(self, won, coins, start_time): # exibe a tela de game over
        self.screen.fill(BLACK)
        title = "Você venceu!" if won else "GAME OVER!" # condicionais para qual título mostrar
        color = GREEN if won else RED
        
        remaining = max(0, GAME_DURATION - ((pygame.time.get_ticks() - start_time) / 1000)) # calcula quanto tempo sobrou
        score_base = int(remaining * 1000) # a pontuação será o tempo sobrado multiplicado por 1000
        bonus_moedas = 1 + (coins * 0.05) # bônus por moeda coletada
        
        if not won:
            final_score = int(coins * 100) # se perdeu
        else:
            final_score = int(score_base * bonus_moedas) # se ganhou
            
        self.draw_text(title, 48, color, WIDTH/2, HEIGHT/4) 
        self.draw_text(f"Pontuação Final: {final_score}", 36, YELLOW, WIDTH/2, HEIGHT/2) 
        self.draw_text("Enter para Menu", 18, WHITE, WIDTH/2, HEIGHT*3/4) 
        pygame.display.flip()
        self._wait_key(['RETURN']) 

    def _wait_key(self, keys): # função de espera
        waiting = True
        while waiting: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: return 'QUIT' 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and 'RETURN' in keys: return 'GAME' 
                    if event.key == pygame.K_o and 'o' in keys: return 'SETTINGS' 
                    if event.key == pygame.K_ESCAPE and 'ESCAPE' in keys: return 'ESCAPE' 
        return None
