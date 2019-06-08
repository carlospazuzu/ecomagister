import pygame
from random import randint
from pygame.locals import *

class Trash(pygame.sprite.Sprite):

    def __init__(self, x, y, player):        
        pygame.sprite.Sprite.__init__(self)        
        g_options = ['plastic', 'metal', 'organic', 'glass', 'paper']
        g_chosen = g_options[randint(0, len(g_options) - 1)]
        self.type = g_chosen
        i_chosen = randint(1, 3)
        self.player = player
        self.image = pygame.image.load('img/garbage/' + g_chosen + '/' + str(i_chosen) +'.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.SPEED = 80
        self.temp = self.image.copy()
        #self.image.fill((154, 154, 155), None, BLEND_ADD)
        self.eventime = False
        self.is_colliding_with_player = False
        self.count = 0

    def get_type(self):
        return self.type

    def update(self, dt):       
        # checks if this trash is colliding with the player hand
        if pygame.sprite.collide_rect(self, self.player) and self.player.button_is_pressed:            
                self.is_colliding_with_player = True
        else:
            self.is_colliding_with_player = False

        if not self.is_colliding_with_player:
            self.count += dt * 1000        
            if self.count >= 300:
                self.count = 0
                self.eventime = not self.eventime

            self.rect.y += self.SPEED * dt
        else:
            if self.player.move_up:
                self.rect.y -= self.player.SPEED * dt
            if self.player.move_down:
                self.rect.y += self.player.SPEED * dt
            if self.player.move_left:
                self.rect.x -= self.player.SPEED * dt
            if self.player.move_right:
                self.rect.x += self.player.SPEED * dt
    
    # not actually used
    def draw(self, screen):                
        if self.eventime:
            screen.blit(self.temp, self.rect)
        else:            
            screen.blit(self.image, self.rect)