from bottle import Bottle
from game import Game
import pygame
from math import ceil
import os

from constants import *

class Level(Game):
    def __init__(self, 
                #  caption, 
                #  width, 
                #  height, 
                #  frame_rate,
                number, 
                bottles_number,
                liquids):
                
        Game.__init__(self, CAPTION, WIDTH, HEIGHT, FRAME_RATE)
        self.number = number
        self.bottles_number = bottles_number
        self.bottles = []
        self.clicked_bottle_idx = None        
        
        x, y = 80, 80
        for n in range(self.bottles_number):
            self.bottles.append(Bottle(x, y, BTL_COLOR))
            x += BLC_W*2
            if n == ceil(self.bottles_number / 2) - 1:
                x = 80
                y += self.bottles[-1].height+2*BLC_H

        self._liquids = liquids
        self._fill_bottles(liquids)

        self.moves_stack = []

        self.mouse_handlers.append(self.handle_mouse_event)
        self.keyup_handlers[pygame.K_LEFT].append(self.handle_key_event)
        # self.keyup_handlers[pygame.K_RIGHT].append(self.handle_key_event)
        self.keyup_handlers[pygame.K_SPACE].append(self.handle_key_event)
        


    def _fill_bottles(self, liquids: list) -> None:
        assert(len(liquids) < self.bottles_number)
        i = 0
        for l in liquids:
            self.bottles[i].add_liquid(l)
            i += 1
        for b in range(i, self.bottles_number):
            while not self.bottles[b].is_empty():
                self.bottles[b].pop_block()
        
    
    def draw(self):
        super().draw()
        for b in self.bottles:
            b.draw(self.surface)

    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos) #FIXME redundant

    def handle_key_event(self, key):
        if key == pygame.K_LEFT:
            self.roll_back()            
        # elif key == pygame.K_RIGHT:
        elif key == pygame.K_SPACE:
            self.restart()

    def roll_back(self):
        ids, blc_n = self.moves_stack.pop()
        id_from, id_to = ids
        bottle_from, bottle_to = self.bottles[id_from], self.bottles[id_to]
        for _ in range(blc_n):
            bottle_from.add_block(bottle_to.pop_block())

    def restart(self):
        if self.clicked_bottle_idx is not None:
            clicked_bottle = self.bottles[self.clicked_bottle_idx]
            clicked_bottle.move_down()
            self.clicked_bottle_idx = None
        self._fill_bottles(self._liquids)
        self.moves_stack = []

    def handle_mouse_up(self, pos):
        if (self.clicked_bottle_idx is not None 
                and self.bottles[self.clicked_bottle_idx].bounds.collidepoint(pos)):
            clicked_bottle = self.bottles[self.clicked_bottle_idx]
            clicked_bottle.move_down()
            self.clicked_bottle_idx = None
            return

        bottle, bottle_idx = None, None
        for i, btl in enumerate(self.bottles):
            if btl.bounds.collidepoint(pos):
                bottle = btl
                bottle_idx = i
                break
        if not bottle:
            return

        if self.clicked_bottle_idx is not None:
            clicked_bottle = self.bottles[self.clicked_bottle_idx]
            blocks_numb = self.transfer_liquid(self.clicked_bottle_idx, bottle_idx)
            if blocks_numb:
                self.moves_stack.append(((self.clicked_bottle_idx, bottle_idx), blocks_numb))
                self.check_win()
            clicked_bottle.move_down()
            self.clicked_bottle_idx = None
        else:
            self.clicked_bottle_idx = bottle_idx
            bottle.move_up()
    
    def transfer_liquid(self, from_bottle_idx: int, to_bottle_idx: int) -> int:
        from_bottle, to_bottle = self.bottles[from_bottle_idx], self.bottles[to_bottle_idx]
        free_space = to_bottle.get_free_space()
        blocks_numb = 0
        if free_space == 0:
            return
        for n in range(free_space):
            if from_bottle.is_empty():
                break
            if to_bottle.is_empty() or from_bottle.get_block().color == to_bottle.get_block().color:
                to_bottle.add_block(from_bottle.pop_block())
                blocks_numb += 1
            else:
                break
        return blocks_numb

    def check_win(self):
        for bottle in self.bottles:
            if not bottle.is_fulled:
                if bottle.is_empty(): 
                    continue
                return
        self.write_moves()
        self.game_over = True

    def write_moves(self):
        moves_dir = './moves/'
        if not os.path.exists(moves_dir):
            os.mkdir(moves_dir)
        with open(moves_dir+str(self.number)+'.txt', 'w+')as f:
            for bottles, bn in self.moves_stack:
                f.write(str(bottles[0]+1)+' ' + str(bottles[1]+1)+' ' + str(bn)+'\n')
                
