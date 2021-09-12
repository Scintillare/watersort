import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/../')

from lvl import Level
from constants import *

if __name__ == "__main__":
    
    liquids = [
        (GREY, BROWN, ORANGE, BLUE),
        (PURPLE, TURQUOISE, YELLOW, GREY),
        (BLUE, PINK, GREEN, ORANGE),
        (YELLOW, RED, YELLOW, DARK_BLUE),
        (YELLOW, ORANGE, PURPLE, BROWN),
        (DARK_GREEN, GREEN, TURQUOISE, DARK_GREEN),
        (DARK_BLUE, RED, DARK_BLUE, GREEN),

        (RED, BROWN,  TURQUOISE, BROWN),
        (PURPLE, BLUE, TURQUOISE, PINK),
        (PINK, ORANGE, GREEN, PURPLE),
        (DARK_GREEN, DARK_GREEN, PINK, GREY),
        (DARK_BLUE, BLUE, RED, GREY)]

    lvl109 = Level("Watersort", 800, 600, 30, 109, len(liquids)+2, liquids)
    lvl109.run()