import pygame
from scripts.gameobjects.trash import Trash
from random import randint

class TrashThrower:

    def __init__(self, player_ref):
        self.player_reference = player_ref
        self.trash_list = pygame.sprite.Group()
        self.time_ticker = 3000
        self.throw_delay = 3500
        self.keep_throwing = True

    def get_trash_list(self):
        #print('tamanho da lista = ' + str(len(self.trash_list)))
        return self.trash_list

    def update(self, dt):     
        if self.keep_throwing:   
            self.time_ticker += dt * 1000
            if self.time_ticker >= self.throw_delay:
                self.time_ticker = 0
                self.trash_list.add(Trash(randint(10, 720), -80, self.player_reference))      

            self.trash_list.update(dt)  

    def draw(self, screen):
        pass