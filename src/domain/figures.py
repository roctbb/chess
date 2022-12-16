import abc
from typing import Tuple
from domain.common import Side


class Figure:
    def __init__(self, side: Side):
        self.side = side

    @abc.abstractmethod
    def move(self, start, end, board):
        raise NotImplementedError

    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError


class Pawn(Figure):
    def __init__(self, side: Side):
        super().__init__(side)
        self.__is_moved = False

    def __repr__(self):
        return "p"


class Rook(Figure):
    def __init__(self, side: Side):
        super().__init__(side)

    def __repr__(self):
        return "r"


class Bishop(Figure):
    def __init__(self, side: Side):
        super().__init__(side)

    def __repr__(self):
        return "b"


class Knight(Figure):
    def __init__(self, side: Side):
        super().__init__(side)

    def __repr__(self):
        return "k"


class Queen(Figure):
    def __init__(self, side: Side):
        super().__init__(side)

    def __repr__(self):
        return "q"


class King(Figure):
    def __init__(self, side: Side):
        super().__init__(side)

    def __repr__(self):
        return "K"
