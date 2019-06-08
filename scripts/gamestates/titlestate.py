import pygame
from pygame.locals import *
from scripts.utils import assetsmanager
from scripts.utils.animation import Animation

class TitleState:

    def __init__(self, sm):        
        self.state_manager = sm
        self.title_bg_animation = Animation(assetsmanager.get('TITLEGIF'), 30)  
        self.title_font = assetsmanager.get('EXPLANATION').render('APERTE ALGUM BOTAO', 0, (186, 214, 166)).convert()              
        self.title_alpha = 255
        self.decrease_alpha = True
        self.title_image = assetsmanager.get('TITLEIMG')

    def fade_title(self, dt):
        if self.title_alpha >= 255:
            self.decrease_alpha = True
        elif self.title_alpha <= 25:
            self.decrease_alpha = False

        if self.decrease_alpha:
            self.title_alpha -= 0.2 * dt * 1000
        else:
            self.title_alpha += 0.2 * dt * 1000

    def handle_input(self, event):        
        if event.type == JOYBUTTONDOWN:            
            self.state_manager.change_state(2)
            #self.state_manager.transition.set_start_showing(True)            

    def update(self, dt):
        self.fade_title(dt)
        self.title_font.set_alpha(self.title_alpha)
        self.title_bg_animation.update(dt)

    def draw(self, screen):
        screen.blit(self.title_bg_animation.get_frame(), (0, 0))
        screen.blit(self.title_font, (100, 500))
        screen.blit(self.title_image, (100, 50))

    
    