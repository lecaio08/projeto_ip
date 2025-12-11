import pygame
from settings import *

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        super().__init__()
        self.game            = game
        self.image           = pygame.Surface((30, 40))
        self.image.fill(PLAYER_COLOR)
        self.rect            = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        self.pos             = vec(x, y)
        self.vel             = vec(0, 0)
        self.acc             = vec(0, 0)
        self.lives           = 3
        self.apples          = 0       
        self.has_hammer      = False
        self.on_ladder       = False
        self.invulnerable    = False 
        self.last_hit        = 0

    def jump(self):
        if self.on_ladder:
            return

        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 2
        
        if hits:
            self.vel.y = PLAYER_JUMP_POWER

    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        keys     = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:  self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]: self.acc.x = PLAYER_ACC

        check_rect = self.rect.move(0, 10) 
        
        ladder_hits = []
        for ladder in self.game.ladders:
            if check_rect.colliderect(ladder.rect):
                ladder_hits.append(ladder)

        if ladder_hits:
            if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                self.on_ladder = True
                self.vel.x     = 0

        if self.on_ladder:
            self.acc.y = 0
            if keys[pygame.K_UP]: 
                self.vel.y = -CLIMB_SPEED
            elif keys[pygame.K_DOWN]: 
                self.vel.y = CLIMB_SPEED
            else: 
                self.vel.y = 0
            
            if not ladder_hits: 
                self.on_ladder = False
        
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel   += self.acc
        self.pos   += self.vel + 0.5 * self.acc
        
        if self.pos.x > WIDTH: self.pos.x = WIDTH
        if self.pos.x < 0:     self.pos.x = 0
        
        self.rect.midbottom = self.pos
        
        if self.invulnerable:
            if pygame.time.get_ticks() - self.last_hit > 2000: 
                self.invulnerable = False
                self.image.set_alpha(255) 
            else:
                if (pygame.time.get_ticks() // 200) % 2 == 0:
                    self.image.set_alpha(100)
                else:
                    self.image.set_alpha(255)
