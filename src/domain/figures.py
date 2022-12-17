import abc
from typing import Tuple
from domain.common import Side


class Figure:
    def __init__(self, side: Side):
        self.side = side

    @abc.abstractmethod
    def can_move(self, start, end, board):
        raise NotImplementedError

    def moved(self, start, end, board):
        pass

    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError

    def _colorise(self, s):
        if self.side == Side.WHITE:
            return s.upper()
        return s

    def _direction(self, board):
        if self.side == board.side:
            return -1
        else:
            return 1


class Pawn(Figure):
    def __init__(self, side: Side):
        super().__init__(side)
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
            if board.get(end) is not None and board.get(end).side != self.side:
                return True

        return False

    def moved(self, start, end, board):
        self.__is_moved = True

    def __repr__(self):
        return self._colorise("p")


class Rook(Figure):
    #ЛАДИЯ
    def __init__(self, side: Side):
        super().__init__(side)

    def __repr__(self):
        return self._colorise("r")

    def moved(self, start, end, board):
        pass

    def can_move(self, start, end, board):
        if start[0] == end[0]:
            if start[1] > end[1]:
                for i in range(end[1], start[1]):
                    if board.get([start[0], i]) != None: return False
            elif start[1] < end[1]:
                for i in range(start[1], end[1]):
                    if board.get([start[0], i]) != None: return False
        elif start[1] == end[1]:
            if start[0] > end[0]:
                for i in range(end[0], start[0]):
                    if board.get([start[1], i]) != None: return False
            elif start[0] < end[0]:
                for i in range(start[0], end[0]):
                    if board.get([start[1], i]) != None: return False
        return True

class Bishop(Figure):
    #Слон
    def __init__(self, side: Side):
        super().__init__(side)

    def __repr__(self):
        return self._colorise("b")

    def moved(self, start, end, board):
        pass

    def can_move(self, start, end, board):
        pass


class Knight(Figure):
    #Лошаодь
    def __init__(self, side: Side):
        super().__init__(side)

    def __repr__(self):
        return self._colorise("h")

    def moved(self, start, end, board):
        pass

    def can_move(self, start, end, board):
        pass


class Queen(Figure):
    def __init__(self, side: Side):
        super().__init__(side)

    def __repr__(self):
        return self._colorise("q")

    def moved(self, start, end, board):
        pass

    def can_move(self, start, end, board):
        pass


class King(Figure):
    def __init__(self, side: Side):
        super().__init__(side)

    def __repr__(self):
        return self._colorise("k")

    def moved(self, start, end, board):
        pass

    def can_move(self, start, end, board):
        pass
