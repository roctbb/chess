import abc
from typing import Tuple
from domain.common import Color
# from domain.board import Board
from domain.figures import Figure


class Knight(Figure):
    # Конь

    LITERAL = 'n'

    def __init__(self, color: Color):
        super().__init__(color)

    def __repr__(self):
        return self._colorise(Knight.LITERAL)  # В шахматной нотации Конь это не "Horse", а N, от kNight

    def moved(self, start, end, board):
        pass

    def can_move(self, start, end, board):
        pass
