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
        row = piece.row
        col = piece.col

        if piece.color == GREEN:
            moves.update(self._travel_left_up(piece.row, piece.col)) # X-1 Y-1
            moves.update(self._travel_left_down(piece.row, piece.col)) # X+1 Y-1
            moves.update(self._travel_right_up(piece.row, piece.col)) # X-1 Y+1
            moves.update(self._travel_right_down(piece.row, piece.col)) # X+1 Y+1
            moves.update(self._travel_up(piece.row, piece.col)) # X+1 Y
            moves.update(self._travel_down(piece.row, piece.col)) # X-1 Y
            moves.update(self._travel_right(piece.row, piece.col)) # X Y+1
            moves.update(self._travel_left(piece.row, piece.col)) # X Y-1
        if piece.color == RED:
            moves.update(self._travel_left_up(piece.row, piece.col)) # X-1 Y-1
            moves.update(self._travel_left_down(piece.row, piece.col)) # X+1 Y-1
            moves.update(self._travel_right_up(piece.row, piece.col)) # X-1 Y+1
            moves.update(self._travel_right_down(piece.row, piece.col)) # X+1 Y+1
            moves.update(self._travel_up(piece.row, piece.col)) # X+1 Y
            moves.update(self._travel_down(piece.row, piece.col)) # X-1 Y
            moves.update(self._travel_right(piece.row, piece.col)) # X Y+1
            moves.update(self._travel_left(piece.row, piece.col)) # X Y-1
        
        return moves

    def _travel_up(self, row, col):
        moves = {}

        current_row_checking = row -1
        if(current_row_checking >= 0 and current_row_checking <= 15):
            current_spot_checking = self.board[current_row_checking][col]
            if(current_spot_checking == 0):
                moves[(current_row_checking,col)] = current_row_checking + col
            else:
                moves.update(self._travel_up(current_row_checking, col)) # X+1 Y

        return moves

    def _travel_down(self, row, col):
        moves = {}

        current_row_checking = row +1

        if(current_row_checking >= 0 and current_row_checking <= 15):
            current_spot_checking = self.board[current_row_checking][col]
            if(current_spot_checking == 0):
                moves[(current_row_checking,col)] = current_row_checking + col
            else:
                moves.update(self._travel_down(current_row_checking, col)) # X-1 Y

        return moves

    def _travel_left(self, row, col):
        moves = {}

        current_col_checking = col -1

        if(current_col_checking >= 0 and current_col_checking <= 15):
            current_spot_checking = self.board[row][current_col_checking]
            if(current_spot_checking == 0):
                moves[(row,current_col_checking)] = row + current_col_checking
            else:
                moves.update(self._travel_left(row, current_col_checking)) # X Y-1

        return moves
    
    def _travel_right(self, row, col):
        moves = {}

        current_col_checking = col +1

        if(current_col_checking >= 0 and current_col_checking <= 15):
            current_spot_checking = self.board[row][current_col_checking]
            if(current_spot_checking == 0):
                moves[(row,current_col_checking)] = row + current_col_checking
            else:
                moves.update(self._travel_right(row, current_col_checking)) # X Y+1

        return moves
    
    def _travel_right_up(self, row, col):
        moves = {}

        current_col_checking = col +1
        current_row_checking = row -1

        if(current_col_checking >= 0 and current_row_checking >= 0 and current_col_checking <= 15 and current_row_checking <= 15):
            current_spot_checking = self.board[current_row_checking][current_col_checking]
            if(current_spot_checking == 0):
                moves[(current_row_checking,current_col_checking)] = current_row_checking + current_col_checking
            else:
                moves.update(self._travel_right_up(current_row_checking, current_col_checking)) # X-1 Y+1

        return moves
    
    def _travel_left_up(self, row, col):
        moves = {}

        current_col_checking = col -1
        current_row_checking = row -1

        if(current_col_checking >= 0 and current_row_checking >= 0 and current_col_checking <= 15 and current_row_checking <= 15):
            current_spot_checking = self.board[current_row_checking][current_col_checking]
            if(current_spot_checking == 0):
                moves[(current_row_checking,current_col_checking)] = current_row_checking + current_col_checking
            else:
                moves.update(self._travel_left_up(current_row_checking, current_col_checking)) # X-1 Y-1

        return moves
    
    def _travel_left_down(self, row, col):
        moves = {}

        current_col_checking = col -1
        current_row_checking = row +1

        if(current_col_checking >= 0 and current_row_checking >= 0 and current_col_checking <= 15 and current_row_checking <= 15):
            current_spot_checking = self.board[current_row_checking][current_col_checking]
            if(current_spot_checking == 0):
                moves[(current_row_checking,current_col_checking)] = current_row_checking + current_col_checking
            else:
                moves.update(self._travel_left_down(current_row_checking, current_col_checking)) # X+1 Y-1

        return moves
    
    def _travel_right_down(self, row, col):
        moves = {}

        current_col_checking = col +1
        current_row_checking = row +1

        if(current_col_checking >= 0 and current_row_checking >= 0 and current_col_checking <= 15 and current_row_checking <= 15):
            current_spot_checking = self.board[current_row_checking][current_col_checking]
            if(current_spot_checking == 0):
                moves[(current_row_checking,current_col_checking)] = current_row_checking + current_col_checking
            else:
                moves.update(self._travel_right_down(current_row_checking, current_col_checking)) # X+1 Y+1

        return moves