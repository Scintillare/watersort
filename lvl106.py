from lvl import Level
from constants import *

if __name__ == "__main__":
    
    liquids = [
        (PINK, TURQUOISE, RED, PURPLE),
        (DARK_BLUE, DARK_BLUE, GREEN, PINK),
        (GREY, BLUE, BLUE, DARK_BLUE),
        (GREEN, TURQUOISE, GREEN, PINK),
        (ORANGE, ORANGE, PURPLE, GREY),
        (GREEN, ORANGE, RED, PINK),

        (GREY, GREY, TURQUOISE, RED),
        (TURQUOISE, RED, PURPLE, ORANGE),
        (BLUE, BLUE, DARK_BLUE, PURPLE)]

    lvl106 = Level("Watersort", 800, 600, 30, 106, 11, liquids)
    lvl106.run()