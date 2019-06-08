import pygame, sys, os
from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.mixer.pre_init(44100, -16, 1, 512) # makes pygame work without sound delay
pygame.init()
pygame.joystick.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
pygame.display.set_caption('PROJETO ECO-MAGISTER')
# need to be here because some modules wont work unless display mode is already set
from scripts.gamestates.statemanager import StateManager

FPS = 30
FPSClock = pygame.time.Clock()
dt = 0

game_state_manager = StateManager()

while True:

    for e in pygame.event.get():
        if e.type == KEYDOWN and e.key == K_ESCAPE:
            pygame.quit()
            sys.exit()        
        game_state_manager.handle_input(e)

    game_state_manager.update(dt)
    game_state_manager.draw(screen)

    pygame.display.update()
    dt = 1.0 / FPSClock.tick(FPS)