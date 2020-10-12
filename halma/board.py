import pygame
from .constants import *
from .piece import *


class Board():
    def __init__(self):
        self.board = [[]]
        self.red_pieces_left = self.green_pieces_left = 19
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

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == GREEN:
                    self.green_pieces_left -= 1
                else:
                    self.red_pieces_left -= 1

    def winner(self):
        if self.red_pieces_left <= 0:
            return GREEN
        elif self.green_pieces_left <= 0:
            return RED
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col -1
        right = piece.col + 1
        row = piece.row

        if piece.color == GREEN:
            moves.update(self._traverse_left(row-1, max(row-3, -1), -1, piece.color, left)) # X-1 Y-1
            moves.update(self._traverse_left_down(row+1, max(row+3, 1), 1, piece.color, left)) # X+1 Y-1
            moves.update(self._traverse_right(row-1, max(row-3, -1), -1, piece.color, right)) # X-1 Y+1
            moves.update(self._traverse_right(row+1, min(row+3, ROWS), 1, piece.color, right)) # X+1 Y+1
            # X+1 Y
            # X-1 Y
            # X Y+1
            # X Y-1
        if piece.color == RED:
            moves.update(self._traverse_left(row+1, min(row+3, ROWS), 1, piece.color, left)) # X+1 Y+1
            moves.update(self._traverse_right(row+1, min(row+3, ROWS), 1, piece.color, right)) # X+1 Y+1
            moves.update(self._traverse_right_up(row-1, min(row-3, ROWS), -1, piece.color, right)) # X-1 Y+1
            moves.update(self._traverse_left(row-1, max(row-3, -1), -1, piece.color, left)) # X-1 Y-1
            #moves.update(self._traverse_down(row+1, max(row+3, ROWS), +1, piece.color, left))
            # X+1 Y
            # X-1 Y
            # X Y+1
            # X Y-1
        
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color: 
                break
            else:
                last = [current]
            left -= 1
        return moves

    def _traverse_left_down(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color: 
                break
            else:
                last = [current]
            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLUMNS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color: 
                break
            else:
                last = [current]
            right += 1
        return moves

    def _traverse_right_up(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLUMNS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color: 
                break
            else:
                last = [current]
            right += 1
        return moves

    def _traverse_down(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, 2)] = last + skipped
                else:
                    moves[(r, 2)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
                    moves.update(self._traverse_down(r+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color: 
                break
            else:
                last = [current]
            left += 1
        return moves