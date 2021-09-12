import os
import sys
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '/../')

from lvl import Level
from constants import *

if __name__ == "__main__":
    
    liquids = [
        (BLUE, BLUE, DARK_GREEN, DARK_BLUE),
        (GREY, GREEN, PINK, PURPLE),
        (BROWN, RED, PURPLE, ORANGE),
        (ORANGE, RED, PINK, ORANGE),
        (DARK_BLUE, YELLOW, RED, DARK_GREEN),
        (DARK_GREEN, BROWN, DARK_GREEN, YELLOW),
        (TURQUOISE, RED, PURPLE, BROWN),

        (TURQUOISE, PINK, PURPLE, TURQUOISE),
        (DARK_BLUE, BLUE, GREY, GREEN),
        (GREEN, GREY, YELLOW, BROWN),
        (DARK_BLUE, TURQUOISE, YELLOW, GREY),
        (ORANGE, PINK, BLUE, GREEN)]

    lvl105 = Level("Watersort", 800, 600, 30, 105, 14, liquids)
    lvl105.run()