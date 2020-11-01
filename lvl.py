from bottle import Bottle
from game import Game

from constants import *

class Level(Game):
    def __init__(self, 
                 caption, 
                 width, 
                 height, 
                 frame_rate,
                number, 
                bottles_number,
                liquids):
                
        Game.__init__(self, caption, width, height, frame_rate)
        self.number = number
        self.bottles_number = bottles_number
        self.bottles = []
        
        
        x, y = 150, 150
        for n in range(self.bottles_number):
            self.bottles.append(Bottle(x, y, BTL_COLOR))
            x += BLC_W*2
            if n == (self.bottles_number // 2)-1:
                x = 150
                y += BLC_H*5.5

        self._fill_bottles(liquids)

    def _fill_bottles(self, liquids: list) -> None:
        assert(len(liquids) < self.bottles_number)

        for i, l in enumerate(liquids):
            self.bottles[i].add_liquid(l)
    
    def draw(self):
        super().draw()
        for b in self.bottles:
            b.draw(self.surface)

if __name__ == "__main__":
    
    liquids = [
    (BLUE, BLUE, DARK_GREEN, DARK_BLUE),
    (GREY, GREEN, PINK, PURPLE),
    (BROWN, RED, PURPLE, ORANGE),
    (ORANGE, RED, PINK, ORANGE),
    (PURPLE, YELLOW, RED, DARK_GREEN),
    (DARK_GREEN, BROWN, DARK_GREEN, YELLOW),
    (TURQUOISE, RED, PURPLE, BROWN),

    (TURQUOISE, PINK, PURPLE, TURQUOISE),
    (DARK_BLUE, BLUE, GREY, GREEN),
    (GREEN, GREY, YELLOW, BROWN),
    (BLUE, TURQUOISE, YELLOW, GREY),
    (ORANGE, PINK, BLUE, GREEN)]

    lvl105 = Level("Watersort", 800, 600, 30, 105, 14, liquids)
    lvl105.run()