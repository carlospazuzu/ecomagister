import pygame

class GroundCollisor(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/ground_collisor.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 570

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)