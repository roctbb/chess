import abc
from typing import Tuple
from domain.common import Color
# from domain.board import Board
from domain.figures import Figure


class Pawn(Figure):

    LITERAL = 'p'

    def __init__(self, color: Color):
        super().__init__(color)
        self.__is_moved = False

    def can_move(self, start, end, board):
        direction = self._direction(board)

        # прямой ход
        if start[0] == end[0]:
            if end[1] == start[1] + direction and board.get(end) is None:
                return True
            if end[1] == start[1] + 2 * direction and board.get(end) is None and board.get(
                    (start[0], start[1] + direction)) is None and not self.__is_moved:
                return True
        # косой ход
        if abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 1:
            if board.get(end) is not None and board.get(end).color != self.color:
                return True

        return False

    def moved(self, start, end, board):
        self.__is_moved = True

    def __repr__(self):
        return self._colorise(Pawn.LITERAL)  # Пешка, вообще говоря, не записывается в нотации)
