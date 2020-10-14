import pygame
from .constants import *
from .piece import *


class Board():
    def __init__(self):
        self.board = [[]]
        self.create_board()

    def draw_grid(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (row*SQAURE_SIZE, col*SQAURE_SIZE, SQAURE_SIZE, SQAURE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]   

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLUMNS):
                self.board[row].append(0)
        
            # Create Pieces
        for position in location_AI:
            x = position[0]
            y = position[1]
            self.board[x][y] = Piece(x, y, RED)
        for position in location_Player:
            x = position[0]
            y = position[1]
            self.board[x][y] = Piece(x, y, GREEN)
    
    def draw(self, win):
        self.draw_grid(win)
        for row in range(ROWS):
            for col in range (COLUMNS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def winner(self):
        pass
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col -1
        right = piece.col +1
        up = piece.row -1
        down = piece.row +1
        row = piece.row
        col = piece.col

        if piece.color == GREEN:
            pass
            # X-1 Y-1
            # X+1 Y-1
            # X-1 Y+1
            # X+1 Y+1
            # X+1 Y
            # X-1 Y
            # X Y+1
            # X Y-1
        if piece.color == RED:
            pass
            # X-1 Y-1
            # X+1 Y-1
            # X-1 Y+1
            # X+1 Y+1
            # X+1 Y
            # X-1 Y
            # X Y+1
            # X Y-1
        
        return moves

    def _travel_up(self, color, direction):
        moves = {}
        
        return moves
