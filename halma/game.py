import pygame
from .constants import *
from .board import *


class Game():
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self): # Initialize the game
        self.selected = None
        self.board = Board()
        self.turn = GREEN # Player turn's first
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result: # There is a piece selected and you select another piece
                self.selected = None #Deselect slected piece
                self.select(row, col) #Select the new piece

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves: #if there is a piece selected and the spot where it goes to is EMPTY ()== 0) and the move is in valid_moves
            self.board.move(self.selected, row, col) #move the piece
            self.change_turn() #change turn to other player
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQAURE_SIZE + SQAURE_SIZE//2, row * SQAURE_SIZE + SQAURE_SIZE //2), 7)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == GREEN:
            self.turn = RED
        else: self.turn = GREEN
