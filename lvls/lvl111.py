import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/../')

from lvl import Level
from constants import *

if __name__ == "__main__":
    
    liquids = [
        (YELLOW, DARK_GREEN, ORANGE, DARK_BLUE),
        (TURQUOISE, GREEN, PINK, DARK_GREEN),
        (YELLOW, PURPLE, BLUE, RED),
        (DARK_GREEN, BLUE, ORANGE, PURPLE),
        (TURQUOISE, GREY, PINK, DARK_BLUE),
        (DARK_GREEN, YELLOW, BROWN, TURQUOISE),
        (BROWN, BLUE, PINK, RED),

        (ORANGE, DARK_BLUE, TURQUOISE, GREY),
        (YELLOW, GREY, GREEN, GREEN),
        (BLUE, GREEN, PINK, BROWN),
        (BROWN, PURPLE, RED, GREY),
        (RED, DARK_BLUE, PURPLE, ORANGE)]

    lvl111 = Level(111, len(liquids)+2, liquids)
    lvl111.run()