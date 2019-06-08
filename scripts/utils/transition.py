import pygame
import pygame.gfxdraw
from scripts.utils import tbpos
from scripts.utils.block import Block

class Transition:

    def __init__(self, sm):
        self.state_manager = sm
        self.blocks = []   
        for b in range(0, 25):
            self.blocks.append(tbpos.get_next_block())  
        self.blocks_draw_in_screen = 0
        self.blocks_hidden_in_screen = 0
        self.block_appear_delay = 200
        self.block_appear_count = 0
        self.block_hide_delay = 50
        self.block_hide_count = 0
        self.start_hiding_blocks = False
        self.start_showing_blocks = False

    def update(self, dt):
        if self.start_showing_blocks:
            update_block_count = 0
            self.block_appear_count += dt * 1000
            if self.block_appear_count >= self.block_appear_delay:
                if self.blocks_draw_in_screen <= 24:
                    self.blocks[self.blocks_draw_in_screen].set_hidden(True) # makes block obj update fade it in
                self.blocks_draw_in_screen += 1
                if self.blocks_draw_in_screen >= 55:
                    self.state_manager.set_current_state(self.state_manager.get_state_to_change())  # currently change to play state                  
                    self.start_hiding_blocks = True
            # make blocks update and update only the allowed ammount 
            for b in self.blocks:
                if update_block_count >= self.blocks_draw_in_screen:
                    break
                b.update(dt)        
                update_block_count += 1
            
            if self.start_hiding_blocks:
                self.show_screen(dt)

    def draw(self, screen):
        draw_block_count = 0
        for b in self.blocks:
            if draw_block_count >= self.blocks_draw_in_screen:
                break
            b.draw(screen)    
            draw_block_count += 1            
        
    def show_screen(self, dt):
        self.block_hide_count += dt * 1000
        if self.block_hide_count >= self.block_hide_delay:
            self.block_hide_count = 0
            if self.blocks_hidden_in_screen <= 24:
                self.blocks[self.blocks_hidden_in_screen].set_hidden(False) # makes block obj update fade it out
            self.blocks_hidden_in_screen += 1
            if self.blocks_hidden_in_screen >= 33: # gambiarra pra dar tempo pra todos os blocos sumirem                
                self.blocks_draw_in_screen = 0
                self.blocks_hidden_in_screen = 0
                self.start_hiding_blocks = False
                self.start_showing_blocks = False

    def set_start_hiding(self, decision):
        self.start_hiding_blocks = decision

    def set_start_showing(self, decision):
        self.start_showing_blocks = decision