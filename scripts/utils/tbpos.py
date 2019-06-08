import pygame
from scripts.utils.block import Block

# TBPOS stands for TRANSITION BLOCK POSITIONING and it is intended to
# keep track of all 25 blocks positions in the transition class manager
# besides, have an vector with proper appearing block sequence

blocks = []
for y in range(0, 5):
    for x in range(0, 5):
        blocks.append(Block(x * 160 + 0 * x, y * 120 + 0 * y))

# pao stand for PROPER APPEARING ORDER which is the proper block appering order
# to appear in the screen in order to "fade out" screen in transition process
pao_pos = -1
pao = [0, 1, 5, 2, 6, 10, 3, 7, 11, 15, 4, 8, 12, 16, 20, 9, 13, 17, 21, 14, 18, 22, 19, 23, 24]

def get_next_block():
    global pao_pos
    if pao_pos >= 25: 
        return 

    
    pao_pos += 1
    return blocks[pao[pao_pos]]