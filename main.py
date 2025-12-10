import pygame
import sys
from game import Game

g = Game()
while g.running:
    if g.state == 'MENU':
        action = g.ui.screen_start()
        if action == 'QUIT': 
            g.running = False
        elif action == 'GAME': 
            g.new_game() 
        elif action == 'SETTINGS': 
            g.state = 'SETTINGS'            
    elif g.state == 'SETTINGS':
        g.ui.screen_settings()
        g.state = 'MENU' 
    elif g.state == 'PAUSE':
        action = g.ui.screen_pause()
        if action == 'QUIT':
            g.running = False
        elif action == 'MENU':
            g.state = 'MENU' 
        elif action == 'CONTINUE':
            g.run() 
    elif g.state == 'GAMEOVER':
        g.ui.screen_gameover(g.won, g.coins, g.start_time)
        g.state = 'MENU'

pygame.quit()
sys.exit()