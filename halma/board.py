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
            self.board[x][y] = Piece(x, y, RED, 2)
        for position in location_Player:
            x = position[0]
            y = position[1]
            self.board[x][y] = Piece(x, y, GREEN, 1)
    
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
            moves = {}
            moves.update(self._travel_left_up(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X-1 Y-1
            moves.update(self._travel_left_down(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X+1 Y-1
            moves.update(self._travel_right_up(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X-1 Y+1
            moves.update(self._travel_right_down(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X+1 Y+1
            moves.update(self._travel_up(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X+1 Y
            moves.update(self._travel_down(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X-1 Y
            moves.update(self._travel_right(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X Y+1
            moves.update(self._travel_left(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X Y-1
        if piece.color == RED:
            moves = {}
            moves.update(self._travel_left_up(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X-1 Y-1
            moves.update(self._travel_left_down(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X+1 Y-1
            moves.update(self._travel_right_up(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X-1 Y+1
            moves.update(self._travel_right_down(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X+1 Y+1
            moves.update(self._travel_up(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X+1 Y
            moves.update(self._travel_down(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X-1 Y
            moves.update(self._travel_right(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X Y+1
            moves.update(self._travel_left(moves, piece.row, piece.col, previous_positions=[], jumped = False, ignore_empty= False)) # X Y-1
        return moves

    def _travel_up(self, moves, row, col, previous_positions, jumped, ignore_empty):
        current_row_checking = row -1
        if(current_row_checking >= 0 and current_row_checking <= 15):
            if(len(previous_positions) == 0): # First time, list is empty
                current_spot_checking = self.board[current_row_checking][col]
                if(current_spot_checking == 0 and not ignore_empty):
                    moves[(current_row_checking,col)] = row, col
                    if(jumped):
                        previous_positions.append([current_row_checking,col])
                        jumped = False
                        ignore_empty = True
                        moves.update(self._travel_left_up(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                        moves.update(self._travel_left_down(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                        moves.update(self._travel_right_up(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                        moves.update(self._travel_right_down(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                        moves.update(self._travel_up(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X+1 Y
                        moves.update(self._travel_right(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X Y+1
                        moves.update(self._travel_left(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X Y-1
                elif(current_spot_checking != 0):
                    jumped = True
                    ignore_empty = False
                    moves.update(self._travel_up(moves, current_row_checking, col, previous_positions, jumped, ignore_empty))


            if [current_row_checking,col] not in previous_positions: # Execute when positions are in list
                    current_spot_checking = self.board[current_row_checking][col]
                    if(current_spot_checking == 0 and not ignore_empty):
                        moves[(current_row_checking,col)] = row, col
                        if(jumped):
                            previous_positions.append([current_row_checking,col])
                            jumped = False
                            ignore_empty = True
                            moves.update(self._travel_left_up(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                            moves.update(self._travel_left_down(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                            moves.update(self._travel_right_up(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                            moves.update(self._travel_right_down(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                            moves.update(self._travel_up(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X+1 Y
                            moves.update(self._travel_right(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X Y+1
                            moves.update(self._travel_left(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X Y-1
                    elif(current_spot_checking != 0):
                        jumped = True
                        ignore_empty = False
                        moves.update(self._travel_up(moves, current_row_checking, col, previous_positions, jumped, ignore_empty))

        return moves

    def _travel_down(self, moves, row, col, previous_positions, jumped, ignore_empty):
        current_row_checking = row +1

        if(current_row_checking >= 0 and current_row_checking <= 15):
            if(len(previous_positions) == 0): # First time, list is empty
                current_spot_checking = self.board[current_row_checking][col]
                if(current_spot_checking == 0 and not ignore_empty):
                    moves[(current_row_checking,col)] = row, col
                    if(jumped):
                        previous_positions.append([current_row_checking,col])
                        jumped = False
                        ignore_empty = True
                        moves.update(self._travel_left_up(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                        moves.update(self._travel_left_down(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                        moves.update(self._travel_right_up(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                        moves.update(self._travel_right_down(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                        moves.update(self._travel_down(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X-1 Y
                        moves.update(self._travel_right(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X Y+1
                        moves.update(self._travel_left(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X Y-1
                elif(current_spot_checking != 0):
                    jumped = True
                    ignore_empty = False
                    moves.update(self._travel_down(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X+1 Y


            if [current_row_checking,col] not in previous_positions: # Execute when positions are in list
                    current_spot_checking = self.board[current_row_checking][col]
                    if(current_spot_checking == 0 and not ignore_empty):
                        moves[(current_row_checking,col)] = row, col
                        if(jumped):
                            previous_positions.append([current_row_checking,col])
                            jumped = False
                            ignore_empty = True
                            moves.update(self._travel_left_up(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                            moves.update(self._travel_left_down(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                            moves.update(self._travel_right_up(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                            moves.update(self._travel_right_down(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                            moves.update(self._travel_down(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X-1 Y
                            moves.update(self._travel_right(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X Y+1
                            moves.update(self._travel_left(moves, current_row_checking, col, previous_positions, jumped, ignore_empty)) # X Y-1
                    elif(current_spot_checking != 0):
                        jumped = True
                        ignore_empty = False
                        moves.update(self._travel_down(moves, current_row_checking, col, previous_positions, jumped, ignore_empty))

        return moves

    def _travel_left(self, moves, row, col, previous_positions, jumped, ignore_empty):
        current_col_checking = col -1

        if(current_col_checking >= 0 and current_col_checking <= 15):
            if(len(previous_positions) == 0): # First time, list is empty
                current_spot_checking = self.board[row][current_col_checking]
                if(current_spot_checking == 0 and not ignore_empty):
                    moves[(row,current_col_checking)] = row, col
                    if(jumped):
                        previous_positions.append([row,current_col_checking])
                        jumped = False
                        ignore_empty = True
                        moves.update(self._travel_left_up(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                        moves.update(self._travel_left_down(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                        moves.update(self._travel_right_up(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                        moves.update(self._travel_right_down(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                        moves.update(self._travel_up(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y
                        moves.update(self._travel_down(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y
                        #moves.update(self._travel_right(row, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y+1
                        moves.update(self._travel_left(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y-1
                elif(current_spot_checking != 0):
                    jumped = True
                    ignore_empty = False
                    moves.update(self._travel_left(moves, row, current_col_checking, previous_positions, jumped, ignore_empty))


            if [row,current_col_checking] not in previous_positions: # Execute when positions are in list
                    current_spot_checking = self.board[row][current_col_checking]
                    if(current_spot_checking == 0 and not ignore_empty):
                        moves[(row,current_col_checking)] = row, col
                        if(jumped):
                            previous_positions.append([row,current_col_checking])
                            jumped = False
                            ignore_empty = True
                            moves.update(self._travel_left_up(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                            moves.update(self._travel_left_down(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                            moves.update(self._travel_right_up(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                            moves.update(self._travel_right_down(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                            moves.update(self._travel_up(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y
                            moves.update(self._travel_down(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y
                            #moves.update(self._travel_right(row, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y+1
                            moves.update(self._travel_left(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y-1
                    elif(current_spot_checking != 0):
                        jumped = True
                        ignore_empty = False
                        moves.update(self._travel_left(moves, row, current_col_checking, previous_positions, jumped, ignore_empty))

        return moves
    
    def _travel_right(self, moves, row, col, previous_positions, jumped, ignore_empty):

        current_col_checking = col +1

        if(current_col_checking >= 0 and current_col_checking <= 15):
            if(len(previous_positions) == 0): # First time, list is empty
                current_spot_checking = self.board[row][current_col_checking]
                if(current_spot_checking == 0 and not ignore_empty):
                    moves[(row,current_col_checking)] = row, col
                    if(jumped):
                        previous_positions.append([row,current_col_checking])
                        jumped = False
                        ignore_empty = True
                        moves.update(self._travel_left_up(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                        moves.update(self._travel_left_down(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                        moves.update(self._travel_right_up(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                        moves.update(self._travel_right_down(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                        moves.update(self._travel_up(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y
                        moves.update(self._travel_down(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y
                        moves.update(self._travel_right(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y+1
                        #moves.update(self._travel_left(row, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y-1
                elif(current_spot_checking != 0):
                    jumped = True
                    ignore_empty = False
                    moves.update(self._travel_right(moves, row, current_col_checking, previous_positions, jumped, ignore_empty))


            if [row,current_col_checking] not in previous_positions: # Execute when positions are in list
                    current_spot_checking = self.board[row][current_col_checking]
                    if(current_spot_checking == 0 and not ignore_empty):
                        moves[(row,current_col_checking)] = row, col
                        if(jumped):
                            previous_positions.append([row,current_col_checking])
                            jumped = False
                            ignore_empty = True
                            moves.update(self._travel_left_up(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                            moves.update(self._travel_left_down(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                            moves.update(self._travel_right_up(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                            moves.update(self._travel_right_down(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                            moves.update(self._travel_up(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y
                            moves.update(self._travel_down(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y
                            moves.update(self._travel_right(moves, row, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y+1
                            #moves.update(self._travel_left(row, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y-1
                    elif(current_spot_checking != 0):
                        jumped = True
                        ignore_empty = False
                        moves.update(self._travel_right(moves, row, current_col_checking, previous_positions, jumped, ignore_empty))

        return moves
    
    def _travel_right_up(self, moves, row, col, previous_positions, jumped, ignore_empty):
        current_col_checking = col +1
        current_row_checking = row -1

        if(current_row_checking >= 0 and current_row_checking <= 15 and current_col_checking >= 0 and current_col_checking <= 15):
            if(len(previous_positions) == 0): # First time, list is empty
                current_spot_checking = self.board[current_row_checking][current_col_checking]
                if(current_spot_checking == 0 and not ignore_empty):
                    moves[(current_row_checking,current_col_checking)] = row, col
                    if(jumped):
                        previous_positions.append([current_row_checking,current_col_checking])
                        jumped = False
                        ignore_empty = True
                        moves.update(self._travel_left_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                        #moves.update(self._travel_left_down(current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                        moves.update(self._travel_right_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                        moves.update(self._travel_right_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                        moves.update(self._travel_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y
                        moves.update(self._travel_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y
                        moves.update(self._travel_right(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y+1
                        moves.update(self._travel_left(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y-1
                elif(current_spot_checking != 0):
                    jumped = True
                    ignore_empty = False
                    moves.update(self._travel_right_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y


            if[current_row_checking,current_col_checking] not in previous_positions: # Execute when positions are in list
                    current_spot_checking = self.board[current_row_checking][current_col_checking]
                    if(current_spot_checking == 0 and not ignore_empty):
                        moves[(current_row_checking,current_col_checking)] = row, col
                        if(jumped):
                            previous_positions.append([current_row_checking,current_col_checking])
                            jumped = False
                            ignore_empty = True
                            moves.update(self._travel_left_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                            #moves.update(self._travel_left_down(current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                            moves.update(self._travel_right_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                            moves.update(self._travel_right_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                            moves.update(self._travel_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y
                            moves.update(self._travel_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y
                            moves.update(self._travel_right(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y+1
                            moves.update(self._travel_left(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y-1
                    elif(current_spot_checking != 0):
                        jumped = True
                        ignore_empty = False
                        moves.update(self._travel_right_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y

        return moves
    
    def _travel_left_up(self, moves, row, col, previous_positions, jumped, ignore_empty):

        current_col_checking = col -1
        current_row_checking = row -1

        if(current_row_checking >= 0 and current_row_checking <= 15 and current_col_checking >= 0 and current_col_checking <= 15):
            if(len(previous_positions) == 0): # First time, list is empty
                current_spot_checking = self.board[current_row_checking][current_col_checking]
                if(current_spot_checking == 0 and not ignore_empty):
                    moves[(current_row_checking,current_col_checking)] = row, col
                    if(jumped):
                        previous_positions.append([current_row_checking,current_col_checking])
                        jumped = False
                        ignore_empty = True
                        moves.update(self._travel_left_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                        moves.update(self._travel_left_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                        moves.update(self._travel_right_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                        #moves.update(self._travel_right_down(current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                        moves.update(self._travel_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y
                        moves.update(self._travel_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y
                        moves.update(self._travel_right(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y+1
                        moves.update(self._travel_left(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y-1
                elif(current_spot_checking != 0):
                    jumped = True
                    ignore_empty = False
                    moves.update(self._travel_left_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y


            if[current_row_checking,current_col_checking] not in previous_positions: # Execute when positions are in list
                    current_spot_checking = self.board[current_row_checking][current_col_checking]
                    if(current_spot_checking == 0 and not ignore_empty):
                        moves[(current_row_checking,current_col_checking)] = row, col
                        if(jumped):
                            previous_positions.append([current_row_checking,current_col_checking])
                            jumped = False
                            ignore_empty = True
                            moves.update(self._travel_left_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                            moves.update(self._travel_left_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                            moves.update(self._travel_right_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                            #moves.update(self._travel_right_down(current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                            moves.update(self._travel_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y
                            moves.update(self._travel_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y
                            moves.update(self._travel_right(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y+1
                            moves.update(self._travel_left(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y-1
                    elif(current_spot_checking != 0):
                        jumped = True
                        ignore_empty = False
                        moves.update(self._travel_left_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y

        return moves
    
    def _travel_left_down(self, moves, row, col, previous_positions, jumped, ignore_empty):

        current_col_checking = col -1
        current_row_checking = row +1

        if(current_row_checking >= 0 and current_row_checking <= 15 and current_col_checking >= 0 and current_col_checking <= 15):
            if(len(previous_positions) == 0): # First time, list is empty
                current_spot_checking = self.board[current_row_checking][current_col_checking]
                if(current_spot_checking == 0 and not ignore_empty):
                    moves[(current_row_checking,current_col_checking)] = row, col
                    if(jumped):
                        previous_positions.append([current_row_checking,current_col_checking])
                        jumped = False
                        ignore_empty = True
                        moves.update(self._travel_left_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                        moves.update(self._travel_left_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                        #moves.update(self._travel_right_up(current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                        moves.update(self._travel_right_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                        moves.update(self._travel_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y
                        moves.update(self._travel_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y
                        moves.update(self._travel_right(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y+1
                        moves.update(self._travel_left(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y-1
                elif(current_spot_checking != 0):
                    jumped = True
                    ignore_empty = False
                    moves.update(self._travel_left_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y


            if[current_row_checking,current_col_checking] not in previous_positions: # Execute when positions are in list
                    current_spot_checking = self.board[current_row_checking][current_col_checking]
                    if(current_spot_checking == 0 and not ignore_empty):
                        moves[(current_row_checking,current_col_checking)] = row, col
                        if(jumped):
                            previous_positions.append([current_row_checking,current_col_checking])
                            jumped = False
                            ignore_empty = True
                            moves.update(self._travel_left_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                            moves.update(self._travel_left_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                            #moves.update(self._travel_right_up(current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                            moves.update(self._travel_right_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                            moves.update(self._travel_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y
                            moves.update(self._travel_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y
                            moves.update(self._travel_right(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y+1
                            moves.update(self._travel_left(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y-1
                    elif(current_spot_checking != 0):
                        jumped = True
                        ignore_empty = False
                        moves.update(self._travel_left_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y

        return moves
    
    def _travel_right_down(self, moves, row, col, previous_positions, jumped, ignore_empty):

        current_col_checking = col +1
        current_row_checking = row +1

        if(current_row_checking >= 0 and current_row_checking <= 15 and current_col_checking >= 0 and current_col_checking <= 15):
            if(len(previous_positions) == 0): # First time, list is empty
                current_spot_checking = self.board[current_row_checking][current_col_checking]
                if(current_spot_checking == 0 and not ignore_empty):
                    moves[(current_row_checking,current_col_checking)] = row, col
                    if(jumped):
                        previous_positions.append([current_row_checking,current_col_checking])
                        jumped = False
                        ignore_empty = True
                        #moves.update(self._travel_left_up(current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                        moves.update(self._travel_left_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                        moves.update(self._travel_right_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                        moves.update(self._travel_right_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                        moves.update(self._travel_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y
                        moves.update(self._travel_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y
                        moves.update(self._travel_right(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y+1
                        moves.update(self._travel_left(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y-1
                elif(current_spot_checking != 0):
                    jumped = True
                    ignore_empty = False
                    moves.update(self._travel_right_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y


            if[current_row_checking,current_col_checking] not in previous_positions: # Execute when positions are in list
                    current_spot_checking = self.board[current_row_checking][current_col_checking]
                    if(current_spot_checking == 0 and not ignore_empty):
                        moves[(current_row_checking,current_col_checking)] = row, col
                        if(jumped):
                            previous_positions.append([current_row_checking,current_col_checking])
                            jumped = False
                            ignore_empty = True
                            #moves.update(self._travel_left_up(current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y-1
                            moves.update(self._travel_left_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y-1
                            moves.update(self._travel_right_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y+1
                            moves.update(self._travel_right_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y+1
                            moves.update(self._travel_up(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y
                            moves.update(self._travel_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X-1 Y
                            moves.update(self._travel_right(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y+1
                            moves.update(self._travel_left(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X Y-1
                    elif(current_spot_checking != 0):
                        jumped = True
                        ignore_empty = False
                        moves.update(self._travel_right_down(moves, current_row_checking, current_col_checking, previous_positions, jumped, ignore_empty)) # X+1 Y

        return moves