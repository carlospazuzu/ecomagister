import pygame
import pygame.gfxdraw

class Block:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 160
        self.height = 120
        self.alpha = 0
        self.rect_alpha = 255
        self.hidden = True        

    def update(self, dt):
        if self.hidden:
            self.fade_in(dt)
        else:
            self.fade_out(dt)        

    def draw(self, screen):
        pygame.gfxdraw.rectangle(screen, (self.x, self.y, self.width, self.height), (0, 0, 0, self.rect_alpha))
        pygame.gfxdraw.box(screen, (self.x, self.y, self.width, self.height), (0, 0, 0, self.alpha))

    def fade_in(self, dt):
        self.alpha += dt * 500
        # makes rectangle appear
        if self.rect_alpha < 255:
            self.rect_alpha = 255
        if self.alpha >= 255:
            self.alpha = 255
    
    def fade_out(self, dt):
        self.alpha -= dt * 700
        if self.alpha <= 0:
            self.alpha = 0
            self.rect_alpha = 0 # makes rectangle hide

    def set_hidden(self, hidden):
        self.hidden = hidden