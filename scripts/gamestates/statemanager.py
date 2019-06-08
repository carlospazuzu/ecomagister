import pygame
from scripts.gamestates import titlestate
from scripts.gamestates import explanationstate
from scripts.gamestates import playstate
from scripts.gamestates import gameover
from scripts.utils.transition import Transition

class StateManager:

    def __init__(self):
        self.states = []        
        self.states.append(titlestate.TitleState(self)) # STATE 0 TITLE SCREEN
        self.states.append(explanationstate.ExplanationState(self)) # STATE 1 EXPLANATION SCREEN
        self.states.append(playstate.PlayState(self)) # STATE 2 GAMEPLAY SCREEN        
        self.states.append(gameover.GameOver(self)) # STATE 3 GAMEOVER SCREEN        
        self.current_state = 0
        self.state_to_change = None
        self.transition = Transition(self)                
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()                    

    def change_state(self, state):
        self.state_to_change = state
        self.transition.set_start_showing(True)

    def get_state_to_change(self):
        return self.state_to_change

    # reachable only inside change_state method
    def set_current_state(self, state):
        self.current_state = state

    def get_joystick(self):
        return self.joystick

    def handle_input(self, event):
        self.states[self.current_state].handle_input(event)

    def update(self, dt):        
        self.states[self.current_state].update(dt)
        self.transition.update(dt)

    def draw(self, screen):
        self.states[self.current_state].draw(screen)
        self.transition.draw(screen)        