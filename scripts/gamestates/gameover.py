import pygame
from pygame.locals import *
import pygame.gfxdraw
from scripts.gamestates import playstate
from scripts.utils.animation import Animation

class GameOver:

    def __init__(self, sm):
        self.state_manager = sm        
        self.is_playstate_reset = False                
        self.final_score = -1
        self.frames = []
        for f in range(0, 24):
            self.frames.append(pygame.image.load('img/ending/frame_' + str(f) +'_delay-0.08s.gif'))
        self.animation = Animation(self.frames, 40)
        self.font = pygame.font.Font('fonts/8-bit-Madness.ttf', 58)
        self.font36 = pygame.font.Font('fonts/8-bit-Madness.ttf', 36)

    def set_final_score(self, score):
        self.final_score = score

    def handle_input(self, event):
        if event.type == JOYBUTTONDOWN:      
            pygame.mixer.music.fadeout(1000)                     
            self.state_manager.change_state(0)
            self.final_score = -1

    def update(self, dt):        
        if not pygame.mixer.music.get_busy() and self.final_score > -1:                        
            pygame.mixer.music.load('audio/music/ending.ogg')
            pygame.mixer.music.play(0)
        if not self.is_playstate_reset:
            self.state_manager.states.pop(2)
            self.state_manager.states.insert(2, playstate.PlayState(self.state_manager))
            self.is_playstate_reset = True
        self.animation.update(dt)

    def draw(self, screen):
        pygame.gfxdraw.box(screen, (0, 0, 800, 600), (23, 23, 23))
        screen.blit(self.animation.get_frame(), (145, 100))
        screen.blit(self.font.render('OBRIGADO POR JOGAR!', 0, (254, 254, 254)), (145, 45))
        screen.blit(self.font.render('SUA PONTUACAO FOI: ' + str(self.final_score), 0, (126, 248, 109)), (125, 420))
        screen.blit(self.font36.render('GRACAS A VOCE, O MUNDO E AGORA UM LUGAR MAIS LIMPO!', 0, (254, 254, 254)), (10, 500))
        screen.blit(self.font36.render('JOGO PRODUZIDO POR SUBMERSIVO GAME STUDIO', 0, (254, 254, 254)), (70, 540))