import abc
from typing import Tuple
from domain.common import Color
# from domain.board import Board
from domain.figures import Figure


class Rook(Figure):

    LITERAL = 'r'

    # Ладья
    def __init__(self, color: Color):
        super().__init__(color)

    def __repr__(self):
        return self._colorise(Rook.LITERAL)

    def moved(self, start, end, board):
        pass

    def can_move(self, start, end, board):
        if start[0] == end[0]:
            if start[1] > end[1]:
                for i in range(end[1] + 1, start[1]):
                    if board.get((start[0], i)) != None:
                        return False
            elif start[1] < end[1]:
                for i in range(start[1], end[1] - 1):
                    if board.get((start[0], i)) != None:
                        return False
            return True
        elif start[1] == end[1]:
            if start[0] > end[0]:
                for i in range(end[0] + 1, start[0]):
                    if board.get((start[1], i)) != None:
                        return False
            elif start[0] < end[0]:
                for i in range(start[0], end[0] - 1):
                    if board.get((start[1], i)) != None:
                        return False
            return True
        return False
