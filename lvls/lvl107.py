import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/../')

from lvl import Level
from constants import *

if __name__ == "__main__":
    
    liquids = [
        (YELLOW, ORANGE, GREY, TURQUOISE),
        (BLUE, GREEN, PURPLE, RED),
        (PURPLE, TURQUOISE, PINK, GREEN),
        (BROWN, RED, PINK, YELLOW),
        (PURPLE, BROWN, DARK_BLUE, GREEN),
        (YELLOW, PURPLE, GREY, GREEN),
        (DARK_GREEN, BLUE, GREY, ORANGE),

        (PINK, BLUE, DARK_GREEN, RED),
        (TURQUOISE, BLUE, DARK_BLUE, DARK_BLUE),
        (ORANGE, PINK, BROWN, DARK_GREEN),
        (ORANGE, YELLOW, TURQUOISE, GREY),
        (DARK_BLUE, DARK_GREEN, BROWN, RED)]

    lvl107 = Level("Watersort", 800, 600, 30, 107, 14, liquids)
    lvl107.run()