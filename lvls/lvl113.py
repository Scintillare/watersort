import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/../')

from lvl import Level
from constants import *

if __name__ == "__main__":
    
    liquids = [
        (YELLOW, DARK_BLUE, ORANGE, YELLOW),
        (GREY, PINK, YELLOW, GREEN),
        (TURQUOISE, DARK_BLUE, PINK, DARK_BLUE),
        (DARK_GREEN, YELLOW, RED, GREY),
        (RED, PURPLE, GREY, GREEN),
        (TURQUOISE, BROWN, DARK_BLUE, ORANGE),
        (PURPLE, RED, BLUE, DARK_GREEN),

        (BROWN, PINK, BLUE, TURQUOISE),
        (BROWN, DARK_GREEN, PINK, GREEN),
        (DARK_GREEN, BLUE, PURPLE, BROWN),
        (GREEN, TURQUOISE, ORANGE, GREY),
        (RED, PURPLE, ORANGE, BLUE)]

    lvl111 = Level(113, len(liquids)+2, liquids)
    lvl111.run()