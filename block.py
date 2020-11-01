import pygame

from gameobject import GameObject


class Block(GameObject):
    def __init__(self, x, y, w, h, color):
        GameObject.__init__(self, x, y, w, h)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)