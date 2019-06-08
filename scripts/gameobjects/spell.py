import pygame
from scripts.utils.animation import Animation

class Spell(pygame.sprite.Sprite):

    def __init__(self, x, y):        
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('img/magic.png')        
        self.frames = []
        for yf in range(0, 5):
            for xf in range(0, 5):
                self.frames.append(self.img.subsurface((xf * 96, yf * 96, 96, 96)))
        
        self.animation = Animation(self.frames, 20)
        self.image = self.animation.get_frame()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y        
        self.x = x
        self.y = y

    def update(self, dt):        
        if self.animation.is_on_last_frame():
            self.kill()
        self.animation.update(dt)
        self.image = self.animation.get_frame() 
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.animation.get_frame(), self.rect)