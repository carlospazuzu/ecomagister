import pygame
from pygame.locals import * 

class Hand(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.hand_states = {}
        self.hand_states['seek'] = pygame.image.load('img/hand_seek.png')
        self.hand_states['grab'] = pygame.image.load('img/hand_grab.png')
        self.image = self.hand_states['seek']
        self.rect = self.image.get_rect()
        # movement booleans
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False        
        self.SPEED = 250
        # initial sprite position
        self.rect.x = 400
        self.rect.y = 300
        # button is being pressed booleans
        self.button_is_pressed = False    

    def handle_input(self, event):
        if event.type == JOYAXISMOTION:
            # LEFT AND RIGHT
            if event.axis == 0 and event.value < 0:
                self.move_left = True
            if event.axis == 0 and event.value > 0:   
                self.move_right = True
            if event.axis == 0 and event.value == 0:
                self.move_left = False
                self.move_right = False
            # UP AND DOWN
            if event.axis == 1 and event.value < 0:
                self.move_up = True
            if event.axis == 1 and event.value > 0:   
                self.move_down = True
            if event.axis == 1 and event.value == 0:
                self.move_up = False
                self.move_down = False
        if event.type == JOYBUTTONDOWN:
            if event.button == 3:
                self.button_is_pressed = True
                previous_x = self.rect.x
                previous_y = self.rect.y
                self.image = self.hand_states['grab']
                self.rect = self.image.get_rect()
                self.rect.x = previous_x
                self.rect.y = previous_y
        if event.type == JOYBUTTONUP:
            if event.button == 3:
                self.button_is_pressed = False
                previous_x = self.rect.x
                previous_y = self.rect.y
                self.image = self.hand_states['seek']
                self.rect = self.image.get_rect()
                self.rect.x = previous_x
                self.rect.y = previous_y

    def update(self, dt):
        if self.move_up:
            self.rect.y -= self.SPEED * dt
        if self.move_down:
            self.rect.y += self.SPEED * dt
        if self.move_left:
            self.rect.x -= self.SPEED * dt
        if self.move_right:
            self.rect.x += self.SPEED * dt
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)