import pygame
from settings import *

# recurso do PyGame pra facilitar o uso de vetores. ref.: https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2
vec = pygame.math.Vector2

# definindo a classe Player, que herda a classe Sprite do PyGame. aqui definiremos a lógica do jogador
class Player(pygame.sprite.Sprite):

    # definindo a constructor da classe, passando as coordenadas 
    def __init__(self, game, x, y):
        # inicializa o Sprite base do Pygame
        super().__init__()
        
        # referência ao objeto da classe Game
        self.game = game
        # cria um quadrado amarelo de 30x40 
        self.image = pygame.Surface((30, 40))
        self.image.fill(PLAYER_COLOR)
        # definindo o rect
        self.rect = self.image.get_rect()
        # define o spawn, canto inferior esquerdo
        self.rect.bottomleft = (x, y)
        # definindo os vetores posição (x, y), velocidade (vel) e Aceleração (acc)
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        # definindo os atributos do jogador
        self.lives      = 3     # vidas atuais
        self.apples     = 0     # inventário de maçãs
        self.has_hammer = False # se pegou o martelo
        # definindo os estados do jogador
        self.on_ladder    = False # tá na escada?
        self.invulnerable = False # tá piscando após levar dano?
        self.last_hit     = 0     # marca o tempo (em ms) do último dano

    # função pra fazer o personagem pular
    def jump(self):        
        # não pula se tiver subindo a escada
        if self.on_ladder:
            return
        # o pulo é mover o rect 2 pixels para baixo (temporariamente)
        self.rect.y += 2
        # verifica se colidiu com alguma plataforma
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        # move de volta para o lugar original
        self.rect.y -= 2
        
        # se houve colisão quando descemos 2 pixels, significa que estamos apoiados em algo, então, podemos pular!
        if hits:
            self.vel.y = PLAYER_JUMP_POWER # aplica força p cima
    # loop principal do jogador
    def update(self): 
        # definindo a gravidade do jogo
        self.acc = vec(0, PLAYER_GRAVITY)
        # pegar os inputs do teclado
        keys = pygame.key.get_pressed()
        # altera a aceleração horizontal com base nas setas
        if keys[pygame.K_LEFT]:  self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]: self.acc.x = PLAYER_ACC
        # # logica da escada: criação de um rect fictício (copia do rect do jogador) 10 pixels abaixo dele, pra verificar se o mesmo está tocando uma escada
        check_rect = self.rect.move(0, 10) 
        
        ladder_hits = []
        # percorre todas as escadas do jogo
        for ladder in self.game.ladders:
            if check_rect.colliderect(ladder.rect):
                ladder_hits.append(ladder)

        # se uma escada é detectada e o jogador apertou a seta p cima ou p baixo, impede a movimentação lateral
        if ladder_hits:
            if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                self.on_ladder = True
                self.vel.x = 0

        # comportamento enquanto está na escada
        if self.on_ladder:
            self.acc.y = 0 # anula a gravidade p/ não cair da escada
            
            # subida/descida
            if keys[pygame.K_UP]: 
                self.vel.y = -CLIMB_SPEED
            elif keys[pygame.K_DOWN]: 
                self.vel.y = CLIMB_SPEED
            else: 
                self.vel.y = 0 # se soltar a tecla, fica parado na escada
            
            # se saiu da área da escada, gravidade volta a agir normalmente
            if not ladder_hits: 
                self.on_ladder = False
        
        # definindo o atrito p/ evitar deslizamento. aceleração diminui proporcionalmente à velocidade atual
        self.acc.x += self.vel.x * PLAYER_FRICTION
        
        # v = vo + at
        self.vel += self.acc
        # x = xo + vt + a
        self.pos += self.vel + 0.5 * self.acc

        # determinando os limites da tela
        if self.pos.x > WIDTH: self.pos.x = WIDTH
        if self.pos.x < 0:     self.pos.x = 0
        
        # atualiza a hitbox p/ a nova posição calculada
        self.rect.midbottom = self.pos
        
        # se o jogador for acertado pelo barril, deixá-lo ivulnerável por 2s (efeito visual: levemente translucido)
        if self.invulnerable:
            if pygame.time.get_ticks() - self.last_hit > 2000: 
                self.invulnerable = False
                self.image.set_alpha(255) # volta a ficar totalmente opaco
            else:
                # jogador pisca após levar dano
                if (pygame.time.get_ticks() // 200) % 2 == 0:
                    self.image.set_alpha(100) # translucido
                else:
                    self.image.set_alpha(255) # opaco
