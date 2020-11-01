import pygame

from gameobject import GameObject
from block import Block
from collections import deque
from constants import *

class Bottle(GameObject):

    def __init__(self, x, y, color, blocks_numb=4):
        w = BLC_W+4
        h = BLC_H*(blocks_numb+0.5)
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.blocks_numb = blocks_numb
        self._blocks = deque([], maxlen=self.blocks_numb)

    def add_liquid(self, liquid: list) -> None:
        x, y = self.left+2, self.top+self.height-2
        for color in liquid:
            y -= BLC_H
            self._blocks.append(Block(x, y, BLC_W, BLC_H, color))
           

    def add_block(self, block: Block) -> None:
        if (len(self.blocks) == 0 or block.color == self.blocks[-1].color):
            self._blocks.append(block)
        #FIXME

    def minus_block(self) -> Block:
        return self._blocks.pop() #FIXME

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds, 2, 2)
        for b in self._blocks:
            b.draw(surface)