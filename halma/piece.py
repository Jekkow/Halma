import pygame
from .constants import *

class Piece:
    PADDING = 6
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
      
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = SQAURE_SIZE * self.col + SQAURE_SIZE // 2
        self.y = SQAURE_SIZE * self.row + SQAURE_SIZE // 2
    
    def draw(self, win):
        radius = SQAURE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GRAY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    # Representation of object
    def __repr__(self):
        return str(self.color)
