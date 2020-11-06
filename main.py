import pygame
from pygame.display import set_caption
from halma.constants import *
from halma.board import Board
from halma.game import Game

FPS = 60
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Halma")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQAURE_SIZE
    col = x // SQAURE_SIZE
    return row, col

def result(gameWinner):
    run = False
    resultDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    resultDisplay.fill(WHITE)
    if(gameWinner == GREEN):
        pygame.display.set_caption("You Won")
    elif(gameWinner == RED):
        pygame.display.set_caption("You Lost")
    elif(gameWinner == "remise"):
        pygame.display.set_caption("It's a tie")
    resultDisplay.blit(0,0)
    pygame.display.flip()
    pygame.display.update()

    end_menu_running = True

    while end_menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_menu_running = False

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW, 0)

    while run:

        clock.tick(FPS)
        
        if game.turn == RED:
            pass #AI turn
        
        gameWinner = game.winner()
        print(gameWinner)
        if gameWinner != None:
            result(gameWinner)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    pygame.quit() ## Open new window with Win or Loose

main()
