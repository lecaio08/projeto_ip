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
        self._add(Platform(0, HEIGHT-40, WIDTH, 40), [self.platforms])
        self.player = Player(self, 100, HEIGHT-45)
        self.all_sprites.add(self.player)
        self._add(Platform(0, HEIGHT-200, WIDTH-150, 20), [self.platforms])
        self._add(Platform(150, HEIGHT-400, WIDTH-150, 20), [self.platforms])
        self._add(Ladder(WIDTH-200, HEIGHT-200, 160), [self.ladders])
        self._add(Ladder(200, HEIGHT-400, 200), [self.ladders])
        self._add(Goal(50, HEIGHT-550), [self.goals])
        self._add(Barrel(300, HEIGHT-215, 20, 600), [self.enemies])
        self._add(Item(600, HEIGHT-70, 'coin'), [self.items])
        self._add(Item(400, HEIGHT-430, 'hammer'), [self.items])
        self._add(Item(200, HEIGHT-70, 'apple'), [self.items])
        self._add(Item(500, HEIGHT-70, 'apple'), [self.items])

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
