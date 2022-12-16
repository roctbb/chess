from typing import Optional, Tuple
from domain.figures import *
from domain.common import Side


class Board:
    def __init__(self, side: Side = Side.WHITE, state=None):
        self._cells = {}
        self._size = (8, 8)
        self.eaten = {
            side: [],
            Side.opposite(side): []
        }

        self.side = side

        self.__place_row((0, 6), [Pawn] * 8, side)
        self.__place_row((0, 1), [Pawn] * 8, Side.opposite(side))

        if side == Side.WHITE:
            self.__place_row((0, 0), [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook], Side.opposite(side))
            self.__place_row((0, 7), [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook], side)
        else:
            self.__place_row((0, 0), [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook], Side.opposite(side))
            self.__place_row((0, 7), [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook], side)

    def __load_state(self, state: str):
        rows = state.split()

        if len(rows) != 8:
            raise Exception("Incorrect template")

        for row in rows:
            if len(row) != 8:
                raise Exception("Incorrect template")

        figure_classes = {
            "r": Rook,
            "h": Knight,
            "b": Bishop,
            "k": King,
            "q": Queen,
            "p": Pawn
        }

        for j in range(len(rows)):
            row = rows[j]
            for i in range(len(row)):
                f = row[i]
                if f == ' ':
                    continue
                if f.isupper():
                    self.__set((i, j), figure_classes[f.lower()](Side.WHITE))
                else:
                    self.__set((i, j), figure_classes[f.lower()](Side.BLACK))

    def __set(self, position, figure):
        i, j = position

        if i < 0 or i >= self.width or j < 0 or j >= self.height:
            raise Exception("Outside of field")

        self._cells[position] = figure

    def get_color(self, point):
        if sum(point) % 2 == 0:
            return Side.WHITE
        else:
            return Side.BLACK

    def __place_row(self, start, figures, side):
        for i in range(start[0], start[0] + len(figures)):
            figure = figures.pop()
            self.__set((i, start[1]), figure(side))

    def point_available(self, point):
        i, j = point
        if i < 0 or i >= self.width or j < 0 or j >= self.height:
            return False
        return True

    def get(self, point):
        if not self.point_available(point):
            raise Exception("Point is outside of filed")
        if point in self._cells:
            return self._cells[point]
        else:
            return None

    def move(self, start, end):
        if not self.point_available(start) or not self.point_available(end):
            return False

        figure = self.get(start)
        if not figure:
            return False

        if not figure.can_move(start, end, self):
            return False

        figure.moved(start, end, self)
        self.__set(start, None)

        if self.get(end):
           self.eaten[figure.side].append(self.get(end))

        self.__set(end, figure)

    def __repr__(self):
        result = ""
        for j in range(self.height):
            for i in range(self.width):
                s = ' ' if not self.get((i, j)) else self.get((i, j)).__repr__()
                result += s
            result += '\n'
        return result

    @property
    def width(self):
        return self._size[0]

    @property
    def height(self):
        return self._size[1]
