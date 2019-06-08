import pygame
from scripts.gameobjects.spell import Spell

class GarbageCan(pygame.sprite.Sprite):

    def __init__(self, x, y, type, player, playstate):        
        pygame.sprite.Sprite.__init__(self)
        self.player = player   
        self.type = type     
        self.playstate = playstate
        self.image = pygame.image.load('img/garbage_can/' + type + '_garbage_can.png')
        self.mistake_img = pygame.image.load('img/mistake.png')
        self.showing_mistake = False
        self.mistake_count = 1000
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.wrong_sound = pygame.mixer.Sound('audio/sfx/wrong.wav')
        self.right_sound = pygame.mixer.Sound('audio/sfx/right.wav')        

    def get_type(self):
        return self.type

    def is_colliding_with_player(self):
        return pygame.sprite.collide_rect(self, self.player)

    def is_player_pressing_button(self):
        return self.player.button_is_pressed

    def update(self, dt, trash_list):
        if self.is_colliding_with_player() and self.is_player_pressing_button():
            for collided in pygame.sprite.spritecollide(self, trash_list, True):                
                if self.get_type() == collided.get_type():
                    self.playstate.score_increaser += 150
                    self.playstate.spell_group.add(Spell(self.rect.x, self.rect.y))
                    self.right_sound.play()
                else:
                    self.showing_mistake = True
                    self.wrong_sound.play()

        if self.showing_mistake:            
            self.mistake_count -= dt * 1000
            if self.mistake_count <= 0:
                self.mistake_count = 1000
                self.showing_mistake = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)           
        if self.showing_mistake:            
            temp = self.rect
            screen.blit(self.mistake_img, (temp.x - 20, temp.y, temp.width, temp.height)) 