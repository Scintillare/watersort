import pygame

from gameobject import GameObject
from block import Block
from collections import deque
from typing import Iterable, List
from constants import *

class Bottle(GameObject):

    def __init__(self, x, y, color, blocks_numb=4):
        w = BLC_W+4
        h = BLC_H*(blocks_numb+0.5)
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.blocks_numb = blocks_numb
        self.is_fulled = False
        self._blocks = deque([], maxlen=self.blocks_numb)    

    def add_liquid(self, liquid: list) -> None:
        x, y = self.left+2, self.top+self.height-2
        for color in liquid:
            y -= BLC_H
            self._blocks.append(Block(x, y, BLC_W, BLC_H, color))
           
    def add_block(self, block):
        #FIXME
        # if (len(self._blocks) == 0
        #         or block.color == self._blocks[-1].color):
        x, y, w, h = self.bounds
        x += 2
        y += h-2
        if len(self._blocks):
            x, y, *_ = self._blocks[-1].bounds
        y -= BLC_H
        block.bounds = pygame.Rect(x, y, block.width, block.height)
        self._blocks.append(block)
        self._check_fulled()

    def _check_fulled(self):
        if len(self._blocks) != self.blocks_numb:
            self.is_fulled = False
            return
        for i in range(1, self.blocks_numb):
            if self._blocks[i-1].color != self._blocks[i].color:
                self.is_fulled = False
                return
        self.is_fulled = True


    def pop_block(self):
        if self._blocks: #FIXME ? bool(self._blocks) = False for empty deque
            return self._blocks.pop()
    
    def get_block(self):
        if self._blocks:
            return self._blocks[-1]

    def get_free_space(self):
        return self.blocks_numb - len(self._blocks)

    def is_empty(self):
        return len(self._blocks) == 0

    def move_up(self):
        self.move(0, -BLC_H)
        for block in self._blocks:
            block.move(0, -BLC_H)

    def move_down(self):
        self.move(0, BLC_H)
        for block in self._blocks:
            block.move(0, BLC_H)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds, 2, 2)
        for b in self._blocks:
            b.draw(surface)