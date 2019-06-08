import pygame
from scripts.utils.animation import Animation

class Dirt(pygame.sprite.Sprite):

    def __init__(self, x, y):        
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('img/dirt.png')        
        self.frames = []
        for yf in range(0, 3):
            for xf in range(0, 6):
                self.frames.append(self.img.subsurface((xf * 128, yf * 128, 128, 128)))
        
        self.animation = Animation(self.frames, 1)
        self.image = self.animation.get_frame()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y        
        self.x = x - 20
        self.y = y - 20

    def update(self, dt):        
        if self.animation.is_on_last_frame():
            self.kill()
        self.animation.update(dt)
        self.image = self.animation.get_frame() 
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.animation.get_frame(), self.rect)