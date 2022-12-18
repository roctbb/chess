import abc
from typing import Tuple
from domain.common import Color
# from domain.board import Board


class Figure:

    LITERAL: str = None

    def __init__(self, color: Color):
        self.color = color

    @abc.abstractmethod
    def can_move(self, start, end, board):
        raise NotImplementedError

    def moved(self, start, end, board):
        pass

    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError

    def _colorise(self, s):
        if self.color == Color.WHITE:
            return s.upper()
        return s

    def _direction(self, board):
        if self.color == board.color:
            return -1
        else:
            return 1

    @classmethod
    def get_figure_by_literal(cls, figure_literal: str, color: Color):
        subs = cls.__subclasses__()
        print(subs)
