import abc
from typing import Tuple
from domain.common import Color
# from domain.board import Board
from domain.figures import Figure


class Queen(Figure):

    LITERAL = 'q'

    def __init__(self, color: Color):
        super().__init__(color)

    def __repr__(self):
        return self._colorise(Queen.LITERAL)

    def moved(self, start, end, board):
        pass

    def can_move(self, start, end, board):
        pass
