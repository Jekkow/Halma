import pygame
from halma.constants import *
from halma.board import Board
from halma.game import Game
import sys

FPS = 60
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Halma")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQAURE_SIZE
    col = x // SQAURE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)
    sys.setrecursionlimit(100000000)

    while run:

        clock.tick(FPS)
        
        if game.winner() != None:
            print(game.winner())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    pygame.quit()



main()
