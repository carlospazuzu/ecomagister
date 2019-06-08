import pygame

class ExplanationState:

    def __init__(self, sm):
        self.state_manager = sm
        self.bg = pygame.image.load('img/bg.jpg')

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))