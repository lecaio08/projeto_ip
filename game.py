import pygame
from settings import *
from sprites_player import Player
from sprites_world import Platform, Ladder, Goal, Barrel
from sprites_items import Item
from interface import UI

class Game:

    def __init__(self):
        pygame.init()
        self.screen  = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock   = pygame.time.Clock()
        self.running = True
        self.state   = 'MENU'
        self.ui      = UI(self.screen)

    def new_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms   = pygame.sprite.Group()
        self.ladders     = pygame.sprite.Group()
        self.items       = pygame.sprite.Group()
        self.enemies     = pygame.sprite.Group() 
        self.goals       = pygame.sprite.Group()
        self.coins       = 0
        self.start_time  = pygame.time.get_ticks()
        self.won         = False
        self._create_level()
        self.run()

    def _create_level(self):

        # Lugar de inicialização do personagem controlável 
        self._add(Platform(0, HEIGHT-40, WIDTH, 40), [self.platforms])
        self.player = Player(self, 100, HEIGHT-45)
        self.all_sprites.add(self.player)

        # Plataformas
        # self._add(Platform(0, HEIGHT-200, WIDTH-150, 20), [self.platforms])  # Plataforma inferior
        # self._add(Platform(150, HEIGHT-400, WIDTH-150, 20), [self.platforms]) # Plataforma superior
        
            # teste 
        self._add(Platform(0,HEIGHT-200, 150, 20), [self.platforms]) # Plataforma 1
        self._add(Platform(250, HEIGHT-250, 100, 20), [self.platforms]) # Plataforma 2
        self._add(Platform(500, HEIGHT-300, 250, 20), [self.platforms]) # Plataforma 3
        self._add(Platform(210, HEIGHT-390,220, 20), [self.platforms]) # Plataforma 4
        self._add(Platform(900, HEIGHT-220,160,20), [self.platforms]) # Plataforma 5
        self._add(Platform(850, HEIGHT-450, 230, 20), [self.platforms]) # Plataforma 6 
        self._add(Platform(0, HEIGHT-450, 100, 20), [self.platforms]) # Plataforma 7
        self._add(Platform(450, HEIGHT-520, 340, 20), [self.platforms]) # Plataforma 8
        self._add(Platform(80, HEIGHT-600, 500, 20), [self.platforms]) # Plataforma 9
        self._add(Platform(300, HEIGHT-680, 50, 20), [self.platforms]) # Plataforma 10


        # Escadas
        # self._add(Ladder(WIDTH-200, HEIGHT-200, 160), [self.ladders])
        # self._add(Ladder(200, HEIGHT-400, 150), [self.ladders])

            # teste
        self._add(Ladder(125, HEIGHT-180, 80), [self.ladders]) # Escada - Plataforma 1
        self._add(Ladder(520, HEIGHT-280, 90), [self.ladders]) # Escada - Plataforma 3
        self._add(Ladder(890, HEIGHT-430, 80), [self.ladders]) # Escada - Plataforma 6
        self._add(Ladder(80, HEIGHT-430, 50), [self.ladders]) # Escada - Plataforma 7
        self._add(Ladder(500, HEIGHT-500, 70), [self.ladders]) # Escada - Plataforma 8

        # Posição do objetivo 
        self._add(Goal(325, HEIGHT-700), [self.goals])

        # Inimigos  
        self._add(Barrel(800, HEIGHT-55, 750, 1000), [self.enemies])
        self._add(Barrel(550, HEIGHT-315, 500, 750), [self.enemies])
        self._add(Barrel(260, HEIGHT-405, 210, 430), [self.enemies])
        self._add(Barrel(500, HEIGHT-535, 450, 790), [self.enemies])
        self._add(Barrel(750, HEIGHT-535, 450, 790), [self.enemies])
        self._add(Barrel(500, HEIGHT-615, 120, 540), [self.enemies])

        # Itens
        self._add(Item(1030, HEIGHT-470, 'hammer'), [self.items])
        self._add(Item(30, HEIGHT-220, 'apple'), [self.items])
        self._add(Item(1040, HEIGHT-240, 'apple'), [self.items])
        self._add(Item(20, HEIGHT-470, 'apple'), [self.items])
        self._add(Item(960, HEIGHT-240, 'coin'), [self.items])
        self._add(Item(920, HEIGHT-240, 'coin'), [self.items])
        self._add(Item(570, HEIGHT-540, 'coin'), [self.items])
        self._add(Item(630, HEIGHT-540, 'coin'), [self.items])
        self._add(Item(690, HEIGHT-540, 'coin'), [self.items])
        self._add(Item(280, HEIGHT-270, 'coin'), [self.items])
        self._add(Item(30, HEIGHT-600, 'coin'), [self.items])
        self._add(Item(230, HEIGHT-410, 'coin'), [self.items])

    def _add(self, sprite, groups):
        self.all_sprites.add(sprite)
        for g in groups: g.add(sprite)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        
        if self.player.vel.y > 0 and not self.player.on_ladder:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                
                if self.player.pos.y < lowest.rect.bottom:
                    self.player.pos.y      = lowest.rect.top
                    self.player.vel.y      = 0
                    self.player.rect.midbottom = self.player.pos

        if not self.player.invulnerable:
            hit_enemies = pygame.sprite.spritecollide(self.player, self.enemies, False)
            if hit_enemies:
                if self.player.has_hammer:
                    hit_enemies[0].kill()
                else:
                    self.player.lives       -= 1
                    self.player.invulnerable = True
                    self.player.last_hit     = pygame.time.get_ticks()
                    self.player.vel.y        = -10 
                    
                    if self.player.lives <= 0:
                        self.playing = False
                        self.state   = 'GAMEOVER'
                        self.won     = False

        hits = pygame.sprite.spritecollide(self.player, self.items, False)
        for item in hits:
            if item.type == 'coin':
                self.coins += 1
                item.kill()
            elif item.type == 'hammer':
                self.player.has_hammer = True
                item.kill()
            elif item.type == 'apple':
                if self.player.apples < 3:
                    self.player.apples += 1
                    item.kill()

        if pygame.sprite.spritecollide(self.player, self.goals, False):
            self.won = True; self.playing = False; self.state = 'GAMEOVER'
        
        if (pygame.time.get_ticks() - self.start_time)/1000 > GAME_DURATION:
            self.playing = False; self.state = 'GAMEOVER'

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.playing = False; self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    self.state = 'PAUSE'; self.playing = False
                
                if event.key == pygame.K_SPACE:
                    self.player.jump()

                if event.key == pygame.K_a:
                    if self.player.lives < 3 and self.player.apples > 0:
                        self.player.lives += 1
                        self.player.apples -= 1

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.ui.draw_hud(self.player, self.coins, self.start_time)
        pygame.display.flip()
